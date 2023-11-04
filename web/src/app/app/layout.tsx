import Sidebar from "src/components/sidebar";

export default function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex flex-row">
      <Sidebar />
      {children}
    </div>
  );
}
