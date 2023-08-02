import { createContext, useContext, useState } from 'react';
import jwt from 'jsonwebtoken';
const baseUrl = process.env.NEXT_PUBLIC_API_URL;
const tokenUrl = baseUrl + '/api/token/';

const AuthContext = createContext();

export function useAuth() {
    const auth = useContext(AuthContext);
    if (!auth) {
        throw new Error('You forgot AuthProvider!');
    }
    return auth;
}

export function AuthProvider(props) {

    const [state, setState] = useState({
        tokens: null,
        user: null,
        login,
        logout,
        register,
    });

    async function login(username, password) {

        // const response = await axios.post(tokenUrl, { username, password });

        const options = {
            method: "POST",
            body: JSON.stringify({username, password}),
            headers: {'Content-Type': 'application/json'},
        };

        const response = await fetch(tokenUrl, options);

        const data = await response.json();

        const decodedAccess = jwt.decode(data.access);

        const newState = {
            tokens: data,
            user: {
                username: decodedAccess.username,
                email: decodedAccess.email,
                id: decodedAccess.user_id
            },
        };

        setState(prevState => ({ ...prevState, ...newState }));
    }

    function logout() {
        const newState = {
            tokens: null,
            user: null,
        };
        setState(prevState => ({ ...prevState, ...newState }));
    }

    // new
    async function register(username, password, email) {

        const registerUrl = baseUrl + '/api/register';

        const options = {
            method: "POST",
            body: JSON.stringify({username, password, email}),
            headers: {'Content-Type': 'application/json'},
        };

        const response = await fetch(registerUrl, options);

        if (response.ok) {
            const data = await response.json();
            console.log('Registration Successful', data);

            // Automatically log in the user after successful registration
            login(username, password);
        } else {
            console.error('Registration Failed');
        }
    }

    return (
        <AuthContext.Provider value={state}>
            {props.children}
        </AuthContext.Provider>
    );
}
