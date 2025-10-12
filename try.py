"use client"
/* eslint-disable @next/next/no-img-element */

import React, { useState } from "react";
import { useParams } from "next/navigation";
import { Icon } from "@iconify/react";

import data from "@/app/assets/content.json";
import InnerBanner from "@/components/InnerBanner";
import SocialBadge from "@/components/SocialBadge";

/* -------------------------------------------------------------------------- */
/*                                   Types                                    */
/* -------------------------------------------------------------------------- */

type Submodule = { title: string; content: string[] };

type Topic = {
  title: string;
  content?: string[];       // legacy flat list
  submodules?: Submodule[]; // optional nested
};

type UserCardData = {
  img_url: string;
  name: string;
  linkdin_url: string;
  designation_name: string;
  company_name: string;
  company_business_link: string;
  details: string;
};

type Course = {
  id: number;
  title: string;
  sub_title: string;
  img_url: string;
  right_side_video_url?: string;
  courses_content: Topic[];
  user_section?: UserCardData[];
};

/* -------------------------------------------------------------------------- */
/*                            Highlights (new section)                         */
/* -------------------------------------------------------------------------- */

type Highlight = {
  title: string;
  description: string;
  icon: string; // iconify name
};

const HIGHLIGHTS: Highlight[] = [
  {
    title: "Pay After Placement",
    description: "Zero upfront risk. Start paying only after you land a qualifying role.",
    icon: "mdi:handshake",
  },
  {
    title: "Industry-Expert Led Sessions",
    description: "Live classes taught by senior practitioners who ship in production.",
    icon: "mdi:certificate",
  },
  {
    title: "Lifetime Access to Live Classes",
    description: "Rejoin future cohorts, revisit recordings, and stay current forever.",
    icon: "mdi:infinity",
  },
  {
    title: "Dedicated Career Mentorship",
    description: "1:1 guidance, mock interviews, and resume refactors tailored to you.",
    icon: "mdi:account-check",
  },
];

const HighlightCard = ({ item }: { item: Highlight }) => (
  <article className="group relative overflow-hidden rounded-2xl border border-[#E7E9FF] bg-white shadow-[0_8px_24px_rgba(28,26,74,0.06)] hover:shadow-[0_16px_36px_rgba(28,26,74,0.12)] transition-shadow p-4 sm:p-5">
    <div className="flex items-start gap-3">
      <span className="inline-flex items-center justify-center rounded-xl bg-[#EEF2FF] border border-[#E7E9FF] p-2 shrink-0">
        <Icon icon={item.icon} className="w-5 h-5 text-[#1C1A4A]" aria-hidden />
      </span>
      <div>
        <h3 className="text-base sm:text-lg font-semibold text-[#1C1A4A] leading-tight">
          {item.title}
        </h3>
        <p className="mt-1 text-sm text-gray-700 leading-relaxed">{item.description}</p>
      </div>
    </div>
    <div className="pointer-events-none absolute -right-12 -top-12 h-28 w-28 rounded-full bg-gradient-to-br from-[#D8DCFF] to-transparent opacity-60 group-hover:opacity-90 transition-opacity" />
  </article>
);

const HighlightsSection = () => (
  <section aria-label="Course highlights" className="relative py-8 lg:py-10">
    <div className="absolute inset-0 -z-10 bg-[radial-gradient(60%_80%_at_50%_0%,#EEF2FF_0%,transparent_60%)]" />
    <div className="container px-4 sm:px-6 lg:px-8">
      <div className="text-center mb-6 sm:mb-8">
        <h2 className="text-2xl sm:text-3xl font-bold tracking-tight text-[#111827]">
          Why Choose DataPlay?
        </h2>
        <p className="mt-2 text-sm sm:text-base text-gray-600">
          Built to help you crack interviews and perform on the job.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4 sm:gap-6">
        {HIGHLIGHTS.map((h, i) => (
          <HighlightCard key={`${h.title}-${i}`} item={h} />
        ))}
      </div>
    </div>
  </section>
);

