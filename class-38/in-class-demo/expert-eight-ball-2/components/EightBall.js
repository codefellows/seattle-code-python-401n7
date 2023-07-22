export default function EightBall({ getLatestReply }) {
    return (
        <div className="animate-spin-slow w-96 h-96 mx-auto my-4 bg-custom-salmon rounded-full">
            <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                <p className="text-xl text-center">{getLatestReply()}</p>
            </div>
        </div>
    );
}
