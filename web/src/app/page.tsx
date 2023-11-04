import Link from "next/link";

export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-b from-[#2e026d] to-[#15162c] text-white">
      <div className="container flex flex-col items-center justify-center gap-12 px-4 py-16 ">
        <h1 className="text-5xl font-extrabold tracking-tight text-white sm:text-[5rem]">
          manage<span className="text-[hsl(280,100%,70%)]">fy</span>
        </h1>
        <div>Solving your finance problems with the power of AI</div>
        <div className="rounded-md bg-blue-500 p-2">Sign in</div>
      </div>
    </main>
  );
}
