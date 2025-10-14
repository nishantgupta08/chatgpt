// components/courses/CoursesSectionPro.tsx
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
  duration_weeks?: number;
  hours_per_week?: number;
  level?: string;
  next_cohort_date?: string;
  seats_left?: number;
  badges?: string[];
  syllabus_url?: string;
  features?: string[];
};

function monthsFromWeeks(w?: number){ if(!w||w<=0) return null; return Math.max(1, Math.round(w/4.3)); }
function fmtDate(iso?: string){ if(!iso) return null; const d=new Date(iso); return isNaN(d.getTime())?null:d.toLocaleDateString("en-IN",{year:"numeric",month:"short",day:"numeric"}); }

const palette: Record<string,string> = {
  "DATA ANALYST":"bg-amber-100 text-amber-900 border-amber-300",
  "DATA ENGINEERING":"bg-sky-100 text-sky-900 border-sky-300",
  "WEB DEVELOPMENT":"bg-violet-100 text-violet-900 border-violet-300",
};

export default function CoursesSectionPro() {
  const homeBlock = (data as any)?.homepage?.courses;
  const homeCourses: Course[] = homeBlock?.courses ?? [];
  const fullCourses: Course[] = (data as any)?.courses ?? [];

  // index top-level by id (string)
  const fullById = new Map(fullCourses.map(c => [String(c.id), c]));

  // Prefer homepage cards; merge in extra fields from top-level
  const merged: Course[] = (homeCourses.length ? homeCourses : fullCourses).map(card => {
    const meta = fullById.get(String(card.id)) || {};
    // card fields win; fall back to meta if missing
    return { ...meta, ...card,
      duration_weeks: card.duration_weeks ?? meta.duration_weeks,
      hours_per_week: card.hours_per_week ?? meta.hours_per_week,
      next_cohort_date: card.next_cohort_date ?? meta.next_cohort_date,
      level: card.level ?? meta.level,
      seats_left: card.seats_left ?? meta.seats_left,
      cover_url: card.cover_url ?? meta.cover_url ?? card.img_url ?? meta.img_url
    };
  });

  return (
    <section id="courses" className="bg-white py-10 md:py-16" aria-label="Courses">
      <div className="container">
        <header className="mb-6 md:mb-8">
          <h2 className="text-2xl md:text-3xl font-extrabold tracking-tight text-slate-900">
            {homeBlock?.title ?? "Courses"}
          </h2>
          <p className="mt-1 text-slate-600">
            {homeBlock?.sub_title ?? "Learn with production-grade projects and expert mentorship."}
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 md:gap-6">
          {merged.map((c) => {
            const tag = (c.highlighted_title || "").toUpperCase().trim();
            const cover = c.cover_url || c.img_url || "/images/courses/placeholder.jpg";
            const tagStyle = palette[tag] ?? "bg-slate-100 text-slate-900 border-slate-300";

            const months = monthsFromWeeks(c.duration_weeks);
            const cohort = fmtDate(c.next_cohort_date);

            return (
              <article key={c.id} className="group rounded-2xl border border-slate-200 overflow-hidden bg-white shadow-sm hover:shadow-md transition">
                <div className="relative aspect-[16/9]">
                  <Image src={cover} alt={`${c.title} course cover`} fill sizes="(min-width:1280px)33vw,(min-width:768px)50vw,100vw" className="object-cover transition-transform duration-300 group-hover:scale-[1.02]" priority />
                  {tag && <span className={`absolute left-3 top-3 inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-extrabold border ${tagStyle}`}>{tag}</span>}
                </div>

                <div className="p-4 md:p-5">
                  <h3 className="text-lg md:text-xl font-extrabold text-slate-900">{c.title}</h3>

                  <div className="mt-2 flex flex-wrap items-center gap-3 text-[12px] font-semibold text-slate-600">
                    {months && (<span className="inline-flex items-center gap-1"><i className="icon-[mdi--calendar-month-outline]" />~{months} {months>1?"months":"month"}</span>)}
                    {typeof c.duration_weeks==="number" && c.duration_weeks>0 && (<span className="inline-flex items-center gap-1"><i className="icon-[mdi--calendar-outline]" />{c.duration_weeks} weeks</span>)}
                    {typeof c.hours_per_week==="number" && c.hours_per_week>0 && (<span className="inline-flex items-center gap-1"><i className="icon-[mdi--clock-outline]" />{c.hours_per_week} hrs/week</span>)}
                    {c.level && (<span className="inline-flex items-center gap-1"><i className="icon-[mdi--signal-cellular-2]" />{c.level}</span>)}
                  </div>

                  {cohort && (
                    <div className="mt-2 inline-flex items-center gap-2 text-[12px] font-bold px-2 py-1 rounded-full bg-slate-50 border border-slate-200 text-slate-700">
                      <i className="icon-[mdi--calendar-start]" />
                      Next cohort: {cohort}
                    </div>
                  )}

                  {c.features?.length ? (
                    <ul className="mt-3 space-y-1.5">
                      {c.features.slice(0,3).map((f,idx)=>(
                        <li key={idx} className="flex items-start gap-2 text-[13px] text-slate-700">
                          <span className="mt-[2px] size-[6px] rounded-full bg-slate-900 shrink-0" />
                          <span>{f}</span>
                        </li>
                      ))}
                    </ul>
                  ):null}

                  <div className="mt-4 flex flex-wrap items-center gap-3">
                    <a href={`/courses/${encodeURIComponent(String(c.id))}`} className="inline-flex items-center justify-center px-4 py-2 rounded-full border-2 border-black bg-black text-white font-bold text-sm hover:-translate-y-0.5 transition">View Course</a>
                    {c.syllabus_url && (
                      <a href={c.syllabus_url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center justify-center px-3 py-2 rounded-full border-2 border-black bg-white text-black font-bold text-sm hover:-translate-y-0.5 transition">Syllabus (PDF)</a>
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
