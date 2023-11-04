const Page = () => {
  return (
    <div className="flex h-full w-full flex-col bg-accent-primary">
      <div className="m-1 flex flex-row rounded-lg bg-neutral-primary p-4 shadow-sm">
        <div className="h-8 w-8 rounded-full bg-slate-200 p-20"></div>
        <div className="flex flex-col">
          <input placeholder="Enter name" />
          <input type="text" placeholder="about" />
        </div>
      </div>
    </div>
  );
};
export default Page;
