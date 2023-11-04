const Page = () => {
  return (
    <div className="flex h-full w-full flex-col space-y-2 bg-accent-primary p-2">
      <div className="flex flex-row space-x-2">
        <div className="flex h-80 w-80 flex-col items-center justify-evenly rounded-lg bg-neutral-primary">
          <div className="h-60 w-60 rounded-full bg-black"></div>
          <div>Budget</div>
        </div>
        <div className="h-80 w-full rounded-lg bg-neutral-primary px-2 py-4">
          <span className="text-xl font-bold text-neutral-secondary">
            Category Breakdown:
          </span>
        </div>
      </div>
      <div className="flex h-full flex-col rounded-lg bg-neutral-primary p-4 shadow-sm">
        <div className="flex flex-row">
          <h2>Recent purchases</h2>
          <button type="button" className="ml-auto">
            import statement
          </button>
        </div>
      </div>
    </div>
  );
};
export default Page;
