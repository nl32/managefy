import Link from "next/link";

const Sidebar = () => {
  return (
    <div className="flex h-full flex-col bg-slate-100">
      <h1 className="font-bold">manageFY</h1>
      <div className="flex flex-col">
        <Link href="/app/budget">budget</Link>
        <Link href="/app/settings">Settings</Link>
      </div>
    </div>
  );
};
export default Sidebar;
