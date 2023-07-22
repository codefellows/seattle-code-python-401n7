import Link from "next/link";

// The idea with componentization is to break everything into its own component, ie function
export default function Footer() {
    return (
        <footer className="flex justify-between bg-gray-500 text-gray-50 p-4">
            <p>Expert 8 ball &copy;2023</p>
            <Link href="/careers">Careers</Link>
        </footer>
    );
}
