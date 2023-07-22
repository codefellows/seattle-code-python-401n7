/* eslint-disable indent */
import Head from "next/head";
import Link from 'next/link';
import { replies } from "../data";
import { useState } from "react";
import Footer from "@/components/Footer";
import Header from "@/components/Header";
import QuestionForm from "@/components/QuestionForm";
import EightBall from "@/components/EightBall";
import ResponseTable from "@/components/ResponseTable";

export default function Home() {
    const [answeredQuestions, setAnsweredQuestions] = useState([]);

    function questionAskedHandler(event) {
        event.preventDefault();
        const randomReply = replies[Math.floor(Math.random() * replies.length)];

        const answeredQuestion = {
            question: event.target.question.value,
            answer: randomReply,
            id: answeredQuestions.length,
        };

        setAnsweredQuestions([...answeredQuestions, answeredQuestion]);
        console.log("answeredQuestions is:", answeredQuestions);
    }

    function getLatestReply() {
        if (answeredQuestions.length === 0) {
            return "Ask a question!";
        }
        return answeredQuestions[answeredQuestions.length - 1].answer;
    }

    return (
        <>
            <Head>
                <title>Expert Eight Ball</title>
            </Head>

            <Header answeredQuestions={answeredQuestions} />

            <main className="flex flex-col items-center py-4 space-y-8">
                {/* Question Form */}
                <QuestionForm questionAskedHandler={questionAskedHandler} />

                {/* Eight Ball */}
                <EightBall getLatestReply={getLatestReply} />

                {/* Table */}
                <ResponseTable answeredQuestions={answeredQuestions} />
            </main>

            <Footer />
        </>
    );
}
