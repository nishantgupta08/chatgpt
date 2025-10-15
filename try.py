// app/page.tsx
// Data Analyst Pay After Placement Program — mobile-first, theme-ready.
// Uses JSON-provided course content to render syllabus cards.
// Sections: Hero • Stats (modes/duration/cohort/fees) • Features • Syllabus (from content.json) • Payment • FAQ • Testimonials (as-is)

import Testimonials from "@/components/Testimonials";

export default async function Page() {
  const data = await getDAContent();
  const cohort = formatCohortDate(data?.next_cohort_date);

  return (
    <main className="min-h-screen bg-white text-gray-900">
      {/* Temporary theme tokens — move to globals.css and delete this <style> */}
      <style>{`
        :root {
          /* Map these to your original theme colors */
          --brand-50:  #eff6ff;
          --brand-100: #dbeafe;
          --brand-200: #bfdbfe;
          --brand-300: #93c5fd;
          --brand-400: #60a5fa;
          --brand-500: #3b82f6;
          --brand-600: #2563eb; /* Primary */
          --brand-700: #1d4ed8;
          --brand-800: #1e40af;
          --brand-900: #1e3a8a;
        }
      `}</style>

      {/* ——— HERO ——— */}
      <section className="border-b border-gray-100">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-10 sm:py-14">
          <div className="grid gap-8 lg:grid-cols-12 lg:items-center">
            <div className="lg:col-span-7">
              <span className="inline-flex items-center rounded-full bg-[var(--brand-50)] px-3 py-1 text-xs sm:text-sm font-semibold text-[var(--brand-700)] ring-1 ring-inset ring-[var(--brand-200)]">
                Pay After Placement
              </span>
              <h1 className="mt-3 text-3xl leading-tight font-extrabold sm:text-4xl md:text-5xl">
                {data?.title ?? "Data Analyst"} <span className="text-[var(--brand-700)]">Pay After Placement</span> Program
              </h1>
              <p className="mt-3 text-base sm:text-lg text-gray-700 max-w-2xl">
                {data?.sub_title ?? "Learn data analysis hands-on with real projects, interview prep, and career support."}
              </p>
              <div className="mt-3 flex flex-wrap items-center gap-2 text-[11px] sm:text-xs">
                <Badge>Online</Badge>
                <Badge>Offline</Badge>
                <Badge>Resume refactoring</Badge>
                <Badge>Mock interviews</Badge>
              </div>
              <div className="mt-6 flex flex-col sm:flex-row gap-3">
                <a href="#apply" className="inline-flex justify-center rounded-xl bg-[var(--brand-600)] px-5 py-3 text-white font-semibold shadow hover:bg-[var(--brand-700)]">Start Free Counselling</a>
                <a href="#curriculum" className="inline-flex justify-center rounded-xl border border-gray-300 px-5 py-3 font-semibold text-gray-900 hover:bg-gray-50">View Syllabus</a>
              </div>
            </div>

            <div className="lg:col-span-5">
              <div className="relative rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
                {data?.img_url ? (
                  // eslint-disable-next-line @next/next/no-img-element
                  <img src={data.img_url} alt="Program preview" className="mb-4 h-48 w-full rounded-xl object-cover object-center" />
                ) : null}
                <h3 id="apply" className="text-lg sm:text-xl font-bold">Free Counselling Call</h3>
                <p className="mt-1 text-gray-600 text-sm">Tell us your background and goals. We’ll map the shortest path to your first (or next) data role.</p>
                <form className="mt-4 grid grid-cols-1 gap-3">
                  <input className="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-[var(--brand-600)] focus:outline-none" placeholder="Full name" />
                  <input className="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-[var(--brand-600)] focus:outline-none" placeholder="Email" type="email" />
                  <input className="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-[var(--brand-600)] focus:outline-none" placeholder="Phone" type="tel" />
                  <button type="button" className="mt-1 inline-flex items-center justify-center rounded-lg bg-[var(--brand-600)] px-4 py-2.5 font-semibold text-white hover:bg-[var(--brand-700)] focus:outline-none focus:ring-2 focus:ring-[var(--brand-400)]">Request a Call</button>
                  <p className="text-[11px] text-gray-500">By continuing you agree to be contacted regarding admissions.</p>
                </form>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ——— KEY STATS (replace big partner counts) ——— */}
      <section className="border-b border-gray-100 bg-gray-50">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-10">
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            <Stat label="Delivery Modes" value="Online + Offline" />
            <Stat label="Duration" value={`${data?.duration_weeks ?? 12} weeks`} />
            <Stat label="Next Cohort" value={cohort ?? "TBA"} />
            <Stat label="Fee Plan" value="₹7,500 + ₹22,500" />
          </div>
          {/* If you have few partners, prefer showing logos with caption instead of a big number: */}
          <div className="mt-6 text-center text-sm text-gray-600">
            <span className="rounded-full bg-white px-3 py-1 ring-1 ring-gray-200">Select hiring partners • growing network</span>
          </div>
        </div>
      </section>

      {/* ——— SALIENT FEATURES ——— */}
      <section id="features" className="bg-white">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-2xl sm:text-3xl font-bold">Why this program</h2>
          <div className="mt-6 grid gap-4 sm:gap-6 sm:grid-cols-2 lg:grid-cols-4">
            <FeatureCard title="Lifetime Access" desc="Access updated content, recordings, and resources forever." />
            <FeatureCard title="By Industry, For Industry" desc="Built and reviewed with working data professionals and hiring partners." />
            <FeatureCard title="Resume Refactoring" desc="1:1 resume & LinkedIn revamp tailored to data roles." />
            <FeatureCard title="Mock Interviews" desc="Regular case, SQL, and analytics interviews with feedback." />
          </div>
        </div>
      </section>

      {/* ——— WHAT YOU WILL LEARN (from content.json) ——— */}
      <section id="curriculum" className="bg-white">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-2xl sm:text-3xl font-bold">What you will learn</h2>
          <p className="mt-2 text-gray-700 max-w-2xl text-sm sm:text-base">Auto-loaded from <code>content.json</code> → Data Analyst.</p>

          <div className="mt-7 space-y-6">
            {data?.courses_content?.map((course: any, i: number) => (
              <ModuleCard key={i} title={course.title} submodules={course.submodules} />
            ))}
          </div>
        </div>
      </section>

      {/* ——— HOW PAYMENT WORKS ——— */}
      <section id="pricing" className="bg-gray-50">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-2xl sm:text-3xl font-bold">How payment works</h2>
          <ol className="mt-8 grid gap-4 sm:gap-6 md:grid-cols-3">
            <StepCard step="01" title="Enroll with ₹7,500" desc="Secure your seat with an upfront payment." />
            <StepCard step="02" title="Train & build" desc="Live mentorship, projects, interview prep, and referrals." />
            <StepCard step="03" title="After placement: ₹22,500" desc="Pay the remaining fee once you accept an eligible offer." />
          </ol>

          <div className="mt-8 rounded-xl border border-[var(--brand-200)] bg-[var(--brand-50)] p-4 sm:p-5 text-[var(--brand-900)]">
            <p className="font-semibold">Fee summary</p>
            <p className="text-sm">Total: <strong>₹30,000</strong> (₹7,500 upfront + ₹22,500 after placement). Detailed terms are shared during admissions.</p>
          </div>
        </div>
      </section>

      {/* ——— Testimonials (kept as-is) ——— */}
      <section className="bg-white">
        <div className="container mx-auto max-w-7xl px-0 py-16">
          <Testimonials />
        </div>
      </section>

      {/* ——— FAQ ——— */}
      <section id="faq" className="bg-white">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-2xl sm:text-3xl font-bold">Frequently asked</h2>
          <div className="mt-6 grid gap-4 sm:gap-6 md:grid-cols-2">
            <Faq q="What are the fees?" a="Total fee is ₹30,000 — pay ₹7,500 to enroll and ₹22,500 after placement." />
            <Faq q="Are classes online or offline?" a="Both. Attend live online sessions or join in-person where available." />
            <Faq q="When does the next cohort start?" a={cohort ? `Next cohort: ${cohort}.` : "Cohort date TBA — join the counselling call to get notified."} />
            <Faq q="Who is this program for?" a="Motivated learners seeking a structured, mentor-led path into data roles, including freshers and upskillers." />
          </div>
        </div>
      </section>

      {/* ——— Footer ——— */}
      <footer className="border-t border-gray-100">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-10 text-sm text-gray-600">
          <div className="flex flex-col items-start justify-between gap-4 sm:flex-row">
            <p>© {new Date().getFullYear()} Your Academy. All rights reserved.</p>
            <nav className="flex flex-wrap gap-4">
              <a href="#features" className="hover:text-gray-900">Features</a>
              <a href="#curriculum" className="hover:text-gray-900">Syllabus</a>
              <a href="#pricing" className="hover:text-gray-900">Payment</a>
              <a href="#faq" className="hover:text-gray-900">FAQ</a>
            </nav>
          </div>
        </div>
      </footer>
    </main>
  );
}