/* -------------------------------------------------------------------------- */
/*                     Course Content as Cards (with submodules)              */
/* -------------------------------------------------------------------------- */

const CountBadge = ({ count }: { count: number }) => (
  <span
    aria-label={`${count} items`}
    className="inline-flex items-center justify-center text-[11px] font-semibold rounded-full px-2 py-1 bg-[#EAEAFF] text-[#1C1A4A] border border-[#DCDDFE]"
  >
    {count}
  </span>
);

const Bullets = ({ bullets }: { bullets: string[] }) =>
  bullets?.length ? (
    <ul className="list-disc pl-5 space-y-1.5 text-sm leading-relaxed text-[#111827]">
      {bullets.map((p, i) => (
        <li key={i} className="marker:text-[#6C72FF]">
          {p}
        </li>
      ))}
    </ul>
  ) : (
    <p className="text-sm text-gray-600">No subtopics yet.</p>
  );

const SubmoduleCard = ({ module, maxItems = 8 }: { module: Submodule; maxItems?: number }) => {
  const [expanded, setExpanded] = useState(false);
  const shown = expanded ? module.content : module.content.slice(0, maxItems);
  const canExpand = module.content.length > maxItems;

  return (
    <div className="bg-[#F8F9FF] rounded-xl border border-[#E7E9FF] p-3 sm:p-4">
      <h4 className="text-sm sm:text-base font-semibold text-[#1C1A4A] mb-2">{module.title}</h4>
      <Bullets bullets={shown} />
      {canExpand && (
        <button
          type="button"
          className="mt-2 text-xs font-medium text-[#4F46E5] hover:underline"
          onClick={() => setExpanded((v) => !v)}
        >
          {expanded ? "Show less" : `Show ${module.content.length - shown.length} more`}
        </button>
      )}
    </div>
  );
};

const CourseContentCards = ({
  topics,
  maxItems = 8,
  showCounts = true,
}: {
  topics: Topic[];
  maxItems?: number;
  showCounts?: boolean;
}) => {
  if (!topics?.length) return null;

  return (
    <section aria-label="Course Content" className="relative">
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 sm:gap-6">
        {topics.map((t, i) => {
          const isNested = !!t.submodules?.length;
          const totalCount = isNested
            ? t.submodules!.reduce((acc, m) => acc + (m.content?.length ?? 0), 0)
            : (t.content?.length ?? 0);

          return (
            <article
              key={`${t.title}-${i}`}
              className="relative rounded-2xl border border-[#E7E9FF] bg-white shadow-[0_8px_24px_rgba(28,26,74,0.06)] hover:shadow-[0_16px_36px_rgba(28,26,74,0.12)] transition-shadow p-4 sm:p-5"
            >
              <header className="flex items-start justify-between gap-3 mb-3">
                <h3 className="text-lg font-semibold text-[#1C1A4A] leading-tight">{t.title}</h3>
                {showCounts && <CountBadge count={totalCount} />}
              </header>

              {isNested ? (
                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                  {t.submodules!.map((m, idx) => (
                    <SubmoduleCard key={`${m.title}-${idx}`} module={m} maxItems={maxItems} />
                  ))}
                </div>
              ) : (
                <Bullets bullets={(t.content ?? []).slice(0, maxItems)} />
              )}

              <div className="pointer-events-none absolute -right-12 -top-12 h-28 w-28 rounded-full bg-gradient-to-br from-[#D8DCFF] to-transparent opacity-60" />
            </article>
          );
        })}
      </div>
    </section>
  );
};

/* -------------------------------------------------------------------------- */
/*                                User Card                                   */
/* -------------------------------------------------------------------------- */

