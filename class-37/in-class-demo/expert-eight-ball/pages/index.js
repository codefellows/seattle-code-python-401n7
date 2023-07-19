/* eslint-disable indent */
import Head from "next/head";
import { replies } from '../data';
import { useState } from 'react';

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
        id: answeredQuestions.length
      };

      //   console.log("setAnsweredQuestions is:", setAnsweredQuestions);
      //   alert(randomReply);
      setAnsweredQuestions([...answeredQuestions, answeredQuestion]);
      console.log("answeredQuestions is:", answeredQuestions);
    }

    function getLatestReply() {
      if (answeredQuestions.length === 0) {
        return 'Ask a question!';
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
                <p>1 question answered</p>
            </header>

            <main className="flex flex-col items-center py-4 space-y-8">
                {/* Question Form */}
                <form className="flex w-1/2 p-2 my-4 bg-gray-200" onSubmit={questionAskedHandler}>
                    <input name="question" className="flex-auto pl-1" />
                    <button className="bg-gray-500 text-gray-50 px-2 py-1">
                        Ask!
                    </button>
                </form>

                {/* Eight Ball */}
                <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
                    <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                        <p className="text-xl text-center">{getLatestReply()}</p>
                    </div>
                </div>

                {/* Table */}
                <table className="w-1/2 mx-auto my-4">
                  <thead className="border-gray-500">
                    <tr>
                      <th>Id</th>
                      <th>Question</th>
                      <th>Answer</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>0</td>
                      <td>Will it Rain?</td>
                      <td>Yes.</td>
                    </tr>
                  </tbody>
                </table>
            </main>

            <footer className="bg-gray-500 text-gray-50 p-4">
                <p>Expert 8 ball &copy;2023</p>
            </footer>
        </>
    );
}
