export default function ResponseTable({ answeredQuestions }) {
    return (
        <>
            {answeredQuestions.length > 0 && (
                <table className="w-1/2 mx-auto my-4 border border-gray-500">
                    <thead>
                        <tr className="bg-blue-300">
                            <th className="border border-gray-500">Id</th>
                            <th className="border border-gray-500">
                                Question
                            </th>
                            <th className="border border-gray-500">
                                Answer
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {answeredQuestions.map((item) => {
                            return (
                                <tr key={item.id} className="even:bg-blue-50">
                                    <td className="pl-2 border border-gray-700">
                                        {item.id}
                                    </td>
                                    <td className="pl-2 border border-gray-700">
                                        {item.question}
                                    </td>
                                    <td className="pl-2 border border-gray-700">
                                        {item.answer}
                                    </td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            )}
        </>
    )
}
