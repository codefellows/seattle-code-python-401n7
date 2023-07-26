import Head from "next/head";
import { useAuth } from "@/contexts/auth";
import useResource from "@/hooks/useResource";

export default function Home() {
    // const user = null; // this will be authentication code
    // const user = { username: 'somebody' }; // this will be authentication code
    const { user, login, logout } = useAuth(); // user variable and login() function come from the useAuth hook

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
                        {/* <StandList stands={resources} loading={loading} /> */}
                        <CookieStandAdmin />
                    </>
                ) : (
                    <>
                        {/* <h2>Need to log in</h2>
                        <button
                            onClick={() => login("admin", "1234")}
                            className="p-2 text-white bg-gray-500 rounded"
                        >
                            Login
                        </button> */}
                        <LoginForm onLogin={login} />
                    </>
                )}
            </main>
        </div>
    );
}

function LoginForm({ onLogin }) {
    async function handleSubmit(event) {
        event.preventDefault();
        onLogin(event.target.username.value, event.target.password.value);
    }

    return (
        <form onSubmit={handleSubmit}>
            <fieldset autoComplete="off">
                <legend>Log In</legend>
                <label htmlFor="username">Username</label>
                <input name="username" />
                <label htmlFor="password">Password</label>
                <input type="password" name="password" />
                <button>Log In</button>
            </fieldset>
        </form>
    );
}

// Don't need a <li> we need a table!

// function StandList({ stands, loading }) {
//     if (loading) {
//         return <p>Loading...</p>;
//     }

//     return (
//         <ul>
//             {stands.map((stand) => (
//                 <li key={stand.id}>{stand.location}</li>
//             ))}
//         </ul>
//     );
// }

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
        <form onSubmit={handleSubmit}>
            <fieldset>
                <legend>Create Cookie Stand</legend>
                <input placeholder="location" name="location" />
                <input placeholder="minimum" name="minimum" />
                <input placeholder="maximum" name="maximum" />
                <input placeholder="average" name="average" />
                <button>create</button>
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
