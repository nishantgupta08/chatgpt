// app/page.tsx
// Landing page with a strong "Pay After Placement" value prop.
// Uses Tailwind CSS utility classes. Assumes you already have a
// <Testimonials /> client component at "@/components/Testimonials" (kept as-is).

import Testimonials from "@/components/Testimonials";

export default function Page() {
  return (
    <main className="min-h-screen bg-white text-gray-900">
      {/* Hero */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 pointer-events-none select-none [background:radial-gradient(60%_40%_at_50%_-10%,_#dbeafe_0%,_transparent_60%)]" />
        <div className="container mx-auto max-w-7xl px-6 pt-16 pb-20 lg:pt-24 lg:pb-28">
          <div className="grid items-center gap-10 lg:grid-cols-12">
            <div className="lg:col-span-7">
              <span className="inline-flex items-center rounded-full bg-blue-50 px-3 py-1 text-sm font-medium text-blue-700 ring-1 ring-inset ring-blue-200">
                Pay After Placement
              </span>
              <h1 className="mt-4 text-4xl font-extrabold tracking-tight sm:text-5xl lg:text-6xl">
                Learn. Get Hired. <span className="text-blue-600">Then</span> Pay.
              </h1>
              <p className="mt-4 max-w-2xl text-lg leading-relaxed text-gray-700">
                A mentor-led program designed to take you from fundamentals to a job-ready level. You pay only after you land a qualifying role—no upfront tuition.
              </p>

              <div className="mt-8 flex flex-wrap gap-3">
                <a
                  href="#apply"
                  className="inline-flex items-center justify-center rounded-xl bg-blue-600 px-5 py-3 text-white font-semibold shadow hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400"
                >
                  Apply for Counselling
                </a>
                <a
                  href="#curriculum"
                  className="inline-flex items-center justify-center rounded-xl border border-gray-300 px-5 py-3 font-semibold text-gray-900 hover:bg-gray-50"
                >
                  View Curriculum
                </a>
              </div>

              <div className="mt-8 flex flex-wrap items-center gap-x-6 gap-y-3 text-sm text-gray-600">
                <div className="flex items-center gap-2"><CheckIcon /> No upfront fees</div>
                <div className="flex items-center gap-2"><CheckIcon /> Live mentorship</div>
                <div className="flex items-center gap-2"><CheckIcon /> Placement support</div>
                <div className="flex items-center gap-2"><CheckIcon /> Job-ready portfolio</div>
              </div>
            </div>

            <div className="lg:col-span-5">
              <div className="relative mx-auto max-w-lg overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm">
                <div className="p-6">
                  <h3 id="apply" className="text-xl font-bold">Free Counselling Call</h3>
                  <p className="mt-1 text-gray-600">Tell us about your background and goals. We’ll map a path to your first (or next) role.</p>
                  <form className="mt-6 grid grid-cols-1 gap-4">
                    <input className="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none" placeholder="Full name" />
                    <input className="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none" placeholder="Email" type="email" />
                    <input className="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none" placeholder="Phone" type="tel" />
                    <button type="button" className="mt-2 inline-flex items-center justify-center rounded-lg bg-blue-600 px-4 py-2.5 font-semibold text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400">Request a Call</button>
                    <p className="text-xs text-gray-500">By continuing you agree to be contacted regarding admissions.</p>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Trust / Stats */}
      <section className="border-y border-gray-100 bg-gray-50">
        <div className="container mx-auto max-w-7xl px-6 py-10">
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            <Stat label="Hiring Partners" value="120+" />
            <Stat label="Avg. Time to Offer" value="10–16 weeks" />
            <Stat label="Interview Readiness" value="Mock + Review" />
            <Stat label="Alumni Satisfaction" value="4.8/5" />
          </div>
        </div>
      </section>

      {/* Why Pay After Placement */}
      <section id="why" className="container mx-auto max-w-7xl px-6 py-16">
        <div className="grid gap-12 lg:grid-cols-12">
          <div className="lg:col-span-5">
            <h2 className="text-3xl font-bold sm:text-4xl">Aligned incentives. Real outcomes.</h2>
            <p className="mt-4 text-gray-700">We win only when you do. Instead of paying a large tuition up front, you pay a capped amount only after you secure a qualifying job. That means our focus stays on job outcomes: rigorous curriculum, practical projects, and interview prep.</p>
            <ul className="mt-6 space-y-3 text-gray-700">
              <li className="flex items-start gap-3"><Badge>₹0 upfront</Badge> Get started without financial burden.</li>
              <li className="flex items-start gap-3"><Badge>Cap on fees</Badge> Transparent terms, no surprises.</li>
              <li className="flex items-start gap-3"><Badge>Career support</Badge> 1:1 mentorship, referrals & mock interviews.</li>
            </ul>
          </div>
          <div className="lg:col-span-7">
            <div className="grid gap-6 sm:grid-cols-2">
              <FeatureCard title="Live Mentor Sessions" desc="Weekly live classes, office hours, and feedback." />
              <FeatureCard title="Real Projects" desc="Build deployable projects to showcase skills." />
              <FeatureCard title="Interview Prep" desc="DSA drills, system design, resume & LinkedIn." />
              <FeatureCard title="Placement Support" desc="Referrals, hiring fairs, and offer negotiation." />
            </div>
          </div>
        </div>
      </section>

      {/* Curriculum Preview */}
      <section id="curriculum" className="bg-gray-50">
        <div className="container mx-auto max-w-7xl px-6 py-16">
          <h2 className="text-3xl font-bold sm:text-4xl">What you’ll learn</h2>
          <p className="mt-3 max-w-2xl text-gray-700">A streamlined path from fundamentals to job-ready skills. Exact tracks can be customized based on your background.</p>
          <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            <CurriculumItem title="Foundations" bullets={["Programming basics","Git & workflows","Problem solving"]} />
            <CurriculumItem title="Core Skills" bullets={["Data structures & algorithms","APIs & databases","Testing & debugging"]} />
            <CurriculumItem title="Advance & Projects" bullets={["System design","Cloud & DevOps basics","Capstone portfolio"]} />
          </div>
        </div>
      </section>

      {/* Pricing explainer for Pay After Placement */}
      <section id="pricing" className="container mx-auto max-w-7xl px-6 py-16">
        <div className="grid items-center gap-10 lg:grid-cols-12">
          <div className="lg:col-span-6">
            <h2 className="text-3xl font-bold sm:text-4xl">How payment works</h2>
            <ol className="mt-6 space-y-4 text-gray-700">
              <li className="flex items-start gap-3">
                <Step /> <div>
                  <p className="font-semibold">Join with ₹0 upfront</p>
                  <p>Begin learning with no tuition fees at enrollment.</p>
                </div>
              </li>
              <li className="flex items-start gap-3">
                <Step /> <div>
                  <p className="font-semibold">Train & build</p>
                  <p>Attend live sessions, finish projects, and get matched to mentors.</p>
                </div>
              </li>
              <li className="flex items-start gap-3">
                <Step /> <div>
                  <p className="font-semibold">Get placed</p>
                  <p>When you accept an eligible offer, pay a capped fee over time.</p>
                </div>
              </li>
            </ol>

            <div className="mt-8 rounded-xl border border-blue-200 bg-blue-50 p-4 text-sm text-blue-900">
              <p className="font-semibold">Transparent terms.</p>
              <p>No interest. No surprises. Everything is shared up front during admissions.</p>
            </div>
          </div>
          <div className="lg:col-span-6">
            <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
              <h3 className="text-xl font-bold">At a glance</h3>
              <div className="mt-5 grid grid-cols-2 gap-4 text-sm">
                <div className="rounded-lg border p-4">
                  <p className="font-semibold">Upfront Fee</p>
                  <p className="mt-1 text-gray-700">₹0</p>
                </div>
                <div className="rounded-lg border p-4">
                  <p className="font-semibold">Payment Trigger</p>
                  <p className="mt-1 text-gray-700">After qualifying offer</p>
                </div>
                <div className="rounded-lg border p-4">
                  <p className="font-semibold">Cap</p>
                  <p className="mt-1 text-gray-700">Transparent & fixed</p>
                </div>
                <div className="rounded-lg border p-4">
                  <p className="font-semibold">Support</p>
                  <p className="mt-1 text-gray-700">Till placement</p>
                </div>
              </div>
              <a href="#apply" className="mt-6 inline-flex w-full items-center justify-center rounded-xl bg-blue-600 px-5 py-3 font-semibold text-white hover:bg-blue-700">Start Free Counselling</a>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials — kept exactly via the existing component */}
      <section className="bg-white">
        <div className="container mx-auto max-w-7xl px-0 py-16">
          <Testimonials />
        </div>
      </section>

      {/* FAQ */}
      <section id="faq" className="bg-gray-50">
        <div className="container mx-auto max-w-7xl px-6 py-16">
          <h2 className="text-3xl font-bold sm:text-4xl">Frequently asked</h2>
          <div className="mt-8 grid gap-6 md:grid-cols-2">
            <Faq q="Do I really pay only after placement?" a="Yes. There is no upfront tuition. A capped payment starts only after you accept an eligible job offer, with terms shared during admissions." />
            <Faq q="Who is this program for?" a="Motivated learners looking for a structured, mentor-led path to a job-ready level, including freshers and upskillers." />
            <Faq q="How long until I’m job-ready?" a="Typical timelines range from 10–16 weeks depending on your background and weekly commitment." />
            <Faq q="Is there a refund?" a="Since there’s no upfront fee, there’s nothing to refund. You only pay after a successful outcome." />
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-gray-100">
        <div className="container mx-auto max-w-7xl px-6 py-10 text-sm text-gray-600">
          <div className="flex flex-col items-start justify-between gap-4 sm:flex-row">
            <p>© {new Date().getFullYear()} Your Academy. All rights reserved.</p>
            <nav className="flex flex-wrap gap-4">
              <a href="#why" className="hover:text-gray-900">Why us</a>
              <a href="#curriculum" className="hover:text-gray-900">Curriculum</a>
              <a href="#pricing" className="hover:text-gray-900">Pricing</a>
              <a href="#faq" className="hover:text-gray-900">FAQ</a>
            </nav>
          </div>
        </div>
      </footer>
    </main>
  );
}

/* ——— Small presentational helpers (no external deps) ——— */
function CheckIcon() {
  return (
    <svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" className="shrink-0">
      <path d="M20 7L10 17l-6-6" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

function Step() {
  return (
    <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-blue-600 text-white">•</span>
  );
}

function Badge({ children }: { children: React.ReactNode }) {
  return (
    <span className="mt-1 inline-flex shrink-0 items-center rounded-md bg-blue-50 px-2 py-1 text-xs font-semibold text-blue-700 ring-1 ring-inset ring-blue-200">
      {children}
    </span>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl border border-gray-200 bg-white p-6 text-center shadow-sm">
      <p className="text-2xl font-extrabold">{value}</p>
      <p className="mt-1 text-sm text-gray-600">{label}</p>
    </div>
  );
}

function FeatureCard({ title, desc }: { title: string; desc: string }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
      <h3 className="text-lg font-semibold">{title}</h3>
      <p className="mt-2 text-gray-700">{desc}</p>
    </div>
  );
}

function CurriculumItem({ title, bullets }: { title: string; bullets: string[] }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
      <h3 className="text-lg font-semibold">{title}</h3>
      <ul className="mt-3 list-disc space-y-1 pl-5 text-gray-700">
        {bullets.map((b, i) => (
          <li key={i}>{b}</li>
        ))}
      </ul>
    </div>
  );
}

function Faq({ q, a }: { q: string; a: string }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-5">
      <p className="font-semibold">{q}</p>
      <p className="mt-2 text-gray-700">{a}</p>
    </div>
  );
}