const UserCard = ({ userData }: { userData: UserCardData }) => (
  <div className="w-[320px] sm:w-[360px] lg:w-[400px] flex flex-col gap-2 bg-white rounded-2xl sm:rounded-3xl lg:rounded-4xl p-4 sm:p-6 text-center shadow-[0px_0px_20px_0px_#00000020] sm:shadow-[0px_0px_30px_0px_#00000025] lg:shadow-[0px_0px_40px_0px_#00000033]">
    <img
      src={userData.img_url}
      alt={`${userData.name} testimonial`}
      className="w-16 h-16 sm:w-20 sm:h-20 rounded-full mx-auto border-2 sm:border-4 border-white"
    />
    <h3 className="flex items-center justify-center gap-2 text-lg sm:text-xl font-bold text-black mt-2">
      <span>{userData.name}</span>
      {userData.linkdin_url && (
        <a href={userData.linkdin_url} target="_blank" rel="noopener noreferrer" aria-label="LinkedIn profile">
          <Icon icon="skill-icons:linkedin" className="size-4" />
        </a>
      )}
    </h3>
    <p className="text-sm sm:text-base font-semibold text-black">{userData.designation_name}</p>
    <a href={userData.company_business_link} target="_blank" rel="noopener noreferrer">
      <p className="text-sm sm:text-base font-semibold text-black">{userData.company_name}</p>
    </a>
    <p className="text-black text-sm sm:text-base mt-2 leading-relaxed">{userData.details}</p>
  </div>
);

/* -------------------------------------------------------------------------- */
/*                                   Page                                     */
/* -------------------------------------------------------------------------- */

export default function Page() {
  const params = useParams<{ id: string }>();
  const course_id = params?.id;
  const coursesData = (data.courses as Course[]).find((c) => c.id === Number(course_id));

  return (
    <>
      <SocialBadge />

      <InnerBanner
        img_url={(coursesData?.img_url as string) ?? ""}
        data={
          coursesData
            ? {
                id: coursesData.id.toString(),
                title: coursesData.title,
                sub_title: coursesData.sub_title,
                img_url: coursesData.img_url,
                right_side_video_url: coursesData.right_side_video_url || "",
              }
            : {}
        }
      />

      {/* NEW: Highlights under the banner */}
      <HighlightsSection />

      <div className="relative py-12 lg:py-16">
        <div className="container px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 items-start gap-6 lg:gap-8">
            {/* Course Content (Cards) */}
            <div className="lg:col-span-7">
              <div className="relative rounded-xl p-4 sm:p-6 border border-bor">
                <h2 className="text-2xl sm:text-3xl lg:text-4xl text-black mb-4 sm:mb-6">
                  Course Content
                </h2>

                <CourseContentCards
                  topics={coursesData?.courses_content ?? []}
                  maxItems={8}
                  showCounts
                />
              </div>
            </div>

            {/* Video Section */}
            <div className="lg:col-span-5">
              <div className="relative aspect-video lg:h-[400px] w-full">
                {coursesData?.right_side_video_url && (
                  <iframe
                    className="w-full h-full rounded-xl sm:rounded-2xl lg:rounded-3xl border border-black drop-shadow-[2px_2px_0_#1C1A4A] sm:drop-shadow-[4px_4px_0_#1C1A4A] lg:drop-shadow-[6px_6px_0_#1C1A4A]"
                    src={coursesData?.right_side_video_url}
                    title={`About ${coursesData?.title ?? "DataPlay"}`}
                    frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                  />
                )}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Student / User section (unchanged) */}
      {coursesData?.user_section?.length ? (
        <div className="relative py-12 lg:py-16">
          <div className="container">
            {coursesData.user_section.length > 1 ? (
              <div className="relative w-screen flex items-center gap-10 overflow-auto scroll-hidden">
                {coursesData.user_section.map((userData, index) => (
                  <UserCard key={index} userData={userData} />
                ))}
              </div>
            ) : (
              <div className="flex justify-center">
                <UserCard userData={coursesData.user_section[0]} />
              </div>
            )}
          </div>
        </div>
      ) : null}
    </>
  );
}
