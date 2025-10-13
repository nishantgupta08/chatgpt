"use client";
import React, { useMemo, useState } from "react";
import Image from "next/image";
import data from "@/app/assets/content.json";

type LinkedInMeta = { url?: string | null; urn?: string | null };
type WorkshopItem = {
  college: string;
  city?: string | null;
  date: string;                 // ISO date string
  cover: string;                // /public path
  attendees?: number | null;
  satisfaction?: number | null; // 0–100
  speakers?: string[] | null;
  linkedin?: LinkedInMeta | null;
};

function formatDate(iso: string) {
  const d = new Date(iso);
  return isNaN(d.getTime())
    ? iso
    : d.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
}

export default function WorkshopsGallery() {
  const block = (data as any).workshops ?? {};
  const items: WorkshopItem[] = (block.items ?? []) as WorkshopItem[];

  const [openIdx, setOpenIdx] = useState<number | null>(null);
  const open = (i: number) => setOpenIdx(i);
  const close = () => setOpenIdx(null);

  const stats = useMemo(() => {
    if (!items.length) return { count: 0, avgSat: null, totalAtt: 0 };
    const satVals = items.map(i => i.satisfaction ?? 0);
    const avgSat = Math.round(satVals.reduce((a, b) => a + b, 0) / satVals.length);
    const totalAtt = items.reduce((a, b) => a + (b.attendees ?? 0), 0);
    return { count: items.length, avgSat, totalAtt };
  }, [items]);

  return (
    <section id="workshops" className="bg-[#F7EEFA] py-10 md:py-14">
      <div className="container">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-3">
          <div>
            <h2 className="text-2xl md:text-3xl font-extrabold text-black">
              {block.title ?? "Campus Workshops"}
            </h2>
            <p className="mt-1 text-black/70">
              {block.subtitle ?? "Real sessions. Real feedback from colleges."}
            </p>
          </div>

          {/* Quick stats */}
          {items.length > 0 && (
            <div className="inline-flex flex-wrap items-center gap-2">
              <span className="px-3 py-1.5 rounded-full border-2 border-black bg-white text-sm font-bold">
                {stats.count} workshops
              </span>
              <span className="px-3 py-1.5 rounded-full border-2 border-black bg-white text-sm font-bold">
                {stats.totalAtt.toLocaleString()} attendees
              </span>
              {stats.avgSat !== null && (
                <span className="px-3 py-1.5 rounded-full border-2 border-black bg-white text-sm font-bold">
                  {stats.avgSat}% satisfaction
                </span>
              )}
            </div>
          )}
        </div>

        {/* Grid */}
        <div
          className="mt-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-5"
          role="list"
          aria-label="Workshop gallery"
        >
          {items.map((w, i) => (
            <article
              key={`${w.college}-${w.date}-${i}`}
              role="listitem"
              className="group rounded-2xl overflow-hidden bg-white border border-slate-200 shadow-sm hover:shadow-md transition"
            >
              {/* Cover */}
              <div className="relative aspect-[4/3]">
                <Image
                  src={w.cover}
                  alt={`${w.college} workshop cover`}
                  fill
                  sizes="(min-width: 1024px) 33vw, (min-width: 640px) 50vw, 100vw"
                  className="object-cover"
                  priority={i < 3}
                />
                {/* Hover overlay */}
                <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition bg-gradient-to-t from-black/50 to-black/0" />
                {/* CTA on hover */}
                <button
                  onClick={() => open(i)}
                  className="absolute bottom-3 left-3 opacity-0 group-hover:opacity-100 transition inline-flex items-center gap-2 text-white font-bold text-sm bg-black/70 px-3 py-1.5 rounded-full focus:outline-none focus-visible:ring-2 focus-visible:ring-white"
                  aria-label="Open LinkedIn feedback"
                >
                  View feedback →
                </button>
              </div>

              {/* Body */}
              <div className="p-4">
                <div className="flex items-start gap-3">
                  <div className="min-w-0">
                    <h3 className="text-[15px] font-extrabold leading-snug text-slate-900">
                      {w.college}
                      {w.city ? <span className="text-slate-500 font-semibold"> • {w.city}</span> : null}
                    </h3>
                    <p className="text-xs text-slate-600 mt-0.5">{formatDate(w.date)}</p>

                    {/* Meta row */}
                    <div className="mt-3 flex flex-wrap gap-2 text-xs font-semibold text-slate-700">
                      {typeof w.attendees === "number" && (
                        <span className="px-2 py-1 rounded-full border">{w.attendees} attendees</span>
                      )}
                      {typeof w.satisfaction === "number" && (
                        <span className="px-2 py-1 rounded-full border">{w.satisfaction}% positive</span>
                      )}
                      {w.speakers?.length ? (
                        <span className="px-2 py-1 rounded-full border">
                          Speakers: {w.speakers.slice(0, 2).join(", ")}
                          {w.speakers.length > 2 ? " +" + (w.speakers.length - 2) : ""}
                        </span>
                      ) : null}
                    </div>

                    {/* Actions */}
                    <div className="mt-3 flex items-center gap-2">
                      <button
                        onClick={() => open(i)}
                        className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-black text-white border-2 border-black text-xs font-bold hover:-translate-y-0.5 transition"
                      >
                        View LinkedIn
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                          <path d="M7 17L17 7M17 7H9M17 7V15" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
                        </svg>
                      </button>
                      {w.linkedin?.url && (
                        <a
                          href={w.linkedin.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="inline-flex items-center px-3 py-1.5 rounded-full bg-white text-black border-2 border-black text-xs font-bold hover:-translate-y-0.5 transition"
                        >
                          Open in LinkedIn
                        </a>
                      )}
                    </div>
                  </div>
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>

      {/* Simple modal to show LinkedIn embed or link */}
      {openIdx !== null && items[openIdx] && (
        <LinkedInModal item={items[openIdx]} onClose={close} />
      )}
    </section>
  );
}

/* ---------- Modal (no external deps) ---------- */

function LinkedInModal({ item, onClose }: { item: WorkshopItem; onClose: () => void }) {
  const urn = item.linkedin?.urn ?? null;
  const url = item.linkedin?.url ?? null;
  // Official embed format: https://www.linkedin.com/embed/feed/update/{URN}
  const embedSrc = urn ? `https://www.linkedin.com/embed/feed/update/${encodeURIComponent(urn)}` : null;

  return (
    <div
      className="fixed inset-0 z-50"
      role="dialog"
      aria-modal="true"
      aria-label="LinkedIn feedback"
    >
      <div
        className="absolute inset-0 bg-black/60"
        onClick={onClose}
        aria-hidden="true"
      />
      <div className="absolute inset-0 grid place-items-center p-4">
        <div className="w-full max-w-3xl bg-white rounded-2xl overflow-hidden border-2 border-black shadow-[10px_10px_0_#6B5AED]">
          <div className="flex items-center justify-between px-4 py-3 border-b border-slate-200">
            <h4 className="text-lg font-extrabold">{item.college}{item.city ? ` • ${item.city}` : ""}</h4>
            <button
              onClick={onClose}
              className="inline-flex items-center justify-center size-9 rounded-full border-2 border-black bg-white font-bold hover:-translate-y-0.5 transition"
              aria-label="Close"
            >
              ✕
            </button>
          </div>

          <div className="bg-slate-50">
            {/* Embed if URN available, else fallback card */}
            {embedSrc ? (
              <iframe
                key={embedSrc}
                src={embedSrc}
                height={560}
                className="w-full"
                frameBorder="0"
                allowFullScreen
                title="LinkedIn feedback"
              />
            ) : (
              <div className="p-6 text-center">
                <p className="font-semibold">This workshop’s feedback opens on LinkedIn.</p>
                {url ? (
                  <a
                    href={url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="mt-4 inline-flex items-center px-4 py-2 rounded-full bg-black text-white border-2 border-black font-bold"
                  >
                    Open LinkedIn Post →
                  </a>
                ) : (
                  <p className="mt-2 text-sm text-slate-600">No LinkedIn link provided.</p>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
