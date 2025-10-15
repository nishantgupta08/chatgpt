// app/page.tsx
// Pay After Placement Programs — Data Analyst & Data Engineering
// Mobile-first, theme-ready. Renders two courses on one landing page.
// - Pulls course content from content.json when available
// - Shows cohort start (24 Oct 2025), timing (6–8 pm IST), recordings available
// - Online + Offline delivery
// - Payment plans: DA ₹7,500 + ₹30,000; DE ₹10,000 + ₹30,000
// - Testimonials kept as-is via your component

import Testimonials from "@/components/Testimonials";

export default async function Page() {
  const raw = await getContent();
  const dataAnalyst = pickTrack(raw, "analyst");
  const dataEngineering = pickTrack(raw, "engineer");

  const cohortDisplay = formatCohortDate("24 Oct 2025");
  const classTime = "6–8 pm IST";

  return (
    <main className="min-h-screen bg-white text-gray-900">
      {/* Temporary theme tokens — move to globals.css and delete this <style> */}
      <style>{`
        :root {
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
          <div className="text-center">
            <span className="inline-flex items-center rounded-full bg-[var(--brand-50)] px-3 py-1 text-xs sm:text-sm font-semibold text-[var(--brand-700)] ring-1 ring-inset ring-[var(--brand-200)]">
              Pay After Placement
            </span>
            <h1 className="mt-3 text-3xl leading-tight font-extrabold sm:text-4xl md:text-5xl">
              Data Analyst & Data Engineering Programs
            </h1>
            <p className="mx-auto mt-3 max-w-2xl text-base sm:text-lg text-gray-700">
              Learn with live mentors, real projects, and job support. Start now, pay mostly after placement.
            </p>
            <div className="mt-4 flex flex-wrap items-center justify-center gap-2 text-[11px] sm:text-xs">
              <Badge>Online</Badge>
              <Badge>Offline</Badge>
              <Badge>Recordings available</Badge>
              <Badge>{classTime}</Badge>
              <Badge>Next cohort: {cohortDisplay}</Badge>
            </div>
          </div>

          {/* Program quick cards */}
          <div className="mt-8 grid gap-4 sm:gap-6 sm:grid-cols-2">
            <ProgramCard
              id="data-analyst"
              title={dataAnalyst.title}
              subtitle={dataAnalyst.sub_title}
              img={dataAnalyst.img_url}
              feeUpfront="₹7,500"
              feeAfter="₹30,000"
              ctaHref="#analyst"
            />
            <ProgramCard
              id="data-engineering"
              title={dataEngineering.title}
              subtitle={dataEngineering.sub_title}
              img={dataEngineering.img_url}
              feeUpfront="₹10,000"
              feeAfter="₹30,000"
              ctaHref="#engineering"
            />
          </div>

          {/* Hiring partners note for small partner count */}
          <div className="mt-6 text-center text-sm text-gray-600">
            <span className="rounded-full bg-white px-3 py-1 ring-1 ring-gray-200">Select hiring partners • growing network</span>
          </div>
        </div>
      </section>

      {/* ——— GLOBAL KEY STATS ——— */}
      <section className="border-b border-gray-100 bg-gray-50">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-10">
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            <Stat label="Delivery Modes" value="Online + Offline" />
            <Stat label="Class Timing" value={classTime} />
            <Stat label="Next Cohort" value={cohortDisplay} />
            <Stat label="Recordings" value="Available" />
          </div>
        </div>
      </section>

      {/* ——— SALIENT FEATURES ——— */}
      <section id="features" className="bg-white">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-2xl sm:text-3xl font-bold">Why these programs</h2>
          <div className="mt-6 grid gap-4 sm:gap-6 sm:grid-cols-2 lg:grid-cols-4">
            <FeatureCard title="Lifetime Access" desc="Access updated content, recordings, and resources forever." />
            <FeatureCard title="By Industry, For Industry" desc="Built and reviewed with working professionals and hiring partners." />
            <FeatureCard title="Resume Refactoring" desc="1:1 resume & LinkedIn revamp tailored to the role." />
            <FeatureCard title="Mock Interviews" desc="Regular case, SQL/DS, and system rounds with feedback." />
          </div>
        </div>
      </section>

      {/* ——— DATA ANALYST ——— */}
      <CourseSection
        anchor="analyst"
        title={`${dataAnalyst.title} — Pay After Placement`}
        subtitle={dataAnalyst.sub_title}
        img={dataAnalyst.img_url}
        feeUpfrontLabel="Enroll with ₹7,500"
        feeAfterLabel="After placement: ₹30,000"
        totalLabel="Total: ₹37,500"
        modules={dataAnalyst.courses_content}
      />

      {/* ——— DATA ENGINEERING ——— */}
      <CourseSection
        anchor="engineering"
        title={`${dataEngineering.title} — Pay After Placement`}
        subtitle={dataEngineering.sub_title}
        img={dataEngineering.img_url}
        feeUpfrontLabel="Enroll with ₹10,000"
        feeAfterLabel="After placement: ₹30,000"
        totalLabel="Total: ₹40,000"
        modules={dataEngineering.courses_content}
      />

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
            <Faq q="Are classes online or offline?" a="Both. Attend live online sessions or join in-person where available; all sessions have recordings." />
            <Faq q="When does the cohort start?" a={`Cohort starts ${cohortDisplay}. Classes run ${classTime}.`} />
            <Faq q="How do fees work?" a="Data Analyst: ₹7,500 upfront + ₹30,000 after placement. Data Engineering: ₹10,000 upfront + ₹30,000 after placement." />
            <Faq q="Do I keep access?" a="Yes, you get lifetime access to updated materials and recordings." />
          </div>
        </div>
      </section>

      {/* ——— Footer ——— */}
      <footer className="border-t border-gray-100">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-10 text-sm text-gray-600">
          <div className="flex flex-col items-start justify-between gap-4 sm:flex-row">
            <p>© {new Date().getFullYear()} Your Academy. All rights reserved.</p>
            <nav className="flex flex-wrap gap-4">
              <a href="#analyst" className="hover:text-gray-900">Data Analyst</a>
              <a href="#engineering" className="hover:text-gray-900">Data Engineering</a>
              <a href="#features" className="hover:text-gray-900">Features</a>
              <a href="#faq" className="hover:text-gray-900">FAQ</a>
            </nav>
          </div>
        </div>
      </footer>
    </main>
  );
}

/* ——— Building blocks ——— */
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

function ProgramCard({ id, title, subtitle, img, feeUpfront, feeAfter, ctaHref }:{ id: string; title: string; subtitle?: string; img?: string; feeUpfront: string; feeAfter: string; ctaHref: string; }) {
  return (
    <div id={id} className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 shadow-sm">
      <div className="flex items-start gap-4">
        {img ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={img} alt="Program" className="hidden sm:block h-20 w-28 rounded-md object-cover" />
        ) : null}
        <div>
          <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
          {subtitle ? <p className="mt-1 text-sm text-gray-700 line-clamp-3">{subtitle}</p> : null}
          <div className="mt-3 flex flex-wrap items-center gap-2 text-xs text-gray-700">
            <Badge>{feeUpfront} to enroll</Badge>
            <Badge>{feeAfter} after placement</Badge>
          </div>
          <a href={ctaHref} className="mt-4 inline-flex rounded-lg bg-[var(--brand-600)] px-4 py-2.5 text-sm font-semibold text-white hover:bg-[var(--brand-700)]">View details</a>
        </div>
      </div>
    </div>
  );
}

function CourseSection({ anchor, title, subtitle, img, feeUpfrontLabel, feeAfterLabel, totalLabel, modules }:{ anchor: string; title: string; subtitle?: string; img?: string; feeUpfrontLabel: string; feeAfterLabel: string; totalLabel: string; modules: any[]; }) {
  return (
    <section id={anchor} className="bg-white">
      <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
        <div className="grid gap-6 lg:grid-cols-12 lg:items-start">
          <div className="lg:col-span-7">
            <h2 className="text-2xl sm:text-3xl font-bold">{title}</h2>
            {subtitle ? <p className="mt-2 text-gray-700">{subtitle}</p> : null}
            <div className="mt-4 flex flex-wrap items-center gap-2 text-xs">
              <Badge>Online</Badge>
              <Badge>Offline</Badge>
              <Badge>Recordings available</Badge>
            </div>
            <div className="mt-8 space-y-6">
              {Array.isArray(modules) && modules.length > 0 ? (
                modules.map((course: any, i: number) => (
                  <ModuleCard key={i} title={course.title} submodules={course.submodules} />
                ))
              ) : (
                <div className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 text-sm text-gray-600">Syllabus coming soon.</div>
              )}
            </div>
          </div>

          <div className="lg:col-span-5">
            <div className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 shadow-sm">
              {img ? (
                // eslint-disable-next-line @next/next/no-img-element
                <img src={img} alt="Program" className="mb-4 h-44 w-full rounded-xl object-cover" />
              ) : null}
              <h3 className="text-lg font-bold">How payment works</h3>
              <ol className="mt-4 space-y-3 text-sm">
                <li className="flex items-start gap-3"><StepDot /> <div><p className="font-semibold">{feeUpfrontLabel}</p><p>Secure your seat.</p></div></li>
                <li className="flex items-start gap-3"><StepDot /> <div><p className="font-semibold">Train & build</p><p>Live mentorship, projects, interview prep, and referrals.</p></div></li>
                <li className="flex items-start gap-3"><StepDot /> <div><p className="font-semibold">{feeAfterLabel}</p><p>Pay the remaining amount after you accept an eligible offer.</p></div></li>
              </ol>
              <div className="mt-5 rounded-xl border border-[var(--brand-200)] bg-[var(--brand-50)] p-4 text-[var(--brand-900)]">
                <p className="font-semibold">Fee summary</p>
                <p className="text-sm">{totalLabel}</p>
              </div>
              <a href="#apply" className="mt-5 inline-flex w-full items-center justify-center rounded-xl bg-[var(--brand-600)] px-5 py-3 font-semibold text-white hover:bg-[var(--brand-700)]">Start Free Counselling</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function StepDot() {
  return <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-[var(--brand-600)] text-white">•</span>;
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

/* ——— Data loaders ——— */
async function getContent(): Promise<any> {
  try {
    const mod: any = await import("@/content.json");
    return mod.default ?? mod;
  } catch (e) {
    return null;
  }
}

function pickTrack(raw: any, keyword: "analyst" | "engineer") {
  const fallback = keyword === "analyst"
    ? {
        title: "Data Analyst",
        sub_title: "Make businesses smarter with data.",
        img_url: "",
        courses_content: [],
      }
    : {
        title: "Data Engineering",
        sub_title: "Build reliable data pipelines and platforms.",
        img_url: "",
        courses_content: [],
      };

  if (!raw) return fallback;

  // If top-level object is the track
  if (raw?.title && String(raw.title).toLowerCase().includes(keyword)) return raw;

  // If it's an array of courses
  if (Array.isArray(raw)) {
    const found = raw.find((x: any) => String(x?.title ?? "").toLowerCase().includes(keyword));
    return found ?? fallback;
  }

  // If it's a map keyed by course names
  const key = Object.keys(raw || {}).find((k) => k.toLowerCase().includes(keyword));
  if (key) return raw[key];

  return fallback;
}

function formatCohortDate(raw: string): string {
  // Accepts formats like "24 Oct 2025", "2025-10-24", etc.
  const tryParse = (s: string) => new Date(s);
  const d = tryParse(raw);
  if (!isNaN(d.getTime())) return d.toLocaleDateString("en-IN", { day: "2-digit", month: "short", year: "numeric" });
  return raw;
}
