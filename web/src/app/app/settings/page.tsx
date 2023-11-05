"use client";
import { useUser } from "@auth0/nextjs-auth0/client";
import Image from "next/image";

const Page = () => {
  const user = useUser();
  return (
    <div className="flex h-full w-full flex-col bg-accent-primary">
      <div className="m-1 flex flex-row rounded-lg bg-neutral-primary p-4 shadow-sm">
        <div className="relative h-40 w-40 overflow-hidden rounded-full">
          <Image fill src={user.user?.picture ?? ""} alt="pfp" />
        </div>
        <div className="flex flex-col">
          <input placeholder={user.user?.name ?? "Enter name"} />
          <input type="text" placeholder="about" />
        </div>
      </div>
    </div>
  );
};
export default Page;
