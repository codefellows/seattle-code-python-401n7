/* eslint-disable indent */
import Head from "next/head";

export default function Home() {
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
        <p>Sample text. Eight ball goes here</p>
      </main>

      <footer className="bg-gray-500">
        <p>Expert 8 ball &copy;2023</p>
      </footer>
    </>
  );
}
