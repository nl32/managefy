import Link from "next/link";

const Sidebar = () => {
  return (
    <div className="flex h-full min-h-screen w-1/5 flex-col items-center bg-neutral-secondary py-5 text-center text-highlight">
      <h1 className="font-bold">manageFY</h1>
      <div className="flex flex-col space-y-2">
        <Link href="/app/budget">budget</Link>
        <Link href="/app/settings">Settings</Link>
      </div>
      <div className="mt-auto">
        <Link href={"/api/auth/logout"}>signout</Link>
      </div>
    </div>
  );
};
export default Sidebar;
