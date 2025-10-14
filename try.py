/* eslint-disable @next/next/no-img-element */
'use client';

import React from "react";
import Image from "next/image";
import { Icon } from "@iconify/react";
import data from "@/app/assets/content.json";

type Feature = { icon: string; title: string; href?: string };

const HeroSection: React.FC = () => {
  const hero = data?.homepage?.hero ?? {};

  const features: Feature[] = [
    {
      icon: "/lifetime.png",
      title: data?.homepage?.features?.[0] ?? "Lifetime Access",
      href: "#live-classes",
    },
    {
      icon: "/bytheindustry.png",
      title: data?.homepage?.features?.[1] ?? "By the Industry For the Industry",
      href: "#industry",
    },
    {
      icon: "/resume.png",
      title: data?.homepage?.features?.[2] ?? "Resume Refactoring & Mock Interviews",
      href: "#career",
    },
    {
      icon: "/money.png",
      title: data?.homepage?.features?.[3] ?? "Affordability meets Quality",
      href: "#pricing",
    },
  ];

  const openModal = (e: React.MouseEvent) => {
    e.preventDefault();
    // Trigger the global modal you mounted in app/layout.tsx
    window.dispatchEvent(new CustomEvent("openCounsellingModal"));
  };

  return (
    <section id="home" className="relative overflow-hidden bg-[#F8F3FF]">
      <div className="container grid lg:grid-cols-2 gap-8 items-center pt-10 pb-12">
        {/* Left: Copy */}
        <div className="max-w-2xl">
          {/* Kicker */}
          <p className="uppercase tracking-wide font-extrabold text-[#7c6cff]">
            {hero.kicker ?? "Never Stop"}{" "}
            <span className="bg-[#e9e5ff] px-2 py-1 rounded-md">
              {hero.kicker_right ?? "Learning"}
            </span>
          </p>

          {/* Headline */}
          <h1 className="text-darkBlue font-extrabold text-4xl sm:text-5xl leading-tight mt-3">
            {hero.heading ?? "Build Real Skills. Get Real Outcomes."}
            <span className="relative block">
              {hero.underline_heading ?? "From Basics to Breakthroughs"}
              {/* underline */}
              <svg
                aria-hidden="true"
                width="227"
                height="20"
                className="absolute top-full -right-10"
                viewBox="0 0 227 20"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M-267.413 10.121C-263.4 10.1409 -259.407 10.1807 -255.413 10.2006C-144.49 10.7469 -33.566 11.2832 77.3572 11.8294C92.3877 11.9041 107.418 11.9887 122.448 12.0634C139.943 12.1518 157.427 12.2401 174.922 12.3284C183.727 12.3731 192.543 12.4177 201.348 12.4623C207.944 12.4961 214.539 12.54 221.135 12.5738C221.984 12.5781 223.466 12.064 223.423 11.3465C223.381 10.6714 222.109 10.1351 221.239 10.1307C214.654 10.097 208.06 10.0531 201.475 10.0194C192.648 9.97474 183.832 9.93013 175.005 9.88552C157.5 9.7972 140.006 9.70888 122.5 9.62056C107.47 9.54587 92.4398 9.46133 77.4094 9.38664C-33.5139 8.8404 -144.438 8.3041 -255.361 7.75784C-259.344 7.738 -263.337 7.6982 -267.32 7.67836C-268.201 7.674  -269.462 8.2103 -269.504 8.8854C-269.547 9.603 -268.054 10.1169 -267.413 10.121Z"
                  fill="#FF4C3D"
                />
              </svg>
            </span>
          </h1>

          {/* Subhead */}
          <p className="text-darkBlue 2xl:text-[28px] xl:text-2xl text-xl font-bold mt-4 mb-6">
            {hero?.sub_heading ?? "Let’s sculpt YOUR path to success — YOUR way!"}
          </p>

          {/* CTAs */}
          <div className="flex flex-col sm:flex-row gap-3">
            {/* Primary: opens modal */}
            <a
              href="#contact-us"
              onClick={openModal}
              className="inline-flex items-center justify-center gap-2 rounded-xl bg-black text-white px-6 py-3 font-bold hover:bg-darkBlue focus:outline-none focus-visible:ring-2 focus-visible:ring-black"
              aria-label="Book 1:1 Counselling Session"
            >
              <Icon icon="mdi:rocket-launch-outline" className="mr-2 text-xl" />
              Book 1:1 Counselling Session
            </a>

            {/* Secondary */}
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
              <a
                key={i}
                href={f.href}
                className="flex items-center gap-2 bg-white rounded-xl px-3 py-2 shadow hover:shadow-md transition"
              >
                <img src={f.icon} alt="" className="h-6 w-6" />
                <span className="text-sm font-semibold">{f.title}</span>
              </a>
            ))}
          </div>
        </div>

        {/* Right: Art */}
        <div className="relative">
          <Image
            src="/hero-person.png"
            alt="Learner studying with laptop"
            width={640}
            height={520}
            className="w-full h-auto"
            priority
          />
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
