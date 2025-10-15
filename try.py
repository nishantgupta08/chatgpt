// app/page.tsx
// Refactored to keep only the approved sections and to use theme tokens
// so colors match your original Tailwind theme.
// 
// ✅ Kept sections (as requested):
// 1) 120+ Hiring Partners (Stats)
// 2) What You Will Learn
// 3) How Payment Works
// 4) Frequently Asked
// + Testimonials kept exactly via your existing component
//
// 🎨 Color Strategy
// This file uses CSS variables (e.g. --brand-600) so you can map them
// to your **original theme** in `globals.css` (or wherever you define colors).
// Example mapping is embedded below and can be removed once you add it
// to your global styles.

import Testimonials from "@/components/Testimonials";

export default function Page() {
  return (
    <main className="min-h-screen bg-white text-gray-900">
      {/* Temporary theme tokens — move to globals.css and delete this <style> */}
      <style>{`
        :root {
          /* Replace these with your original palette */
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

      {/* ——— 1) TRUST / STATS ——— */}
      <section className="border-b border-gray-100 bg-gray-50">
        <div className="container mx-auto max-w-7xl px-6 py-12">
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            <Stat label="Hiring Partners" value="120+" />
            <Stat label="Avg. Time to Offer" value="10–16 weeks" />
            <Stat label="Mock Interviews" value="Weekly" />
            <Stat label="Alumni Rating" value="4.8/5" />
          </div>
        </div>
      </section>

      {/* ——— 2) WHAT YOU WILL LEARN ——— */}
      <section id="curriculum" className="bg-white">
        <div className="container mx-auto max-w-7xl px-6 py-16">
          <h2 className="text-3xl font-bold sm:text-4xl">What you will learn</h2>
          <p className="mt-3 max-w-2xl text-gray-700">A practical, mentor-led track aligned to landing a role. Modules can be tailored to your background.</p>

          <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            <CurriculumItem
              title="Foundations"
              bullets={["Programming basics","Git & workflows","Problem solving"]}
            />
            <CurriculumItem
              title="Core Skills"
              bullets={["Data structures & algorithms","APIs & databases","Testing & debugging"]}
            />
            <CurriculumItem
              title="Advanced & Projects"
              bullets={["System design","Cloud & DevOps basics","Capstone portfolio"]}
            />
          </div>
        </div>
      </section>

      {/* ——— 3) HOW PAYMENT WORKS ——— */}
      <section id="pricing" className="bg-gray-50">
        <div className="container mx-auto max-w-7xl px-6 py-16">
          <h2 className="text-3xl font-bold sm:text-4xl">How payment works</h2>
          <ol className="mt-8 grid gap-6 md:grid-cols-3">
            <StepCard
              step="01"
              title="Join with ₹0 upfront"
              desc="Start learning without any enrollment fee."
            />
            <StepCard
              step="02"
              title="Train & build"
              desc="Live mentorship, projects, interview prep, and referrals."
            />
            <StepCard
              step="03"
              title="Pay after placement"
              desc="After you accept an eligible offer, pay a capped amount over time."
            />
          </ol>

          <div className="mt-10 rounded-xl border border-[var(--brand-200)] bg-[var(--brand-50)] p-5 text-[var(--brand-900)]">
            <p className="font-semibold">Transparent terms</p>
            <p className="text-sm">No interest, no surprises. Full details are provided during admissions.</p>
          </div>
        </div>
      </section>

      {/* ——— Testimonials (kept as-is) ——— */}
      <section className="bg-white">
        <div className="container mx-auto max-w-7xl px-0 py-16">
          <Testimonials />
        </div>
      </section>

      {/* ——— 4) FREQUENTLY ASKED ——— */}
      <section id="faq" className="bg-white">
        <div className="container mx-auto max-w-7xl px-6 py-16">
          <h2 className="text-3xl font-bold sm:text-4xl">Frequently asked</h2>
          <div className="mt-8 grid gap-6 md:grid-cols-2">
            <Faq q="Do I really pay only after placement?" a="Yes. There is no upfront tuition. A capped payment starts only after you accept an eligible job offer, with terms shared during admissions." />
            <Faq q="Who is this program for?" a="Motivated learners seeking a structured, mentor-led path to a job-ready level, including freshers and upskillers." />
            <Faq q="How long until I’m job-ready?" a="Typical timelines range from 10–16 weeks depending on your background and weekly commitment." />
            <Faq q="Is there a refund?" a="Since there’s no upfront fee, there’s nothing to refund. You only pay after a successful outcome." />
          </div>
        </div>
      </section>

      {/* ——— Footer (neutral, minimal) ——— */}
      <footer className="border-t border-gray-100">
        <div className="container mx-auto max-w-7xl px-6 py-10 text-sm text-gray-600">
          <div className="flex flex-col items-start justify-between gap-4 sm:flex-row">
            <p>© {new Date().getFullYear()} Your Academy. All rights reserved.</p>
            <nav className="flex flex-wrap gap-4">
              <a href="#curriculum" className="hover:text-gray-900">Curriculum</a>
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
function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-6 text-center shadow-sm">
      <p className="text-2xl font-extrabold text-[var(--brand-700)]">{value}</p>
      <p className="mt-1 text-sm text-gray-600">{label}</p>
    </div>
  );
}

function CurriculumItem({ title, bullets }: { title: string; bullets: string[] }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
      <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
      <ul className="mt-3 list-disc space-y-1 pl-5 text-gray-700">
        {bullets.map((b, i) => (
          <li key={i}>{b}</li>
        ))}
      </ul>
    </div>
  );
}

function StepCard({ step, title, desc }: { step: string; title: string; desc: string }) {
  return (
    <li className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
      <div className="inline-flex items-center gap-2 rounded-full bg-[var(--brand-50)] px-3 py-1 text-xs font-semibold text-[var(--brand-700)] ring-1 ring-inset ring-[var(--brand-200)]">
        {step}
      </div>
      <h3 className="mt-3 text-lg font-semibold text-gray-900">{title}</h3>
      <p className="mt-2 text-gray-700">{desc}</p>
    </li>
  );
}

function Faq({ q, a }: { q: string; a: string }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-5">
      <p className="font-semibold text-gray-900">{q}</p>
      <p className="mt-2 text-gray-700">{a}</p>
    </div>
  );
}
