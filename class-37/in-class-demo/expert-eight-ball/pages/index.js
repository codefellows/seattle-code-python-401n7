/* eslint-disable indent */
import Head from "next/head";
import Link from 'next/link';
import { replies } from "../data";
import { useState } from "react";

export default function Home() {
    const [answeredQuestions, setAnsweredQuestions] = useState([]);

    function questionAskedHandler(event) {
        event.preventDefault();
        //   console.log(event.target.question.value);
        //   alert(event.target.question.value);
        const randomReply = replies[Math.floor(Math.random() * replies.length)];

        const answeredQuestion = {
            question: event.target.question.value,
            reply: randomReply,
            id: answeredQuestions.length,
        };

        //   console.log("setAnsweredQuestions is:", setAnsweredQuestions);
        //   alert(randomReply);
        setAnsweredQuestions([...answeredQuestions, answeredQuestion]);
        console.log("answeredQuestions is:", answeredQuestions);
    }

    function getLatestReply() {
        if (answeredQuestions.length === 0) {
            return "Ask a question!";
        }
        return answeredQuestions[answeredQuestions.length - 1].reply;
    }

    return (
        <>
            <Head>
                <title>Expert Eight Ball</title>
            </Head>

            <header className="flex item-center justify-between bg-gray-500 text-gray-50 p-4">
                <h1>Expert 8 Ball</h1>
                <p>{answeredQuestions.length} question answered</p>
            </header>

            <main className="flex flex-col items-center py-4 space-y-8">
                {/* Question Form */}
                <form
                    className="flex w-1/2 p-2 my-4 bg-gray-200"
                    onSubmit={questionAskedHandler}
                >
                    <input name="question" className="flex-auto pl-1" />
                    <button className="bg-gray-500 text-gray-50 px-2 py-1">
                        Ask!
                    </button>
                </form>

                {/* Eight Ball */}
                <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
                    <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                        <p className="text-xl text-center">
                            {getLatestReply()}
                        </p>
                    </div>
                </div>

                {/* Table */}
                {answeredQuestions.length > 0 && (
                    <table className="w-1/2 mx-auto my-4 border border-gray-500">
                        <thead>
                            <tr>
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
                                    <tr key={item.id}>
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
            </main>

            <footer className="flex justify-between bg-gray-500 text-gray-50 p-4">
                <p>Expert 8 ball &copy;2023</p>
                <Link href="/careers">
                  Careers
                </Link>
            </footer>
        </>
    );
}
