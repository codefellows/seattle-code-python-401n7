export default function Header({ answeredQuestions }) {
    return (
        <header className="flex item-center justify-between bg-gray-500 text-gray-50 p-4">
            <h1>Expert 8 Ball</h1>
            <p>{answeredQuestions.length} question answered</p>
        </header>
    );
}
