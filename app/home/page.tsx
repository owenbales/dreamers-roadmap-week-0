export default function HomePage() {
  const scholarships = [
    { name: "6-7's 67th Annual Scholarship" },
    { name: "Russel House Memorial Scholarship" },
  ];

  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-black">
      <div className="mx-auto max-w-4xl px-6 py-12">
        <h2 className="scroll-m-20 border-b border-zinc-200 pb-2 text-2xl font-semibold tracking-tight text-zinc-900 first:mt-0 dark:border-zinc-800 dark:text-zinc-50">
          Welcome to Dreamers Roadmap!
        </h2>
        <p className="mt-4 leading-7 text-zinc-700 dark:text-zinc-300">
          Dreamers Roadmap is a web app that helps you track scholarships and
          stay on top of opportunities. Sign in and add entries that contain
          the scholarship name, deadline, and more.
        </p>
        <p className="mt-2 leading-7 text-zinc-700 dark:text-zinc-300">
          Add scholarships using the button below.
        </p>
        <hr className="my-8 border-zinc-200 dark:border-zinc-800" />
        <p className="leading-7 text-zinc-600 dark:text-zinc-400">
          Dreamers Roadmap Week-0 Project Deliverable - Owen Bales
        </p>
        <div className="mb-8 mt-10 flex items-center justify-between">
          <h2 className="scroll-m-20 border-b border-zinc-200 pb-2 text-2xl font-semibold tracking-tight text-zinc-900 first:mt-0 dark:border-zinc-800 dark:text-zinc-50">
            Scholarships
          </h2>
          <button
            type="button"
            className="rounded-md bg-zinc-900 px-4 py-2 font-medium text-white transition-colors hover:bg-zinc-800 dark:bg-zinc-50 dark:text-zinc-900 dark:hover:bg-zinc-200"
          >
            Add
          </button>
        </div>
        <div className="overflow-hidden rounded-lg border border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
          <table className="w-full">
            <thead>
              <tr className="border-b border-zinc-200 bg-zinc-50 dark:border-zinc-700 dark:bg-zinc-800">
                <th className="px-6 py-4 text-left text-sm font-semibold text-zinc-900 dark:text-zinc-50">
                  Name
                </th>
              </tr>
            </thead>
            <tbody>
              {scholarships.map((s) => (
                <tr
                  key={s.name}
                  className="border-b border-zinc-200 last:border-0 dark:border-zinc-700"
                >
                  <td className="px-6 py-4 text-sm text-zinc-700 dark:text-zinc-300">
                    {s.name}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
