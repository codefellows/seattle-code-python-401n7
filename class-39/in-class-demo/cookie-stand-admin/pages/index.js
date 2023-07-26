import Head from "next/head";
import { useAuth } from "@/contexts/auth";
import useResource from "@/hooks/useResource";

export default function Home() {
    // const user = null; // this will be authentication code
    // const user = { username: 'somebody' }; // this will be authentication code
    const { user, login, logout } = useAuth(); // user variable and login() function come from the useAuth hook
    const { resources, loading } = useResource();

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
                        <StandList stands={resources} loading={loading} />
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

function StandList({ stands, loading }) {
    if (loading) {
        return <p>Loading...</p>;
    }

    return (
        <ul>
            {stands.map((stand) => (
                <li key={stand.id}>{stand.location}</li>
            ))}
        </ul>
    );
}
