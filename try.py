// app/page.tsx
// PAY AFTER PLACEMENT — Data Analyst & Data Engineering (LOUD / MODERN)
// - Stronger "Hybrid Pay After Placement" visibility (big gradient badge + fee strip)
// - Partners logos row (with graceful fallback to monograms)
// - DA ⊂ DE section with 12w vs 20w breakdown bar
// - Syllabus: shows ONLY main topics (module titles) + a clear Capstone/Projects card
// - Pulls from content.json (shape: { courses: [...] } as provided)
// - Cohort + timing + recordings

import Testimonials from "@/components/Testimonials";

export default async function Page() {
  const raw = await getContent();
  const { analyst, engineering } = findCourses(raw);

  const daWeeks = Number(analyst?.duration_weeks ?? 12);
  const deWeeks = Number(engineering?.duration_weeks ?? 20);

  const cohortDate = analyst?.next_cohort_date || engineering?.next_cohort_date || "24 Oct 2025";
  const cohortDisplay = formatCohortDate(cohortDate);
  const classTime = "6–8 pm IST";

  const partners: PartnerItem[] = [
    { name: "Celebal", logo: "/logos/celebal.svg" },
    { name: "Polestar", logo: "/logos/polestar.svg" },
    { name: "Mandle Bulb", logo: "/logos/mandlebulb.svg" },
    { name: "Pratham Software", logo: "/logos/pratham.svg" },
    { name: "Neos Alpha", logo: "/logos/neosalpha.svg" },
  ];

  const experts = [
    {
      name: "Rajat Sinha",
      role: "Data Engineer, Shiprocket",
      img: "https://res.cloudinary.com/dd0e4iwau/image/upload/v1759416236/Rajat_Sinha_p1lgdb.jpg",
      linkedin: "https://www.linkedin.com/in/rajat-sinha-94aa22201/",
    },
    {
      name: "Soumya Awasthi",
      role: "Associate Analytical Engineer, Gartner",
      img: "https://res.cloudinary.com/dd0e4iwau/image/upload/v1759416237/Soumya_Awasthi_bebpm3.jpg",
      linkedin: "https://www.linkedin.com/in/soumyaawasthi08/",
    },
  ];

  return (
    <main className="min-h-screen bg-white text-gray-900">
      {/* Theme tokens — map to your real palette in globals.css */}
      <style>{`
        :root {
          --brand-50:#eef2ff; --brand-100:#e0e7ff; --brand-200:#c7d2fe; --brand-300:#a5b4fc;
          --brand-400:#818cf8; --brand-500:#6366f1; --brand-600:#4f46e5; --brand-700:#4338ca; --brand-800:#3730a3; --brand-900:#312e81;
          --ink:#0b1220; --ink-2:#0a0f1d;
        }
      `}</style>

      {/* ——— HERO ——— */}
      <section className="relative overflow-hidden bg-[#050814]">
        {/* background paint */}
        <div className="absolute inset-0 z-0 pointer-events-none">
          <div className="absolute inset-0 bg-[radial-gradient(55%_45%_at_50%_-10%,_rgba(79,70,229,0.5),_transparent_60%)]" />
          <div className="absolute inset-0 bg-[conic-gradient(from_140deg_at_50%_50%,_rgba(99,102,241,0.25),_transparent_60%)]" />
          <div className="absolute inset-0 bg-[#050814]/90" />
          <div className="absolute inset-0 [background-image:linear-gradient(#ffffff10_1px,transparent_1px),linear-gradient(90deg,#ffffff10_1px,transparent_1px)] [background-size:28px_28px] [mask-image:radial-gradient(60%_55%_at_50%_0%,_#000_45%,_transparent_75%)]" />
        </div>

        <div className="relative z-10 container mx-auto max-w-7xl px-4 sm:px-6 py-14 sm:py-20">
          <div className="text-center text-white">
            {/* BIG hybrid badge */}
            <span className="inline-flex items-center gap-2 rounded-full border border-white/20 bg-gradient-to-r from-[var(--brand-600)] via-[var(--brand-400)] to-[var(--brand-600)] px-4 py-2 text-xs sm:text-sm font-semibold shadow-lg backdrop-blur">
              <SparkleIcon /> Hybrid Pay After Placement
            </span>
            
            <h1 className="mt-4 text-4xl font-extrabold leading-tight text-white drop-shadow-[0_8px_30px_rgba(99,102,241,0.45)] sm:text-5xl md:text-6xl">
              Data Analyst <span className="opacity-90">&</span> Data Engineering Programs
            </h1>
            <p className="mx-auto mt-3 max-w-2xl text-base sm:text-lg text-white/85">
              Mentor-led. Project-first. Job-focused. Start small, pay the balance after placement.
            </p>

            {/* fee strip */}
            <div className="mx-auto mt-4 inline-flex flex-wrap items-center justify-center gap-2 rounded-full border border-white/15 bg-white/10 px-3 py-1.5 text-[11px] text-white/90 shadow-sm">
              <span className="rounded-full bg-white/10 px-2 py-0.5">Data Analyst: ₹7,500 now + ₹30,000 after</span>
              <span className="hidden h-3 w-px bg-white/20 sm:inline-block" />
              <span className="rounded-full bg-white/10 px-2 py-0.5">Data Engineering: ₹10,000 now + ₹30,000 after</span>
            </div>

            <div className="mt-5 flex flex-wrap items-center justify-center gap-2 text-[11px] sm:text-xs">
              <Chip>Online</Chip>
              <Chip>Offline</Chip>
              <Chip>Recordings available</Chip>
              <Chip>6–8 pm IST</Chip>
            </div>

            {/* program quicks */}
            <div className="mt-10 grid gap-5 sm:grid-cols-2">
              <ProgramCard
                dark
                id="data-analyst"
                title={analyst?.title ?? "Data Analyst"}
                subtitle={analyst?.sub_title}
                img={analyst?.img_url}
                feeUpfront="₹7,500"
                feeAfter="₹30,000"
                duration={`${daWeeks} weeks`}
                ctaHref="#analyst"
              />
              <ProgramCard
                dark
                id="data-engineering"
                title={engineering?.title ?? "Data Engineering"}
                subtitle={engineering?.sub_title}
                img={engineering?.img_url}
                feeUpfront="₹10,000"
                feeAfter="₹30,000"
                duration={`${deWeeks} weeks`}
                ctaHref="#engineering"
              />
            </div>

            {/* partners logos */}
            <div className="mt-10">
              <p className="text-xs uppercase tracking-wide text-white/60">Select hiring partners</p>
              <PartnersRow items={partners} />
              <p className="mt-2 text-xs text-white/60">growing network</p>
            </div>
          </div>
        </div>

        {/* sticky mobile CTA */}
        <div className="fixed inset-x-0 bottom-3 z-30 mx-auto w-[92%] sm:hidden">
          <div className="rounded-2xl border border-white/15 bg-white/10 p-2 backdrop-blur">
            <a href="#apply" className="block w-full rounded-xl bg-gradient-to-r from-[var(--brand-600)] to-[var(--brand-400)] px-5 py-3 text-center font-semibold text-white shadow">Start Free Counselling</a>
          </div>
        </div>
      </section>

      {/* ——— GLOBAL KEY STATS ——— */}
      <section className="bg-[#0b1220]">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-10">
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            <Stat dark label="Delivery Modes" value="Online + Offline" />
            <Stat dark label="Class Timing" value={classTime} />
            <Stat dark label="Next Cohort" value={cohortDisplay} />
            <Stat dark label="Recordings" value="Available" />
          </div>
        </div>
      </section>

      {/* ——— FEATURES ——— */}
      <section id="features" className="relative bg-white">
        <div className="absolute inset-x-0 -top-10 -z-10 h-20 bg-gradient-to-b from-[#0b1220] to-transparent opacity-80" />
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-3xl font-extrabold tracking-tight sm:text-4xl">Why these programs</h2>
          <div className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
            <FeatureCard title="Lifetime Access" desc="Content updates, recordings, templates — forever." />
            <FeatureCard title="By Industry, For Industry" desc="Built with hiring managers & working pros." />
            <FeatureCard title="Resume Refactoring" desc="1:1 resume/LinkedIn overhaul tailored to role." />
            <FeatureCard title="Mock Interviews" desc="Regular analytics & system rounds with feedback." />
          </div>
        </div>
      </section>

      {/* ——— EXPERTS ——— */}
      <section id="experts" className="bg-gray-50">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-3xl font-extrabold sm:text-4xl">Backed by Industry Experts</h2>
          <div className="mt-8 grid gap-6 sm:grid-cols-2">
            {experts.map((e, i) => (
              <ExpertCard key={i} {...e} />
            ))}
          </div>
        </div>
      </section>

      {/* ——— DA ⊂ DE (dissection) ——— */}
      <section id="subset" className="bg-white">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-3xl font-extrabold sm:text-4xl">Data Analyst ⊂ Data Engineer</h2>
          <p className="mt-2 max-w-3xl text-gray-700">The Analyst track is the foundation of the Engineering track. Complete the first {daWeeks} weeks for Analyst outcomes; continue to {deWeeks} weeks to master engineering depth.</p>

            {/* segmented bar 12 / 20 */}
          <div className="mt-6 rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
            <div className="text-sm font-semibold text-gray-900">Timeline</div>
            <div className="mt-3 grid grid-cols-[repeat(20,minmax(0,1fr))] overflow-hidden rounded-xl">
              {Array.from({ length: daWeeks }).map((_, i) => (
                <div key={`da-${i}`} className="h-3 bg-[var(--brand-600)]" />
              ))}
              {Array.from({ length: deWeeks - daWeeks }).map((_, i) => (
                <div key={`de-${i}`} className="h-3 bg-[var(--brand-800)]" />
              ))}
            </div>
            <div className="mt-3 grid gap-3 sm:grid-cols-2 text-sm text-gray-700">
              <div className="flex items-start gap-2"><span className="mt-1 inline-block h-2 w-2 rounded bg-[var(--brand-600)]" /><p><b>Weeks 1–{daWeeks}:</b> Analyst foundations — Excel/BI, SQL essentials, stats & storytelling, Python for analysis.</p></div>
              <div className="flex items-start gap-2"><span className="mt-1 inline-block h-2 w-2 rounded bg-[var(--brand-800)]" /><p><b>Weeks {daWeeks + 1}–{deWeeks}:</b> Engineering depth — ETL/ELT, orchestration, cloud, modeling at scale, streaming basics.</p></div>
            </div>
          </div>
        </div>
      </section>

      {/* ——— DATA ANALYST ——— */}
      <CourseSection
        anchor="analyst"
        title={`${analyst?.title ?? "Data Analyst"} — Pay After Placement`}
        subtitle={analyst?.sub_title}
        img={analyst?.img_url}
        feeUpfrontLabel="Enroll with ₹7,500"
        feeAfterLabel="After placement: ₹30,000"
        totalLabel="Total: ₹37,500"
        modules={analyst?.courses_content ?? []}
        duration={`${daWeeks} weeks`}
      />

      {/* ——— DATA ENGINEERING ——— */}
      <CourseSection
        anchor="engineering"
        title={`${engineering?.title ?? "Data Engineering"} — Pay After Placement`}
        subtitle={engineering?.sub_title}
        img={engineering?.img_url}
        feeUpfrontLabel="Enroll with ₹10,000"
        feeAfterLabel="After placement: ₹30,000"
        totalLabel="Total: ₹40,000"
        modules={engineering?.courses_content ?? []}
        duration={`${deWeeks} weeks`}
      />

      {/* ——— Testimonials (kept as-is) ——— */}
      <section className="bg-white">
        <div className="container mx-auto max-w-7xl px-0 py-16">
          <Testimonials />
        </div>
      </section>

      {/* ——— FAQ ——— */}
      <section id="faq" className="relative bg-[#0b1220] text-white">
        <div className="absolute inset-x-0 -top-10 -z-10 h-20 bg-gradient-to-b from-white to-transparent opacity-70" />
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-3xl font-extrabold sm:text-4xl">Frequently asked</h2>
          <div className="mt-6 grid gap-4 sm:gap-6 md:grid-cols-2">
            <Faq dark q="Are classes online or offline?" a="Both. Attend live online sessions or join in-person where available; all sessions have recordings." />
            <Faq dark q="When does the cohort start?" a={`Cohort starts ${cohortDisplay}. Classes run ${classTime}.`} />
            <Faq dark q="How do fees work?" a="Data Analyst: ₹7,500 upfront + ₹30,000 after placement. Data Engineering: ₹10,000 upfront + ₹30,000 after placement." />
            <Faq dark q="Do I keep access?" a="Yes, you get lifetime access to updated materials and recordings." />
          </div>
        </div>
      </section>

      {/* ——— Footer ——— */}
      <footer className="bg-[#0b1220] text-white/80">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-8 text-sm">
          <div className="flex flex-col items-start justify-between gap-4 sm:flex-row">
            <p>© {new Date().getFullYear()} Your Academy. All rights reserved.</p>
            <nav className="flex flex-wrap gap-4">
              <a href="#subset" className="hover:text-white">DA ⊂ DE</a>
              <a href="#analyst" className="hover:text-white">Data Analyst</a>
              <a href="#engineering" className="hover:text-white">Data Engineering</a>
              <a href="#features" className="hover:text-white">Features</a>
              <a href="#experts" className="hover:text-white">Experts</a>
              <a href="#faq" className="hover:text-white">FAQ</a>
            </nav>
          </div>
        </div>
      </footer>
    </main>
  );
}