/* ——— UI Helpers ——— */
function Badge({ children }: { children: React.ReactNode }) {
  return (
    <span className="inline-flex items-center rounded-md bg-[var(--brand-50)] px-2.5 py-1 text-[11px] font-semibold text-[var(--brand-700)] ring-1 ring-inset ring-[var(--brand-200)]">
      {children}
    </span>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 text-center shadow-sm">
      <p className="text-2xl sm:text-3xl font-extrabold text-[var(--brand-700)]">{value}</p>
      <p className="mt-1 text-sm text-gray-600">{label}</p>
    </div>
  );
}

function StepCard({ step, title, desc }: { step: string; title: string; desc: string }) {
  return (
    <li className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 shadow-sm">
      <div className="inline-flex items-center gap-2 rounded-full bg-[var(--brand-50)] px-3 py-1 text-xs font-semibold text-[var(--brand-700)] ring-1 ring-inset ring-[var(--brand-200)]">
        {step}
      </div>
      <h3 className="mt-3 text-base sm:text-lg font-semibold text-gray-900">{title}</h3>
      <p className="mt-2 text-sm text-gray-700">{desc}</p>
    </li>
  );
}

function FeatureCard({ title, desc }: { title: string; desc: string }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 shadow-sm">
      <h3 className="text-base sm:text-lg font-semibold text-gray-900">{title}</h3>
      <p className="mt-2 text-sm text-gray-700">{desc}</p>
    </div>
  );
}

