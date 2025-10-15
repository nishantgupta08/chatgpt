import { useState } from "react";
import { Check, ChevronRight, Star, ShieldCheck, Rocket, TrendingUp, BarChart4, Users, Clock, Briefcase, BookOpen, Mail, Phone, Globe, ArrowRight, PlayCircle } from "lucide-react";

export default function LandingPage() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    background: "",
  });
  const [submitted, setSubmitted] = useState(false);

  const onChange = (e) => setForm((f) => ({ ...f, [e.target.name]: e.target.value }));
  const onSubmit = (e) => {
    e.preventDefault();
    // Replace with your submit logic
    setSubmitted(true);
  };

  const usp = [
    { icon: <ShieldCheck className="h-5 w-5"/>, title: "Pay After Placement", desc: "₹0 tuition until you land a qualifying job (₹6 LPA+)." },
    { icon: <Rocket className="h-5 w-5"/>, title: "Job-Ready in 16 Weeks", desc: "Live, mentor-led sprints + hands‑on projects." },
    { icon: <TrendingUp className="h-5 w-5"/>, title: "Hiring Network", desc: "200+ partner companies across tech, fintech & e‑commerce." },
  ];

  const curriculum = [
    {
      unit: "Foundations",
      weeks: "Week 1–2",
      items: ["Excel for Analysis", "Business Metrics", "Data Cleaning Basics", "Case Study: A/B Primer"],
    },
    {
      unit: "SQL Deep Dive",
      weeks: "Week 3–5",
      items: ["SELECT to CTEs", "Window Functions", "Query Optimization", "DBT & Data Warehousing"],
    },
    {
      unit: "Python for DA",
      weeks: "Week 6–8",
      items: ["Pandas & NumPy", "EDA & Visualization", "Stats for DA", "Working with APIs"]
    },
    {
      unit: "BI & Dashboards",
      weeks: "Week 9–11",
      items: ["Power BI / Tableau", "Storytelling with Data", "KPI Dashboards", "Automations"]
    },
    {
      unit: "Business Cases",
      weeks: "Week 12–14",
      items: ["Cohort & Retention", "Funnel Analysis", "Forecasting Lite", "Pricing & AB Testing"]
    },
    {
      unit: "Placement Sprint",
      weeks: "Week 15–16",
      items: ["Interview Prep", "Mock Interviews", "Portfolio & Resume", "Hiring Week"]
    }
  ];

  const faqs = [
    {
      q: "How does Pay After Placement work?",
      a: "You pay ₹0 upfront. After you secure a qualifying role (₹6 LPA+), you pay easy monthly installments capped at a transparent maximum. If you don't get placed within the placement window, you owe nothing.",
    },
    {
      q: "Who is this course for?",
      a: "Final‑year students, recent grads, and professionals transitioning into analytics. Basic comfort with Excel is helpful; we teach the rest from first principles.",
    },
    {
      q: "Is the program live or self‑paced?",
      a: "Hybrid: Live mentor‑led sessions (evenings & weekends IST) plus flexible self‑paced labs. All sessions are recorded.",
    },
    {
      q: "Do you help with placements?",
      a: "Yes — resume & portfolio, mock interviews, referrals to our hiring partners, and direct access to hiring managers during Hiring Week.",
    },
    {
      q: "What tools will I learn?",
      a: "Excel/Google Sheets, SQL (PostgreSQL), Python (Pandas), Power BI/Tableau, dbt basics, Git, and interview tooling.",
    },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-white text-slate-800">
      {/* Top Bar */}
      <header className="sticky top-0 z-50 backdrop-blur bg-white/70 border-b border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <a href="#home" className="flex items-center gap-2 font-semibold text-slate-900">
            <BarChart4 className="h-6 w-6"/> DataLift Academy
          </a>
          <nav className="hidden md:flex items-center gap-6 text-sm">
            <a href="#curriculum" className="hover:text-slate-900">Curriculum</a>
            <a href="#projects" className="hover:text-slate-900">Projects</a>
            <a href="#mentors" className="hover:text-slate-900">Mentors</a>
            <a href="#pricing" className="hover:text-slate-900">Pricing</a>
            <a href="#faq" className="hover:text-slate-900">FAQ</a>
          </nav>
          <a href="#apply" className="inline-flex items-center gap-2 rounded-2xl bg-slate-900 text-white px-4 py-2 text-sm shadow hover:shadow-md transition">
            Apply Now <ChevronRight className="h-4 w-4"/>
          </a>
        </div>
      </header>

      {/* Hero */}
      <section id="home" className="relative overflow-hidden">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 grid lg:grid-cols-2 gap-10 items-center">
          <div>
            <span className="inline-flex items-center gap-2 text-xs uppercase tracking-wider font-medium text-slate-600 bg-slate-100 rounded-full px-3 py-1">
              <ShieldCheck className="h-4 w-4"/> Pay After Placement (₹0 upfront)
            </span>
            <h1 className="mt-4 text-4xl sm:text-5xl font-extrabold leading-tight text-slate-900">
              Become a <span className="bg-clip-text text-transparent bg-gradient-to-r from-slate-900 to-slate-600">Job‑Ready Data Analyst</span> in 16 Weeks
            </h1>
            <p className="mt-4 text-lg text-slate-600 max-w-xl">
              Learn SQL, Python, and BI by doing real business cases. Get placed first, then pay.
            </p>
            <div className="mt-6 flex flex-col sm:flex-row gap-3">
              <a href="#apply" className="inline-flex items-center justify-center rounded-2xl bg-slate-900 text-white px-6 py-3 text-base font-medium shadow hover:shadow-lg transition">
                Start free eligibility check <ArrowRight className="h-5 w-5 ml-2"/>
              </a>
              <a href="#video" className="inline-flex items-center justify-center rounded-2xl border border-slate-300 px-6 py-3 text-base font-medium hover:border-slate-400 transition">
                <PlayCircle className="h-5 w-5 mr-2"/> Watch 60s overview
              </a>
            </div>
            <div className="mt-6 flex items-center gap-4 text-sm text-slate-600">
              <div className="flex items-center gap-1"><Star className="h-4 w-4"/> 4.9/5 (1,200+ reviews)</div>
              <div className="flex items-center gap-1"><Briefcase className="h-4 w-4"/> 1,800+ alumni placed</div>
            </div>
          </div>
          <div className="relative">
            <div className="relative rounded-3xl border border-slate-200 bg-white p-6 shadow-lg">
              <h3 className="text-xl font-semibold">Free Eligibility Check</h3>
              <p className="text-sm text-slate-600">Answer a few questions to see if you qualify for Pay After Placement.</p>
              <form className="mt-4 grid grid-cols-1 gap-3" onSubmit={onSubmit}>
                <label className="text-sm">Full name
                  <input required name="name" value={form.name} onChange={onChange} className="mt-1 w-full rounded-xl border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-400" placeholder="Priya Sharma"/>
                </label>
                <label className="text-sm">Email
                  <input required type="email" name="email" value={form.email} onChange={onChange} className="mt-1 w-full rounded-xl border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-400" placeholder="you@example.com"/>
                </label>
                <label className="text-sm">Phone (WhatsApp preferred)
                  <input required name="phone" value={form.phone} onChange={onChange} className="mt-1 w-full rounded-xl border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-400" placeholder="+91"/>
                </label>
                <label className="text-sm">Your background
                  <select name="background" value={form.background} onChange={onChange} className="mt-1 w-full rounded-xl border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-400">
                    <option value="">Select</option>
                    <option>Final year student</option>
                    <option>Fresher</option>
                    <option>Non‑tech professional</option>
                    <option>Software/IT professional</option>
                  </select>
                </label>
                <button type="submit" className="mt-2 inline-flex items-center justify-center rounded-2xl bg-slate-900 text-white px-4 py-2 font-semibold hover:shadow">
                  {submitted ? "Submitted! We’ll reach out soon" : "Check eligibility"}
                </button>
                <p className="text-xs text-slate-500">By continuing you agree to our Terms and consent to contact via WhatsApp, email & phone.</p>
              </form>
            </div>
          </div>
        </div>
      </section>

      {/* Social proof band */}
      <section className="py-10 border-t border-slate-200 bg-white/60">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <p className="text-center text-sm text-slate-600">Trusted by alumni hired at</p>
          <div className="mt-4 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-6 items-center opacity-80">
            {Array.from({ length: 6 }).map((_, i) => (
              <div key={i} className="h-10 rounded-xl bg-slate-100 border border-slate-200"/>
            ))}
          </div>
        </div>
      </section>

      {/* USPs */}
      <section className="py-16" id="why">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-3 gap-6">
            {usp.map((u, i) => (
              <div key={i} className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
                <div className="flex items-center gap-3">
                  <div className="p-2 rounded-xl bg-slate-900 text-white">{u.icon}</div>
                  <h3 className="font-semibold text-lg">{u.title}</h3>
                </div>
                <p className="mt-3 text-slate-600">{u.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Outcomes */}
      <section className="py-16 bg-slate-50 border-y border-slate-200" id="outcomes">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid lg:grid-cols-3 gap-8 items-start">
          <div>
            <h2 className="text-3xl font-bold">Outcomes you can expect</h2>
            <p className="mt-3 text-slate-600">We focus on core analytics skills and business impact — the exact mix hiring managers want.</p>
            <ul className="mt-4 space-y-2 text-slate-700">
              {[
                "Crack SQL + product case interviews",
                "Ship 3 portfolio‑ready dashboards",
                "Confidently analyze funnels, cohorts & churn",
                "Tell compelling stories with data",
              ].map((t, i) => (
                <li key={i} className="flex items-start gap-2"><Check className="h-5 w-5 mt-0.5"/> {t}</li>
              ))}
            </ul>
          </div>
          <div className="lg:col-span-2 grid sm:grid-cols-3 gap-4">
            {[
              { label: "Avg. CTC for grads", value: "₹8.2 LPA" },
              { label: "Placement rate", value: "92%" },
              { label: "Hiring partners", value: "200+" },
            ].map((kpi, i) => (
              <div key={i} className="rounded-3xl border border-slate-200 bg-white p-6 text-center shadow-sm">
                <div className="text-4xl font-extrabold">{kpi.value}</div>
                <div className="mt-1 text-sm text-slate-600">{kpi.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Curriculum */}
      <section id="curriculum" className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold">Curriculum</h2>
          <p className="mt-2 text-slate-600">A practical, case‑driven syllabus designed with hiring managers.</p>
          <div className="mt-6 grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {curriculum.map((mod, i) => (
              <div key={i} className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
                <div className="text-xs text-slate-500 uppercase tracking-wide">{mod.weeks}</div>
                <h3 className="mt-1 font-semibold text-lg">{mod.unit}</h3>
                <ul className="mt-3 space-y-2 text-sm text-slate-700">
                  {mod.items.map((it, j) => (
                    <li key={j} className="flex items-start gap-2"><Check className="h-4 w-4 mt-0.5"/> {it}</li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Projects */}
      <section id="projects" className="py-16 bg-slate-50 border-y border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold">Hands‑on Projects</h2>
          <p className="mt-2 text-slate-600">Build a portfolio that proves your skills.</p>
          <div className="mt-6 grid md:grid-cols-3 gap-6">
            {[
              { title: "E‑commerce Funnel Dashboard", desc: "Analyze drop‑offs & conversion with SQL + BI.", hours: 18 },
              { title: "Cohort Retention Analysis", desc: "Churn & retention deep dive for a subscription app.", hours: 14 },
              { title: "Pricing A/B Test", desc: "Design, run, and evaluate an experiment.", hours: 10 },
            ].map((p, i) => (
              <div key={i} className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
                <h3 className="font-semibold text-lg">{p.title}</h3>
                <p className="mt-2 text-slate-600">{p.desc}</p>
                <div className="mt-3 inline-flex items-center gap-2 text-xs text-slate-600 bg-slate-100 rounded-full px-3 py-1"><Clock className="h-4 w-4"/> {p.hours} hrs</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Mentors */}
      <section id="mentors" className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold">Meet your mentors</h2>
          <p className="mt-2 text-slate-600">Senior analysts & data leaders from top companies.</p>
          <div className="mt-6 grid md:grid-cols-3 gap-6">
            {[1,2,3].map((m) => (
              <div key={m} className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
                <div className="h-24 w-24 rounded-2xl bg-slate-100 border border-slate-200"/>
                <h3 className="mt-4 font-semibold text-lg">Mentor Name</h3>
                <p className="text-sm text-slate-600">Lead Data Analyst · Company</p>
                <ul className="mt-3 text-sm text-slate-700 space-y-1">
                  <li className="flex gap-2"><Check className="h-4 w-4 mt-0.5"/> 8+ years experience</li>
                  <li className="flex gap-2"><Check className="h-4 w-4 mt-0.5"/> Interviewed 200+ candidates</li>
                </ul>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing */}
      <section id="pricing" className="py-16 bg-slate-900 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-2 gap-8 items-center">
            <div>
              <h2 className="text-3xl font-bold">Simple, outcome‑aligned pricing</h2>
              <p className="mt-3 text-slate-200">Join with ₹0 upfront. Pay only after you get a qualifying offer (₹6 LPA+).</p>
              <ul className="mt-4 space-y-2 text-slate-100">
                <li className="flex items-start gap-2"><Check className="h-5 w-5 mt-0.5"/> No placement, no tuition</li>
                <li className="flex items-start gap-2"><Check className="h-5 w-5 mt-0.5"/> Fair monthly EMIs, capped total</li>
                <li className="flex items-start gap-2"><Check className="h-5 w-5 mt-0.5"/> Scholarships for women & diverse talent</li>
              </ul>
            </div>
            <div className="rounded-3xl bg-white text-slate-900 p-6 border border-slate-200 shadow-lg">
              <div className="text-sm text-slate-500">Pay After Placement</div>
              <div className="mt-1 text-4xl font-extrabold">₹0</div>
              <div className="text-sm text-slate-600">today</div>
              <div className="mt-4 grid gap-2 text-sm">
                {[
                  "EMI starts only after placement",
                  "Payments pause if you lose your job",
                  "Max cap: ₹1,20,000 (example)",
                  "7‑day refund on upfront add‑ons",
                ].map((b, i) => (
                  <div key={i} className="flex gap-2"><Check className="h-4 w-4 mt-0.5"/> {b}</div>
                ))}
              </div>
              <a href="#apply" className="mt-6 inline-flex items-center justify-center rounded-2xl bg-slate-900 text-white px-4 py-2 font-semibold hover:shadow w-full">
                Apply for PAP
              </a>
              <p className="mt-2 text-xs text-slate-500">* Actual terms will be shared upon eligibility confirmation.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-16" id="testimonials">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold">What our alumni say</h2>
          <div className="mt-6 grid md:grid-cols-3 gap-6">
            {["I switched from sales to data in 4 months.", "The SQL drills & mock interviews were game changers.", "Got multiple offers; the dashboard projects impressed."].map((t, i) => (
              <div key={i} className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
                <div className="flex items-center gap-2">
                  <div className="flex text-yellow-500">{Array.from({length:5}).map((_,i)=>(<Star key={i} className="h-4 w-4 fill-yellow-400"/>))}</div>
                </div>
                <p className="mt-3 text-slate-700">“{t}”</p>
                <p className="mt-2 text-sm text-slate-500">— Alumni Name, Data Analyst @ Company</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Eligibility */}
      <section id="eligibility" className="py-16 bg-slate-50 border-y border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid md:grid-cols-2 gap-8">
          <div>
            <h2 className="text-3xl font-bold">Eligibility & schedule</h2>
            <ul className="mt-4 space-y-2 text-slate-700">
              <li className="flex items-start gap-2"><Users className="h-5 w-5 mt-0.5"/> Age 18–30, India based</li>
              <li className="flex items-start gap-2"><BookOpen className="h-5 w-5 mt-0.5"/> Basic Excel comfort; no CS degree required</li>
              <li className="flex items-start gap-2"><Clock className="h-5 w-5 mt-0.5"/> 8–10 hrs/week (evenings & weekends)</li>
              <li className="flex items-start gap-2"><Globe className="h-5 w-5 mt-0.5"/> Online, live + self‑paced</li>
            </ul>
          </div>
          <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
            <h3 className="font-semibold text-lg">Next cohort starts</h3>
            <p className="text-slate-600">Nov 15, 2025 · Limited seats</p>
            <a href="#apply" className="mt-4 inline-flex items-center gap-2 rounded-2xl bg-slate-900 text-white px-4 py-2 font-semibold hover:shadow">
              Reserve your seat <ChevronRight className="h-4 w-4"/>
            </a>
            <p className="mt-2 text-xs text-slate-500">Early applicants receive resume review & interview kit.</p>
          </div>
        </div>
      </section>

      {/* Contact / Apply */}
      <section id="apply" className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid lg:grid-cols-2 gap-10 items-center">
          <div>
            <h2 className="text-3xl font-bold">Apply now — it’s free</h2>
            <p className="mt-2 text-slate-600">We’ll review your profile and invite you to a short assessment. Successful candidates receive a conditional PAP offer.</p>
            <div className="mt-6 grid sm:grid-cols-2 gap-4">
              <div className="rounded-3xl border border-slate-200 bg-white p-6 text-slate-700">
                <h4 className="font-semibold">What happens next?</h4>
                <ol className="mt-2 list-decimal list-inside space-y-1 text-sm">
                  <li>Eligibility check</li>
                  <li>15‑min assessment</li>
                  <li>Offer & onboarding</li>
                </ol>
              </div>
              <div className="rounded-3xl border border-slate-200 bg-white p-6 text-slate-700">
                <h4 className="font-semibold">Need help?</h4>
                <p className="mt-2 text-sm">Write to us at <a href="mailto:admissions@datalift.ac" className="underline">admissions@datalift.ac</a> or WhatsApp +91‑98765‑43210.</p>
              </div>
            </div>
          </div>

          <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
            <h3 className="text-xl font-semibold">Quick application</h3>
            <form className="mt-4 grid grid-cols-1 gap-3" onSubmit={onSubmit}>
              <label className="text-sm">Full name
                <input required name="name" value={form.name} onChange={onChange} className="mt-1 w-full rounded-xl border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-400" placeholder="Priya Sharma"/>
              </label>
              <label className="text-sm">Email
                <input required type="email" name="email" value={form.email} onChange={onChange} className="mt-1 w-full rounded-xl border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-400" placeholder="you@example.com"/>
              </label>
              <label className="text-sm">Phone
                <input required name="phone" value={form.phone} onChange={onChange} className="mt-1 w-full rounded-xl border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-400" placeholder="+91"/>
              </label>
              <label className="text-sm">Background
                <select name="background" value={form.background} onChange={onChange} className="mt-1 w-full rounded-xl border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-400">
                  <option value="">Select</option>
                  <option>Final year student</option>
                  <option>Fresher</option>
                  <option>Non‑tech professional</option>
                  <option>Software/IT professional</option>
                </select>
              </label>
              <button type="submit" className="mt-2 inline-flex items-center justify-center rounded-2xl bg-slate-900 text-white px-4 py-2 font-semibold hover:shadow">
                {submitted ? "Submitted! We’ll reach out soon" : "Apply now"}
              </button>
              <p className="text-xs text-slate-500">By submitting, you consent to receive updates via email/WhatsApp. You can opt out anytime.</p>
            </form>
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section id="faq" className="py-16 bg-slate-50 border-t border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold">Frequently asked questions</h2>
          <div className="mt-6 grid md:grid-cols-2 gap-6">
            {faqs.map((f, i) => (
              <details key={i} className="rounded-2xl border border-slate-200 bg-white p-5">
                <summary className="cursor-pointer font-semibold">{f.q}</summary>
                <p className="mt-2 text-slate-700">{f.a}</p>
              </details>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid md:grid-cols-3 gap-8">
          <div>
            <div className="flex items-center gap-2 font-semibold text-slate-900"><BarChart4 className="h-5 w-5"/> DataLift Academy</div>
            <p className="mt-2 text-sm text-slate-600">Outcome‑aligned education for the next million analysts.</p>
          </div>
          <div className="text-sm">
            <div className="font-semibold">Company</div>
            <ul className="mt-2 space-y-1 text-slate-600">
              <li><a href="#" className="hover:underline">About</a></li>
              <li><a href="#" className="hover:underline">Careers</a></li>
              <li><a href="#" className="hover:underline">Terms & Privacy</a></li>
            </ul>
          </div>
          <div className="text-sm">
            <div className="font-semibold">Contact</div>
            <ul className="mt-2 space-y-1 text-slate-600">
              <li className="flex items-center gap-2"><Mail className="h-4 w-4"/> admissions@datalift.ac</li>
              <li className="flex items-center gap-2"><Phone className="h-4 w-4"/> +91‑98765‑43210</li>
            </ul>
          </div>
        </div>
        <div className="mt-8 text-center text-xs text-slate-500">© {new Date().getFullYear()} DataLift EdTech Pvt. Ltd. All rights reserved.</div>
      </footer>

      {/* Simple analytics placeholder */}
      <script dangerouslySetInnerHTML={{ __html: `/* analytics placeholder */` }} />
    </div>
  );
}