/* ——— Building blocks ——— */
function SparkleIcon() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" className="opacity-90">
      <path d="M12 3l1.8 4.5L18 9.3l-4.2 1.8L12 15l-1.8-3.9L6 9.3l4.2-1.8L12 3z" stroke="currentColor" strokeWidth="1.5"/>
    </svg>
  );
}

function Chip({ children }: { children: React.ReactNode }) {
  return (
    <span className="inline-flex items-center rounded-full border border-white/15 bg-white/10 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur hover:bg-white/15">
      {children}
    </span>
  );
}

function Stat({ label, value, dark }: { label: string; value: string; dark?: boolean }) {
  const base = dark
    ? "rounded-2xl border border-white/10 bg-white/5 p-5 sm:p-6 text-center text-white/90 shadow-sm hover:bg-white/7"
    : "rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 text-center shadow-sm hover:shadow-md";
  const valueCls = dark ? "text-2xl sm:text-3xl font-extrabold text-white" : "text-2xl sm:text-3xl font-extrabold text-[var(--brand-700)]";
  const labelCls = dark ? "mt-1 text-sm text-white/70" : "mt-1 text-sm text-gray-600";
  return (
    <div className={`${base} transition-transform duration-200 hover:-translate-y-0.5`}>
      <p className={valueCls}>{value}</p>
      <p className={labelCls}>{label}</p>
    </div>
  );
}