function Faq({ q, a }: { q: string; a: string }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-5">
      <p className="font-semibold text-gray-900">{q}</p>
      <p className="mt-2 text-gray-700 text-sm">{a}</p>
    </div>
  );
}

function ModuleCard({ title, submodules }: { title: string; submodules: any[] }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 shadow-sm">
      <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
      <div className="mt-3 space-y-3">
        {Array.isArray(submodules) && submodules.map((sm: any, idx: number) => (
          <details key={idx} className="group rounded-lg border border-gray-100 p-3 open:bg-gray-50">
            <summary className="cursor-pointer list-none font-semibold text-gray-800">
              {sm.title ?? `Topic ${idx + 1}`}
            </summary>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-gray-700">
              {Array.isArray(sm?.content) && sm.content.map((c: string, i: number) => (
                <li key={i}>{c}</li>
              ))}
            </ul>
          </details>
        ))}
      </div>
    </div>
  );
}

// —— Data loader for content.json ——
// Accepts the provided structure; also attempts to find the DA object if nested.
async function getDAContent(): Promise<any> {
  try {
    const mod: any = await import("@/content.json");
    const raw = mod.default ?? mod;

    // If the object already looks like the provided snippet
    if (raw?.title && String(raw.title).toLowerCase().includes("analyst") && raw?.courses_content) return raw;

    // If it's an array of courses
    if (Array.isArray(raw)) {
      const found = raw.find((x: any) => String(x?.title ?? "").toLowerCase().includes("analyst"));
      if (found) return found;
    }

    // If it's a map keyed by course names
    const key = Object.keys(raw || {}).find((k) => k.toLowerCase().includes("analyst"));
    if (key) return raw[key];
  } catch (e) {
    // ignore
  }

  // Fallback minimal object
  return {
    title: "Data Analyst",
    sub_title: "Learn data analysis hands-on with projects and mentorship.",
    duration_weeks: 12,
    next_cohort_date: "",
    courses_content: [
      { title: "Foundations", submodules: [{ title: "Basics", content: ["Excel/Sheets", "Descriptive Stats", "KPIs & Dashboards"] }] },
      { title: "SQL & Databases", submodules: [{ title: "Queries", content: ["Joins", "Windows", "Optimization"] }] },
      { title: "Power BI", submodules: [{ title: "DAX", content: ["Time Intelligence", "Interactive Reports"] }] },
    ],
  };
}

function formatCohortDate(raw?: string): string | null {
  if (!raw) return null;
  const candidates = [raw, raw.replace(/\//g, "-")];
  // Try common patterns: YYYY-MM-DD, YYYY-DD-MM, DD-MM-YYYY, MM-DD-YYYY
  for (const s of candidates) {
    const parts = s.split("-").map((p) => parseInt(p, 10));
    if (parts.length === 3) {
      const [a, b, c] = parts;
      const tryOrders = [
        { y: a, m: b, d: c }, // YYYY-MM-DD
        { y: a, m: c, d: b }, // YYYY-DD-MM (given example)
        { y: c, m: b, d: a }, // DD-MM-YYYY
        { y: c, m: a, d: b }, // MM-DD-YYYY
      ];
      for (const o of tryOrders) {
        const dt = new Date(o.y, (o.m ?? 1) - 1, o.d ?? 1);
        if (!isNaN(dt.getTime())) {
          return dt.toLocaleDateString("en-IN", { day: "2-digit", month: "short", year: "numeric" });
        }
      }
    }
  }
  return null;
}
