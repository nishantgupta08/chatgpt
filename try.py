/* eslint-disable @next/next/no-img-element */
"use client";
import Image from "next/image";
import { Icon } from "@iconify/react";
import data from "@/app/assets/content.json";

type Course = {
  id: number | string;
  highlighted_title?: string;
  title: string;
  img_url?: string;
  cover_url?: string;
  duration_weeks?: number;      // 👈 add in content.json
  hours_per_week?: number;
  level?: string;
  next_cohort_date?: string;    // 👈 add in content.json (ISO date: YYYY-MM-DD)
  seats_left?: number;
  badges?: string[];
  syllabus_url?: string;
  features?: string[];
};

const palette: Record<string, string> = {
  "DATA ANALYST": "bg-amber-100 text-amber-900 border-amber-300",
  "DATA ENGINEERING": "bg-sky-100 text-sky-900 border-sky-300",
  "WEB DEVELOPMENT": "bg-violet-100 text-violet-900 border-violet-300",
};

function monthsFromWeeks(weeks?: number): number | null {
  if (!weeks || weeks <= 0) return null;
  // ~4.3 weeks per month
  return Math.max(1, Math.round(weeks / 4.3));
}

function fmtDate(iso?: string): string | null {
  if (!iso) return null;
  const d = new Date(iso);
  if (isNaN(d.getTime())) return null;
  // India-friendly format; change locale if you prefer
  return d.toLocaleDateString("en-IN", { year: "numeric", month: "short", day: "numeric" });
}

export default function CoursesSectionPro() {
  const block = (data as any)?.homepage?.courses;
  const courses: Course[] = block?.courses ?? [];

  return (
    <section id="courses" aria-label="Courses" className="bg-white py-10 md:py-16">
      <div className="container">
        <header className="mb-6 md:mb-8">
          <h2 className="text-2xl md:text-3xl font-extrabold tracking-tight text-slate-900">
            {block?.title ?? "Courses"}
          </h2>
          <p className="mt-1 text-slate-600">
            {block?.sub_title ?? "Learn with production-grade projects and expert mentorship."}
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 md:gap-6">
          {courses.map((c) => {
            const tag = (c.highlighted_title || "").toUpperCase().trim();
            const cover = c.cover_url || c.img_url || "/images/courses/placeholder.jpg";
            const tagStyle = palette[tag] ?? "bg-slate-100 text-slate-900 border-slate-300";

            const months = monthsFromWeeks(c.duration_weeks);
            const weeks = c.duration_weeks;
            const hrs = c.hours_per_week;
            const cohort = fmtDate(c.next_cohort_date);

            return (
              <article
                key={c.id}
                className="group rounded-2xl border border-slate-200 overflow-hidden bg-white shadow-sm hover:shadow-md transition"
              >
                {/* Cover */}
                <div className="relative aspect-[16/9]">
                  <Image
                    src={cover}
                    alt={`${c.title} course cover`}
                    fill
                    sizes="(min-width: 1280px) 33vw, (min-width: 768px) 50vw, 100vw"
                    className="object-cover transition-transform duration-300 group-hover:scale-[1.02]"
                    priority
                  />
                  {tag && (
                    <span
                      className={`absolute left-3 top-3 inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-extrabold border ${tagStyle}`}
                    >
                      {tag}
                    </span>
                  )}
                </div>

                {/* Body */}
                <div className="p-4 md:p-5">
                  <h3 className="text-lg md:text-xl font-extrabold text-slate-900">{c.title}</h3>

                  {/* NEW: concise facts row */}
                  <div className="mt-2 flex flex-wrap items-center gap-3 text-[12px] font-semibold text-slate-600">
                    {months && (
                      <span className="inline-flex items-center gap-1">
                        <Icon icon="mdi:calendar-month-outline" className="text-slate-500" />
                        ~{months} {months > 1 ? "months" : "month"}
                      </span>
                    )}
                    {typeof weeks === "number" && weeks > 0 && (
                      <span className="inline-flex items-center gap-1">
                        <Icon icon="mdi:calendar-outline" className="text-slate-500" />
                        {weeks} weeks
                      </span>
                    )}
                    {typeof hrs === "number" && hrs > 0 && (
                      <span className="inline-flex items-center gap-1">
                        <Icon icon="mdi:clock-outline" className="text-slate-500" />
                        {hrs} hrs/week
                      </span>
                    )}
                  </div>

                  {/* NEW: next cohort line */}
                  {cohort && (
                    <div className="mt-2 inline-flex items-center gap-2 text-[12px] font-bold px-2 py-1 rounded-full bg-slate-50 border border-slate-200 text-slate-700">
                      <Icon icon="mdi:calendar-start" />
                      Next cohort: {cohort}
                    </div>
                  )}

                  {/* Features (keep short) */}
                  {c.features?.length ? (
                    <ul className="mt-3 space-y-1.5">
                      {c.features.slice(0, 3).map((f, idx) => (
                        <li key={idx} className="flex items-start gap-2 text-[13px] text-slate-700">
                          <span className="mt-[2px] size-[6px] rounded-full bg-slate-900 shrink-0" />
                          <span>{f}</span>
                        </li>
                      ))}
                    </ul>
                  ) : null}

                  {/* Actions */}
                  <div className="mt-4 flex flex-wrap items-center gap-3">
                    <a
                      href={`/courses/${encodeURIComponent(String(c.id))}`}
                      className="inline-flex items-center justify-center px-4 py-2 rounded-full border-2 border-black bg-black text-white font-bold text-sm hover:-translate-y-0.5 transition"
                    >
                      View Course
                    </a>

                    {c.syllabus_url && (
                      <a
                        href={c.syllabus_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center justify-center px-3 py-2 rounded-full border-2 border-black bg-white text-black font-bold text-sm hover:-translate-y-0.5 transition"
                      >
                        Syllabus (PDF)
                      </a>
                    )}
                  </div>
                </div>
              </article>
            );
          })}
        </div>
      </div>
    </section>
  );
}