function ProgramCard({ id, title, subtitle, img, feeUpfront, feeAfter, duration, ctaHref, dark }:{ id: string; title: string; subtitle?: string; img?: string; feeUpfront: string; feeAfter: string; duration?: string; ctaHref: string; dark?: boolean; }) {
  return (
    <div id={id} className="relative rounded-2xl bg-gradient-to-b from-white/20 to-white/5 p-[1.2px] backdrop-blur">
      <div className={`relative rounded-2xl ${dark ? "bg-white/10 text-white" : "bg-white text-gray-900"} p-5 sm:p-6 shadow-sm transition-transform duration-200 hover:-translate-y-0.5 hover:shadow-lg`}>
        {img ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={img} alt="Program" className="mb-4 h-24 w-full rounded-xl object-cover" />
        ) : null}
        <h3 className="text-lg font-semibold">{title}</h3>
        {subtitle ? <p className={`mt-1 text-sm ${dark ? "text-white/80" : "text-gray-700"}`}>{subtitle}</p> : null}
        <div className={`mt-3 flex flex-wrap items-center gap-2 text-xs ${dark ? "text-white/90" : "text-gray-700"}`}>
          {duration ? <span className="rounded-full border border-current/20 px-2.5 py-1">{duration}</span> : null}
          <span className="rounded-full border border-current/20 px-2.5 py-1">{feeUpfront} to enroll</span>
          <span className="rounded-full border border-current/20 px-2.5 py-1">{feeAfter} after placement</span>
        </div>
        <a href={ctaHref} className="mt-4 inline-flex rounded-lg bg-gradient-to-r from-[var(--brand-600)] to-[var(--brand-400)] px-4 py-2.5 text-sm font-semibold text-white shadow hover:opacity-95 focus:outline-none focus:ring-2 focus:ring-[var(--brand-400)]">View details</a>
      </div>
    </div>
  );
}

