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
        {/* Question Form */}
        <form className="flex w-1/2 p-2 my-4 bg-gray-200">
          <input className="flex-auto pl-1" />
          <button className="bg-gray-500 text-gray-50 px-2 py-1">Ask!</button>
        </form>

        {/* Eight Ball */}
        <div className="w-96 h-96 bg-gray-900 rounded-full">
          <div className="relative  w-48 h-48 bg-gray-50">

          </div>
        </div>

      </main>

      <footer className="bg-gray-500 text-gray-50 p-4">
        <p>Expert 8 ball &copy;2023</p>
      </footer>
    </>
  );
}
