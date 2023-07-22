export default function QuestionForm({ questionAskedHandler }) {
    return (
        <form
            className="flex w-1/2 p-2 my-4 bg-gray-200"
            onSubmit={questionAskedHandler}
        >
            <input name="question" className="flex-auto pl-1" />
            <button className="bg-gray-500 text-gray-50 px-2 py-1">Ask!</button>
        </form>
    );
}
