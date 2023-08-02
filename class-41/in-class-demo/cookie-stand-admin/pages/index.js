import Head from "next/head";
import { useState } from "react";
import { useAuth } from "@/contexts/auth";
import useResource from "@/hooks/useResource";

export default function Home() {
    const { user, login, logout, register } = useAuth();

    return (
        <div>
            <Head>
                <title>Cookie Stand Admin</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="p-4 space-y-8 text-center">
                <h1 className="text-4xl">
                    Fetching Data from Authenticated API
                </h1>

                {user ? (
                    <>
                        <h2>Welcome username: {user.username}</h2>
                        <h2>Whose email is {user.email}</h2>
                        <button
                            onClick={logout}
                            className="p-2 text-white bg-gray-500 rounded"
                        >
                            Logout
                        </button>
                        <CookieStandAdmin />
                    </>
                ) : (
                    <>
                        <LoginForm onLogin={login} />
                        {/* new register form */}
                        <RegisterForm onRegister={register} />
                    </>
                )}
            </main>
        </div>
    );
}

// New
function RegisterForm({ onRegister }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [email, setEmail] = useState("");
    const [errorMessage, setErrorMessage] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            setErrorMessage('Passwords do not match');
            return;
        }
        // pass the form values of username, password, and email to `register` in auth.js
        onRegister(username, password, email);
    };

    return (
        <form onSubmit={handleSubmit} className="flex flex-col w-2/4 mx-auto">
            <legend className="block text-gray-700 text-lg font-bold mb-2">
                Register New User
            </legend>
            <label className="font-bold text-gray-700 mb-2" htmlFor="username">Username</label>
            <input id="username" type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} className="p-2 mb-4 border border-gray-300 rounded shadow-sm focus:outline-none focus:border-blue-300" />

            <label className="font-bold text-gray-700 mb-2" htmlFor="password">Password</label>
            <input id="password" type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} className="p-2 mb-4 border border-gray-300 rounded shadow-sm focus:outline-none focus:border-blue-300" />

            <label className="font-bold text-gray-700 mb-2" htmlFor="confirmPassword">Confirm Password</label>
            <input id="confirmPassword" type="password" placeholder="Confirm Password" onChange={(e) => setConfirmPassword(e.target.value)} className="p-2 mb-4 border border-gray-300 rounded shadow-sm focus:outline-none focus:border-blue-300" />

            <label className="font-bold text-gray-700 mb-2" htmlFor="email">Email</label>
            <input id="email" type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} className="p-2 mb-4 border border-gray-300 rounded shadow-sm focus:outline-none focus:border-blue-300" />

            {errorMessage && <p className="text-red-500">{errorMessage}</p>}
            <button type="submit" className="mt-4 bg-blue-500 text-white p-2 rounded hover:bg-blue-400">Register</button>
        </form>
    );
}

function LoginForm({ onLogin }) {
    async function handleSubmit(event) {
        event.preventDefault();
        onLogin(event.target.username.value, event.target.password.value);
    }

    return (
        <form
            onSubmit={handleSubmit}
            className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-2/4 mx-auto"
        >
            <fieldset autoComplete="off" className="mb-4">
                <legend className="block text-gray-700 text-lg font-bold mb-2">
                    Log In
                </legend>

                <div className="mb-4">
                    <label
                        className="block text-gray-700 text-sm font-bold mb-2"
                        htmlFor="username"
                    >
                        Username
                    </label>
                    <input
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        name="username"
                    />
                </div>

                <div className="mb-6">
                    <label
                        className="block text-gray-700 text-sm font-bold mb-2"
                        htmlFor="password"
                    >
                        Password
                    </label>
                    <input
                        type="password"
                        name="password"
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    />
                </div>

                <button
                    type="submit"
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                >
                    Log In
                </button>
            </fieldset>
        </form>
    );
}

function CookieStandAdmin() {
    const { resources, deleteResource } = useResource();

    return (
        <>
            <CookieStandForm />
            <CookieStandTable
                stands={resources || []}
                deleteStand={deleteResource}
            />
        </>
    );
}

function CookieStandForm() {
    const { user } = useAuth();
    const { createResource } = useResource();

    function handleSubmit(event) {
        event.preventDefault();
        const info = {
            location: event.target.location.value,
            minimum_customers_per_hour: parseInt(event.target.minimum.value),
            maximum_customers_per_hour: parseInt(event.target.maximum.value),
            average_cookies_per_sale: parseFloat(event.target.average.value),
            owner: user.id,
        };
        createResource(info);
    }

    return (
        <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-2/4 mx-auto" onSubmit={handleSubmit}>
            <fieldset>
                <legend className="block text-gray-700 text-lg font-bold mb-2">Create Cookie Stand</legend>

                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="location">
                        Location
                    </label>
                    <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Location" name="location" id="location" />
                </div>

                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="minimum">
                        Minimum
                    </label>
                    <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Minimum" name="minimum" id="minimum" />
                </div>

                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="maximum">
                        Maximum
                    </label>
                    <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Maximum" name="maximum" id="maximum" />
                </div>

                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="average">
                        Average
                    </label>
                    <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Average" name="average" id="average" />
                </div>

                <div className="flex items-center justify-between">
                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                        Create
                    </button>
                </div>
            </fieldset>
        </form>
    );
}

function CookieStandTable({ stands, deleteStand }) {
    return (
        <table className="my-8">
            <thead>
                <tr>
                    <th>Location</th>
                    <th>6 am</th>
                    <th>7 am</th>
                    <th>8 am</th>
                    <th>9 am</th>
                    <th>10 am</th>
                    <th>11 am</th>
                    <th>12 pm</th>
                    <th>1 pm</th>
                    <th>2 pm</th>
                    <th>3 pm</th>
                    <th>4 pm</th>
                    <th>5 pm</th>
                    <th>6 pm</th>
                    <th>7 pm</th>
                    <th>totals</th>
                </tr>
            </thead>
            <tbody>
                {stands.map((stand) => (
                    <CookieStandRow
                        key={stand.id}
                        info={stand}
                        deleteStand={deleteStand}
                    />
                ))}
            </tbody>
        </table>
    );
}

function CookieStandRow({ info, deleteStand }) {
    function clickHandler() {
        deleteStand(info.id);
    }

    if (info.hourly_sales.length == 0) {
        // bunk data
        info.hourly_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    }

    return (
        <tr>
            <td>
                {info.location} <button onClick={clickHandler}>[x]</button>
            </td>
            {info.hourly_sales.map((slot, index) => (
                <td key={index}>{slot}</td>
            ))}
            <td>{info.hourly_sales.reduce((num, sum) => num + sum, 0)}</td>
        </tr>
    );
}
