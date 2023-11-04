import Sidebar from "src/components/sidebar";

export default function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-full flex-row">
      <Sidebar />
      <div className="min-h-screen w-full">{children}</div>
    </div>
  );
}
