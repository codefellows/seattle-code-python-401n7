/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./pages/**/*.{js,ts,jsx,tsx,mdx}",
        "./components/**/*.{js,ts,jsx,tsx,mdx}",
        "./app/**/*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
        extend: {
            animation: {
                'spin-slow': 'spin 7s linear infinite',
            },
            colors: {
                'custom-salmon':'#FA8072',
            },
        },
    },
    plugins: [],
};
