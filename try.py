// app/landing/page.tsx
// TypeScript rewrite — no `any`, JSON-typed syllabus, bold UI.

import Testimonials from "@/components/Testimonials";
import EnrollForm from "@/components/EnrollForm"; // client component (has onSubmit, WA opt-in default)
import contentJson from "../assets/content.json";
import { JSX } from "react";

/* ===========================
   Types for content.json
=========================== */
export interface Submodule {
  title: string;
  content: string[];
}

export interface Module {
  title: string;
  submodules: Submodule[];
}

export interface UserTestimonial {
  img_url: string;
  name: string;
  linkdin_url: string;
  designation_name: string;
  company_name: string;
  company_business_link: string;
  details: string;
}

export interface Course {
  id: number;
  title: string;
  sub_title: string;
  img_url: string;
  duration_weeks: number;
  next_cohort_date: string; // e.g. "2025-24-10"
  courses_content: Module[];
  right_side_video_url: string;
  user_section?: UserTestimonial[];
}

export type CoursesRoot = { courses: Course[] } | Course[];

function isWrapped(root: CoursesRoot): root is { courses: Course[] } {
  return (root as { courses?: unknown }).courses !== undefined;
}

/* ===========================
   Data & helpers (typed)
=========================== */
const CONTENT: CoursesRoot = (contentJson as unknown) as CoursesRoot;

function pickTrack(raw: CoursesRoot | null, keyword: "analyst" | "engineer"): Course {
  const fallback: Course =
    keyword === "analyst"
      ? {
          id: 1,
          title: "Data Analyst",
          sub_title: "Make businesses smarter with data.",
          img_url: "",
          duration_weeks: 12,
          next_cohort_date: "",
          courses_content: [],
          right_side_video_url: "",
        }
      : {
          id: 2,
          title: "Data Engineering",
          sub_title: "Build reliable data pipelines and platforms.",
          img_url: "",
          duration_weeks: 20,
          next_cohort_date: "",
          courses_content: [],
          right_side_video_url: "",
        };

  if (!raw) return fallback;

  const list: Course[] = isWrapped(raw) ? raw.courses : (raw as Course[]);
  const needle = keyword === "analyst" ? "analyst" : "engineering";
  return list.find((c) => c.title.toLowerCase().includes(needle)) ?? fallback;
}

function formatCohortDate(raw: string): string {
  // accept formats like YYYY-MM-DD or YYYY-DD-MM (given: "2025-24-10")
  if (!raw) return "";
  const parts = raw.split("-");
  const year = parts[0];
  let month = parts[1];
  let day = parts[2];
  if (parts.length === 3) {
    const p2 = Number(parts[1]);
    const p3 = Number(parts[2]);
    if (p2 > 12 && p3 <= 12) {
      // YYYY-DD-MM → YYYY-MM-DD
      month = parts[2];
      day = parts[1];
    }
  }
  const iso = `${year}-${month}-${day}`;
  const d = new Date(iso);
  if (!isNaN(d.getTime())) return d.toLocaleDateString("en-IN", { day: "2-digit", month: "short", year: "numeric" });
  return raw;
}

export interface OutlineItem {
  title: string;
  topics: string[];
}

function condenseModules(modules: Module[]): { outline: OutlineItem[]; capstone: string[] } {
  const outline: OutlineItem[] = [];
  const capstone: string[] = [];

  modules.forEach((m) => {
    const subs = Array.isArray(m?.submodules) ? m.submodules : [];

    // Collect capstone/projects bullets
    const cap = subs.find((s) => /capstone/i.test(s.title)) || subs.find((s) => /project/i.test(s.title));
    if (cap && Array.isArray(cap.content)) {
      cap.content.forEach((line) => {
        if (capstone.length < 12) capstone.push(String(line));
      });
    }

    // Main topics = submodule titles excluding prerequisites/projects/capstone
    const mains = subs
      .filter((s) => !/prereq|project|capstone/i.test(s.title))
      .map((s) => s.title)
      .slice(0, 6);

    outline.push({ title: m.title, topics: mains });
  });

  return { outline, capstone };
}

interface Partner {
  name: string;
  logo?: string;
}
interface Expert {
  name: string;
  role?: string;
  img?: string;
  linkedin?: string;
}

