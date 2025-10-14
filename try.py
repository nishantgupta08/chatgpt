/* eslint-disable @next/next/no-img-element */
import React from "react";
import Image from "next/image";
import { Icon } from "@iconify/react";
import data from "@/app/assets/content.json";

type Feature = { icon: string; title: string; href?: string };

const HeroSection = () => {
  const hero = data?.homepage?.hero ?? {};
  const features: Feature[] = [
    { icon: "/lifetime.png", title: (data?.homepage?.features?.[0] ?? "Lifetime Access"), href: "#live-classes" },
    { icon: "/bytheindustry.png", title: (data?.homepage?.features?.[1] ?? "By the Industry For the Industry"), href: "#industry" },
    { icon: "/resume.png", title: (data?.homepage?.features?.[2] ?? "Resume Refactoring & Mock Interviews"), href: "#career" },
    { icon: "/money.png", title: (data?.homepage?.features?.[3] ?? "Affordability meets Quality"), href: "#pricing" },
  ];

  return (
    <section className="relative overflow-hidden bg-[#F8F3FF]">
      <div className="container grid lg:grid-cols-2 gap-6 items-center pt-10 pb-12">
        {/* Copy */}
        <div className="max-w-2xl">
          <p className="uppercase tracking-wide font-extrabold text-[#7c6cff]">
            {hero.kicker ?? "Never Stop"} <span className="bg-[#e9e5ff] px-2 py-1 rounded-md">{hero.kicker_right ?? "Learning"}</span>
          </p>

          <h1 className="text-darkBlue font-extrabold text-4xl sm:text-5xl leading-tight mt-2">
            {hero.heading}
            <span className="relative">
              {hero.underline_heading}
              {/* underline svg ... */}
            </span>
          </h1>

          <p className="text-darkBlue 2xl:text-[28px] xl:text-2xl text-xl font-bold mt-3 mb-5">
            {hero?.sub_heading ?? "Let's Sculpt YOUR Path To Success, YOUR Way !"}
          </p>

          {/* CTAs */}
          <div className="flex flex-col sm:flex-row gap-3">
            <a
              href="#contact-us"
              className="inline-flex items-center justify-center gap-2 rounded-xl bg-black text-white px-6 py-3 font-bold hover:bg-darkBlue focus:outline-none focus-visible:ring-2 focus-visible:ring-black"
              aria-label="Book 1:1 Counselling Session"
            >
              <Icon icon="mdi:rocket-launch-outline" className="mr-2 text-xl" />
              Book 1:1 Counselling Session
            </a>

            <a
              href="#courses"
              className="inline-flex items-center justify-center gap-2 rounded-xl border border-black px-6 py-3 font-bold hover:bg-black hover:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-black"
              aria-label="Explore Courses"
            >
              <Icon icon="mdi:school-outline" className="mr-2 text-xl" />
              Explore Courses
            </a>
          </div>

          {/* Feature chips */}
          <div className="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3">
            {features.map((f, i) => (
              <a key={i} href={f.href} className="flex items-center gap-2 bg-white rounded-xl px-3 py-2 shadow hover:shadow-md transition">
                <img src={f.icon} alt="" className="h-6 w-6" />
                <span className="text-sm font-semibold">{f.title}</span>
              </a>
            ))}
          </div>
        </div>

        {/* Art */}
        <div className="relative">
          <Image src="/hero-person.png" alt="Student with laptop" width={640} height={520} className="w-full h-auto" />
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