function CourseSection({ anchor, title, subtitle, img, feeUpfrontLabel, feeAfterLabel, totalLabel, modules, duration }:{ anchor: string; title: string; subtitle?: string; img?: string; feeUpfrontLabel: string; feeAfterLabel: string; totalLabel: string; modules: any[]; duration?: string; }) {
  // Extract main-topic modules and any Capstone/Projects content
  const mainTopics = Array.isArray(modules) ? modules.map((m: any) => String(m?.title ?? "Module")) : [];
  const capstoneBullets: string[] = collectCapstone(modules);

  return (
    <section id={anchor} className="relative bg-white">
      <div className="absolute inset-x-0 -top-10 -z-10 h-20 bg-gradient-to-b from-gray-50 to-transparent" />
      <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
        <div className="grid gap-6 lg:grid-cols-12 lg:items-start">
          <div className="lg:col-span-7">
            <div className="flex flex-wrap items-center gap-3">
              <h2 className="text-3xl font-extrabold tracking-tight sm:text-4xl">{title}</h2>
              {duration ? <span className="inline-flex items-center rounded-full bg-[var(--brand-50)] px-3 py-1 text-xs font-semibold text-[var(--brand-700)] ring-1 ring-inset ring-[var(--brand-200)]">{duration}</span> : null}
            </div>
            {subtitle ? <p className="mt-2 text-gray-700">{subtitle}</p> : null}
            <div className="mt-4 flex flex-wrap items-center gap-2 text-xs">
              <Badge>Online</Badge>
              <Badge>Offline</Badge>
              <Badge>Recordings available</Badge>
            </div>

            {/* MAIN TOPICS ONLY */}
            <div className="mt-8 grid gap-4 sm:grid-cols-2">
              {mainTopics.map((t, i) => (
                <div key={i} className="rounded-2xl border border-gray-200 bg-white p-4 shadow-sm">
                  <p className="font-semibold text-gray-900">{t}</p>
                </div>
              ))}
            </div>

            {/* Capstone / Projects */}
            {capstoneBullets.length > 0 && (
              <div className="mt-8 rounded-2xl border border-[var(--brand-200)] bg-[var(--brand-50)] p-5 text-[var(--brand-900)]">
                <p className="text-lg font-bold">Capstone / Projects</p>
                <ul className="mt-2 list-disc pl-5 text-sm">
                  {capstoneBullets.map((c, i) => (
                    <li key={i}>{c}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          <div className="lg:col-span-5">
            <div className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 shadow-sm ring-1 ring-transparent transition hover:shadow-lg">
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
              <a href="#apply" className="mt-5 inline-flex w-full items-center justify-center rounded-xl bg-gradient-to-r from-[var(--brand-600)] to-[var(--brand-400)] px-5 py-3 font-semibold text-white shadow hover:opacity-95">Start Free Counselling</a>
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

function Badge({ children }: { children: React.ReactNode }) {
  return (
    <span className="inline-flex items-center rounded-md bg-[var(--brand-50)] px-2.5 py-1 text-[11px] font-semibold text-[var(--brand-700)] ring-1 ring-inset ring-[var(--brand-200)]">
      {children}
    </span>
  );
}

function PillCard({ title, points }: { title: string; points: string[] }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition-transform duration-200 hover:-translate-y-0.5 hover:shadow-lg">
      <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
      <ul className="mt-3 space-y-2 text-sm text-gray-700">
        {points.map((p, i) => (
          <li key={i} className="flex items-start gap-2"><span className="mt-1 inline-block h-1.5 w-1.5 rounded-full bg-[var(--brand-600)]" /> {p}</li>
        ))}
      </ul>
    </div>
  );
}

function PartnersRow({ items }: { items: PartnerItem[] }) {
  return (
    <div className="mt-3 flex flex-wrap items-center justify-center gap-6">
      {items.map((p, i) => (
        <div key={i} className="flex h-8 items-center opacity-90 transition hover:opacity-100">
          {p.logo ? (
            // eslint-disable-next-line @next/next/no-img-element
            <img src={p.logo} alt={p.name} className="h-8 w-auto" />
          ) : (
            <span className="inline-flex items-center rounded-full border border-white/15 bg-white/8 px-3 py-1 text-xs text-w