/* ===========================
   Page (typed)
=========================== */
export default function Page(): JSX.Element {
  const dataAnalyst = pickTrack(CONTENT, "analyst");
  const dataEngineering = pickTrack(CONTENT, "engineer");

  const cohortDisplay = formatCohortDate(
    dataAnalyst.next_cohort_date || dataEngineering.next_cohort_date || ""
  );
  const classTime = "6–8 pm IST";
  const daWeeks = Number(dataAnalyst.duration_weeks || 12);
  const deWeeks = Number(dataEngineering.duration_weeks || 20);

  // Replace logo paths with real files under /public/logos
  const partners: Partner[] = [
    { name: "Celebal", logo: "/logos/celebal.svg" },
    { name: "Polestar", logo: "/logos/polestar.svg" },
    { name: "Mandle Bulb", logo: "/logos/mandle-bulb.svg" },
    { name: "Pratham Software", logo: "/logos/pratham-software.svg" },
    { name: "Neos Alpha", logo: "/logos/neos-alpha.svg" },
  ];

  const experts: Expert[] = [
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
      {/* Theme tokens — move into globals.css when ready */}
      <style>{`
        :root {
          --brand-50:#eef2ff; --brand-100:#e0e7ff; --brand-200:#c7d2fe; --brand-300:#a5b4fc;
          --brand-400:#818cf8; --brand-500:#6366f1; --brand-600:#4f46e5; --brand-700:#4338ca; --brand-800:#3730a3; --brand-900:#312e81;
          --ink:#0b1220; --ink-2:#0a0f1d;
        }
      `}</style>

      {/* HERO */}
      <section className="relative overflow-hidden bg-[#050814]">
        {/* dark art */}
        <div className="absolute inset-0 z-0 pointer-events-none">
          <div className="absolute inset-0 bg-[radial-gradient(55%_45%_at_50%_-10%,_rgba(79,70,229,0.5),_transparent_60%)]" />
          <div className="absolute inset-0 bg-[conic-gradient(from_140deg_at_50%_50%,_rgba(99,102,241,0.25),_transparent_60%)]" />
          <div className="absolute inset-0 bg-[#050814]/90" />
          <div className="absolute inset-0 [background-image:linear-gradient(#ffffff10_1px,transparent_1px),linear-gradient(90deg,#ffffff10_1px,transparent_1px)] [background-size:28px_28px] [mask-image:radial-gradient(60%_55%_at_50%_0%,_#000_45%,_transparent_75%)]" />
        </div>

        <div className="relative z-10 container mx-auto max-w-7xl px-4 sm:px-6 py-12 sm:py-16">
          <div className="grid gap-8 lg:grid-cols-12 lg:items-center">
            {/* LEFT: headline + chips + syllabus button */}
            <div className="lg:col-span-6 text-white">
              <h2 className="text-xl sm:text-2xl font-extrabold tracking-tight text-[var(--brand-400)]">
                Hybrid Pay After Placement
              </h2>
              <h1 className="mt-3 text-4xl font-extrabold leading-tight text-white drop-shadow-[0_8px_30px_rgba(99,102,241,0.45)] sm:text-5xl md:text-6xl">
                Data Analyst & Data Engineering Programs
              </h1>
              <p className="mt-3 max-w-xl text-base sm:text-lg text-white/85">
                Mentor-led. Project-first. Job-focused. Start with a small
                enrollment, pay the balance after placement.
              </p>

              <div className="mt-5 flex flex-wrap items-center gap-2 text-[11px] sm:text-xs">
                <Chip>Online</Chip>
                <Chip>Offline</Chip>
                <Chip>Recordings available</Chip>
                <Chip>{classTime}</Chip>
              </div>

              {/* View Syllabus — single button with dropdown */}
              <div className="mt-6 flex">
                <details className="group relative">
                  <summary className="list-none inline-flex cursor-pointer items-center gap-2 rounded-xl border border-white/25 bg-white/10 px-4 py-2 text-white backdrop-blur hover:bg-white/15 [&::-webkit-details-marker]:hidden">
                    {/* icon */}
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden>
                      <path
                        d="M12 3v14m0 0l-4-4m4 4l4-4M6 21h12"
                        stroke="currentColor"
                        strokeWidth="1.6"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      />
                    </svg>
                    View Syllabus
                    {/* chevron */}
                    <svg className="ml-1" width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden>
                      <path
                        d="M6 9l6 6 6-6"
                        stroke="currentColor"
                        strokeWidth="1.8"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      />
                    </svg>
                  </summary>

                  {/* dropdown */}
                  <div className="absolute left-0 z-20 mt-2 w-64 overflow-hidden rounded-xl border border-white/15 bg-[#0b1220] p-1 text-sm text-white shadow-xl backdrop-blur">
                    <a href="#analyst" className="block rounded-lg px-3 py-2 hover:bg-white/10">
                      Data Analyst
                    </a>
                    <a href="#engineering" className="block rounded-lg px-3 py-2 hover:bg-white/10">
                      Data Engineering
                    </a>
                  </div>
                </details>
              </div>

              {/* Partners */}
              <div className="mt-8">
                <p className="text-xs uppercase tracking-wide text-white/60">Select hiring partners</p>
                <PartnersRow items={partners} />
                <p className="mt-2 text-xs text-white/60">growing network</p>
              </div>
            </div>

            {/* RIGHT: top form (client component) */}
            <div className="lg:col-span-6">
              <EnrollForm />
            </div>
          </div>
        </div>

        {/* sticky mobile CTA */}
        <div className="fixed inset-x-0 bottom-3 z-30 mx-auto w-[92%] sm:hidden">
          <div className="rounded-2xl border border-white/15 bg-white/10 p-2 backdrop-blur">
            <a
              href="#apply"
              className="block w-full rounded-xl bg-gradient-to-r from-[var(--brand-600)] to-[var(--brand-400)] px-5 py-3 text-center font-semibold text-white shadow"
            >
              Start Free Counselling
            </a>
          </div>
        </div>
      </section>

      {/* KEY STATS */}
      <section className="bg-[#0b1220]">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-10">
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            <Stat dark label="Delivery Modes" value="Online + Offline" />
            <Stat dark label="Class Timing" value={classTime} />
            <Stat dark label="Next Cohort" value={cohortDisplay || "24 Oct 2025"} />
            <Stat dark label="Recordings" value="Available" />
          </div>
        </div>
      </section>

      {/* FEATURES */}
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

      {/* EXPERTS */}
      <section id="experts" className="bg-gray-50">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-3xl font-extrabold sm:text-4xl">Backed by Industry Experts</h2>
          <div className="mt-8 grid gap-6 sm:grid-cols-2">
            {experts.map((e) => (
              <ExpertCard key={e.name} {...e} />
            ))}
          </div>
        </div>
      </section>

      {/* DA ⊂ DE */}
      <section id="subset" className="bg-white">
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-3xl font-extrabold sm:text-4xl">Data Analyst ⊂ Data Engineer</h2>
          <p className="mt-2 max-w-3xl text-gray-700">
            The Analyst track is the foundation of the Engineering track. Complete the first {daWeeks} weeks for Analyst
            outcomes; continue to {deWeeks} weeks to master engineering depth.
          </p>
          <div className="mt-6 rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
            <div className="text-sm font-semibold text-gray-900">Timeline</div>
            <div className="mt-3 grid grid-cols-[repeat(20,minmax(0,1fr))] overflow-hidden rounded-xl">
              {Array.from({ length: daWeeks }).map((_, i) => (
                <div key={`da-${i}`} className="h-3 bg-[var(--brand-600)]" />
              ))}
              {Array.from({ length: Math.max(deWeeks - daWeeks, 0) }).map((_, i) => (
                <div key={`de-${i}`} className="h-3 bg-[var(--brand-800)]" />
              ))}
            </div>
            <div className="mt-3 grid gap-3 sm:grid-cols-2 text-sm text-gray-700">
              <div className="flex items-start gap-2">
                <span className="mt-1 inline-block h-2 w-2 rounded bg-[var(--brand-600)]" />
                <p>
                  <b>Weeks 1–{daWeeks}:</b> Analyst foundations — Excel/BI, SQL essentials, stats & storytelling,
                  Python for analysis.
                </p>
              </div>
              <div className="flex items-start gap-2">
                <span className="mt-1 inline-block h-2 w-2 rounded bg-[var(--brand-800)]" />
                <p>
                  <b>Weeks {daWeeks + 1}–{deWeeks}:</b> Engineering depth — ETL/ELT, orchestration, cloud, modeling at
                  scale, streaming basics.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* DATA ANALYST */}
      <CourseSection
        anchor="analyst"
        title={`${dataAnalyst.title} — Pay After Placement`}
        subtitle={dataAnalyst.sub_title}
        img={dataAnalyst.img_url}
        feeUpfrontLabel="Enroll with ₹7,500"
        feeAfterLabel="After placement: ₹30,000"
        totalLabel="Total: ₹37,500"
        modules={dataAnalyst.courses_content}
        duration={`${daWeeks} weeks`}
      />

      {/* DATA ENGINEERING */}
      <CourseSection
        anchor="engineering"
        title={`${dataEngineering.title} — Pay After Placement`}
        subtitle={dataEngineering.sub_title}
        img={dataEngineering.img_url}
        feeUpfrontLabel="Enroll with ₹10,000"
        feeAfterLabel="After placement: ₹30,000"
        totalLabel="Total: ₹40,000"
        modules={dataEngineering.courses_content}
        duration={`${deWeeks} weeks`}
      />

      {/* TESTIMONIALS (as-is) */}
      <section className="bg-white">
        <div className="container mx-auto max-w-7xl px-0 py-16">
          <Testimonials />
        </div>
      </section>

      {/* FAQ */}
      <section id="faq" className="relative bg-[#0b1220] text-white">
        <div className="absolute inset-x-0 -top-10 -z-10 h-20 bg-gradient-to-b from-white to-transparent opacity-70" />
        <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
          <h2 className="text-3xl font-extrabold sm:text-4xl">Frequently asked</h2>
          <div className="mt-6 grid gap-4 sm:gap-6 md:grid-cols-2">
            <Faq dark q="Are classes online or offline?" a="Both. Attend live online sessions or join in-person where available; all sessions have recordings." />
            <Faq dark q="When does the cohort start?" a={`Cohort starts ${cohortDisplay || "24 Oct 2025"}. Classes run ${classTime}.`} />
            <Faq dark q="How do fees work?" a="Data Analyst: ₹7,500 upfront + ₹30,000 after placement. Data Engineering: ₹10,000 upfront + ₹30,000 after placement." />
            <Faq dark q="Do I keep access?" a="Yes, you get lifetime access to updated materials and recordings." />
          </div>
        </div>
      </section>

      {/* FOOTER */}
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

/* ===========================
   UI components (typed)
=========================== */
function Chip({ children }: { children: React.ReactNode }): JSX.Element {
  return (
    <span className="inline-flex items-center rounded-full border border-white/15 bg-white/10 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur hover:bg-white/15">
      {children}
    </span>
  );
}

function Stat({ label, value, dark }: { label: string; value: string; dark?: boolean }): JSX.Element {
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

function CourseSection(props: {
  anchor: string;
  title: string;
  subtitle?: string;
  img?: string;
  feeUpfrontLabel: string;
  feeAfterLabel: string;
  totalLabel: string;
  modules: Module[];
  duration?: string;
}): JSX.Element {
  const { anchor, title, subtitle, img, feeUpfrontLabel, feeAfterLabel, totalLabel, modules, duration } = props;
  const { outline, capstone } = condenseModules(modules);
  return (
    <section id={anchor} className="relative bg-white">
      <div className="absolute inset-x-0 -top-10 -z-10 h-20 bg-gradient-to-b from-gray-50 to-transparent" />
      <div className="container mx-auto max-w-7xl px-4 sm:px-6 py-16">
        <div className="grid gap-6 lg:grid-cols-12 lg:items-start">
          <div className="lg:col-span-7">
            <div className="flex flex-wrap items-center gap-3">
              <h2 className="text-3xl font-extrabold tracking-tight sm:text-4xl">{title}</h2>
              {duration ? (
                <span className="inline-flex items-center rounded-full bg-[var(--brand-50)] px-3 py-1 text-xs font-semibold text-[var(--brand-700)] ring-1 ring-inset ring-[var(--brand-200)]">
                  {duration}
                </span>
              ) : null}
            </div>
            {subtitle ? <p className="mt-2 text-gray-700">{subtitle}</p> : null}
            <div className="mt-4 flex flex-wrap items-center gap-2 text-xs">
              <Badge>Online</Badge>
              <Badge>Offline</Badge>
              <Badge>Recordings available</Badge>
            </div>

            {/* MAIN TOPICS */}
            <div className="mt-8 grid gap-6 sm:grid-cols-2">
              {outline.length > 0 ? (
                outline.map((m) => <OutlineCard key={m.title} title={m.title} topics={m.topics} />)
              ) : (
                <div className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 text-sm text-gray-600">
                  Syllabus coming soon.
                </div>
              )}
            </div>

            {/* CAPSTONE / PROJECTS */}
            {capstone.length > 0 && (
              <div className="mt-8">
                <CapstoneCard bullets={capstone} />
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
                <li className="flex items-start gap-3">
                  <StepDot />{" "}
                  <div>
                    <p className="font-semibold">{feeUpfrontLabel}</p>
                    <p>Secure your seat.</p>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <StepDot />{" "}
                  <div>
                    <p className="font-semibold">Train & build</p>
                    <p>Live mentorship, projects, interview prep, and referrals.</p>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <StepDot />{" "}
                  <div>
                    <p className="font-semibold">{feeAfterLabel}</p>
                    <p>Pay the remaining amount after you accept an eligible offer.</p>
                  </div>
                </li>
              </ol>
              <div className="mt-5 rounded-xl border border-[var(--brand-200)] bg-[var(--brand-50)] p-4 text-[var(--brand-900)]">
                <p className="font-semibold">Fee summary</p>
                <p className="text-sm">{totalLabel}</p>
              </div>
              <a
                href="#apply"
                className="mt-5 inline-flex w-full items-center justify-center rounded-xl bg-gradient-to-r from-[var(--brand-600)] to-[var(--brand-400)] px-5 py-3 font-semibold text-white shadow hover:opacity-95"
              >
                Start Free Counselling
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function OutlineCard({ title, topics }: { title: string; topics: string[] }): JSX.Element {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 shadow-sm">
      <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
      <ul className="mt-3 space-y-1 text-sm text-gray-700">
        {topics.map((t) => (
          <li key={t} className="flex items-start gap-2">
            <span className="mt-2 inline-block h-1.5 w-1.5 rounded-full bg-[var(--brand-600)]" />
            {t}
          </li>
        ))}
      </ul>
    </div>
  );
}

function CapstoneCard({ bullets }: { bullets: string[] }): JSX.Element {
  return (
    <div className="relative rounded-2xl bg-gradient-to-r from-[var(--brand-600)] to-[var(--brand-400)] p-[1.5px]">
      <div className="rounded-2xl bg-white p-5 sm:p-6">
        <h3 className="text-lg font-extrabold text-gray-900">Capstone Projects</h3>
        <ul className="mt-3 list-disc space-y-1 pl-5 text-sm text-gray-800">
          {bullets.map((b, i) => (
            <li key={`${b}-${i}`}>{b}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

function StepDot(): JSX.Element {
  return <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-[var(--brand-600)] text-white">•</span>;
}

function Badge({ children }: { children: React.ReactNode }): JSX.Element {
  return (
    <span className="inline-flex items-center rounded-md bg-[var(--brand-50)] px-2.5 py-1 text-[11px] font-semibold text-[var(--brand-700)] ring-1 ring-inset ring-[var(--brand-200)]">
      {children}
    </span>
  );
}

function PartnersRow({ items }: { items: Partner[] }): JSX.Element {
  return (
    <div className="mt-2 flex flex-wrap items-center justify-center gap-4">
      {items.map((p) => (
        <div key={p.name} className="flex h-10 items-center justify-center rounded-lg border border-white/10 bg-white/5 px-3 backdrop-blur">
          {p.logo ? (
            // eslint-disable-next-line @next/next/no-img-element
            <img src={p.logo} alt={p.name} className="max-h-6 w-auto opacity-90" />
          ) : (
            <span className="text-xs text-white/85">{p.name}</span>
          )}
        </div>
      ))}
    </div>
  );
}

function ExpertCard({ name, role, img, linkedin }: Expert): JSX.Element {
  return (
    <div className="flex items-center gap-4 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
      {img ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img src={img} alt={name} className="h-14 w-14 rounded-full object-cover" />
      ) : (
        <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[var(--brand-100)] text-[var(--brand-700)] font-semibold">
          {name.split(" ").map((n) => n[0]).join("")}
        </div>
      )}
      <div className="min-w-0">
        <p className="truncate text-base font-semibold text-gray-900">{name}</p>
        {role ? <p className="truncate text-sm text-gray-600">{role}</p> : null}
        {linkedin ? (
          <a href={linkedin} className="mt-1 inline-flex text-xs font-medium text-[var(--brand-700)] hover:underline">
            LinkedIn
          </a>
        ) : null}
      </div>
    </div>
  );
}

function FeatureCard({ title, desc }: { title: string; desc: string }): JSX.Element {
  return (
    <div className="relative rounded-2xl bg-gradient-to-b from-[var(--brand-100)] to-transparent p-[1.2px]">
      <div className="rounded-2xl border border-gray-200 bg-white p-5 sm:p-6 shadow-sm">
        <h3 className="text-base sm:text-lg font-semibold text-gray-900">{title}</h3>
        <p className="mt-2 text-sm text-gray-700">{desc}</p>
      </div>
    </div>
  );
}

function Faq({ q, a, dark }: { q: string; a: string; dark?: boolean }): JSX.Element {
  const base = dark
    ? "rounded-2xl border border-white/10 bg-white/5 p-5 text-white/90"
    : "rounded-2xl border border-gray-200 bg-white p-5";
  const ans = dark ? "mt-2 text-sm text-white/80" : "mt-2 text-sm text-gray-700";
  return (
    <div className={`${base} transition hover:bg-white/10`}>
      <p className="font-semibold">{q}</p>
      <p className={ans}>{a}</p>
    </div>
  );
}
