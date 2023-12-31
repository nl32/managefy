import "src/styles/globals.css";

import { Inter } from "next/font/google";
import { cookies } from "next/headers";

import { TRPCReactProvider } from "src/trpc/react";
import { UserProvider } from "@auth0/nextjs-auth0/client";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-sans",
});

export const metadata = {
  title: "Create T3 App",
  description: "Generated by create-t3-app",
  icons: [{ rel: "icon", url: "/favicon.ico" }],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`font-sans ${inter.variable}`}>
        <UserProvider>
          <TRPCReactProvider cookies={cookies().toString()}>
            <div className="max-h-screen overflow-y-scroll">{children}</div>
          </TRPCReactProvider>
        </UserProvider>
      </body>
    </html>
  );
}
