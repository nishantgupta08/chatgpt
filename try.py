/* eslint-disable @next/next/no-img-element */
import React from "react";
import Image from "next/image";
import { Icon } from "@iconify/react";
import data from "@/app/assets/content.json";

/**
 * HeroSection
 * - Background + spacing taken from your reference snippet:
 *   bg-[#F7EEFA], container, grid lg:grid-cols-2 2xl:gap-20 lg:gap-10,
 *   left column py-16 md:py-20, right image wrapper aligned to the edge.
 * - Keeps original "Never Stop Learning" eyebrow.
 * - Google Rating badge sits in the middle gap, slightly lower.
 * - Four feature cards remain below the hero.
 */
const HeroSection = () => {
  const hero = data?.homepage?.hero ?? {};
  const featuresData: string[] = data?.homepage?.features ?? [];

  const featureCards = [
    { icon: "/lifetime.png",      title: featuresData[0] || "Lifetime Access to Live Classes" },
    { icon: "/bytheindustry.png", title: featuresData[1] || "By the Industry For the Industry" },
    { icon: "/resume.png",        title: featuresData[2] || "Resume Refactoring & Mock Interviews" },
    { icon: "/money.png",         title: featuresData[3] || "Affordability meets Quality" },
  ];

  return (
    <section id="home" className="relative bg-[#F7EEFA] overflow-hidden" aria-label="Hero">
      <div className="container">
        {/* grid + gaps from your reference file */}
        <div className="grid lg:grid-cols-2 2xl:gap-20 lg:gap-10 items-end">
          {/* LEFT: copy + CTAs (top spacing from reference) */}
          <div className="relative py-16 md:py-20">
            {/* Eyebrow: original “Never Stop Learning” */}
            <h5 className="text-darkBlue 2xl:text-4xl xl:text-3xl text-2xl font-semibold mb-4">
              Never Stop
              <span className="relative ml-3 inline-flex items-center justify-center text-white font-bold">
                <span className="relative z-[1]">Learning</span>
                <svg
                  className="absolute h-full w-full scale-110"
                  viewBox="0 0 211 56"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  aria-hidden="true"
                >
                  <path
                    d="M210.918 11.866C211.794 5.45292 205.441 4.56218 202.155 4.38404C144.754 -2.88408 47.5176 2.24637 6.62183 6.52173C-1.26521 6.52173 -0.315843 11.6878 0.597016 14.0036L4.9787 45.5344C4.9787 51.5199 9.9081 52.8382 11.5512 53.0163C83.849 59.0018 166.188 53.7289 198.321 50.3442C204.345 50.3442 207.266 47.494 207.084 45.5345C207.084 34.3116 208.727 21.1292 210.918 11.866Z"
                    fill="#8073E5"
                  />
                </svg>
                <img
                  alt="Learning Vector 2"
                  width={53}
                  height={53}
                  decoding="async"
                  src="/learning-vector2.svg"
                  className="absolute -right-12 md:-right-16 -top-12"
                  style={{ color: "transparent" }}
                />
              </span>
            </h5>

            {/* Headline */}
            <h1 className="text-darkBlue 2xl:text-[56px] xl:text-5xl text-4xl font-bold mb-6">
              {hero?.heading ?? "Empowering Careers In DATA and"}
              <span className="relative">
                {hero?.underline_heading ?? " Design"}
                <svg
                  width="227"
                  height="20"
                  className="absolute top-full -right-10"
                  viewBox="0 0 227 20"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  aria-hidden="true"
                >
                  <path
                    d="M-267.413 10.121C-263.4 10.1409 -259.407 10.0217 -255.394 9.95222..."
                    fill="#FF4C3D"
                  />
                </svg>
              </span>
            </h1>

            {/* Subhead */}
            <p className="text-darkBlue 2xl:text-[28px] xl:text-2xl text-xl font-bold mb-6">
              {hero?.sub_heading ?? "Let's Sculpt YOUR Path To Success, YOUR Way !"}
            </p>

            {/* CTAs */}
            <div className="mt-2 flex flex-col sm:flex-row gap-3">
              <a
                href="#contact-us" /* route to contact since inline form was removed */
                className="inline-flex items-center justify-center px-6 py-3 rounded-full font-bold bg-black text-white border-2 border-black shadow-[6px_6px_0_#FF2714] hover:translate-y-[-1px] active:translate-y-[1px] transition-transform focus:outline-none focus-visible:ring-2 focus-visible:ring-black"
                aria-label="Become a Mentor"
              >
                <Icon icon="mdi:rocket-launch-outline" className="mr-2 text-xl" />
                Become a Mentor
              </a>

              <a
                href="#courses"
                className="inline-flex items-center justify-center px-6 py-3 rounded-full font-bold bg-white text-black border-2 border-black hover:translate-y-[-1px] active:translate-y-[1px] transition-transform focus:outline-none focus-visible:ring-2 focus-visible:ring-black"
                aria-label="Explore Courses"
              >
                Explore Courses
                <Icon icon="mdi:arrow-right" className="ml-2 text-xl" />
              </a>
            </div>
          </div>

          {/* RIGHT: image aligned to the edge (spacing from reference) */}
          <div className="relative max-md:-mt-20 max-md:w-[120%] w-full right-0">
            <Image
              src="/hero-img3.png"
              alt="Learner pointing to growth"
              width={1200}
              height={850}
              className="relative block w-full h-auto drop-shadow-xl"
              priority
            />

            {/* Google Rating badge in the inter-column gap, slightly lower */}
            <a
              href="https://www.google.com/search?q=dataplay+reviews"
              target="_blank"
              rel="noopener noreferrer"
              className="absolute left-0 -translate-x-1/2 md:-translate-x-2/3 top-10 md:top-12 z-10 rounded-xl bg-white/95 backdrop-blur border-2 border-black shadow-[6px_6px_0_#6B5AED] px-4 py-2 hover:shadow-[8px_8px_0_#FF2714] transition-shadow focus:outline-none focus-visible:ring-2 focus-visible:ring-black"
              aria-label="Open Google reviews"
              title="Open Google reviews"
            >
              <div className="flex items-center gap-2">
                <span className="inline-flex items-center justify-center size-7 rounded-full border-2 border-black">
                  <svg viewBox="0 0 24 24" className="w-4 h-4" aria-hidden="true">
                    <path
                      fill="currentColor"
                      d="M21.35 11.1H12v2.9h5.38C16.98 16.14 15.09 17.5 12 17.5c-3.59 0-6.5-2.91-6.5-6.5s2.91-6.5 6.5-6.5c1.65 0 3.15.62 4.29 1.63l2.06-2.06C16.76 2.65 14.49 1.75 12 1.75 6.89 1.75 2.75 5.89 2.75 11S6.89 20.25 12 20.25c5.04 0 8.75-3.53 8.75-8.5 0-.52-.06-1.05-.17-1.55z"
                    />
                  </svg>
                </span>
                <span className="text-sm font-extrabold tracking-tight">4.9</span>
                <span className="text-yellow-500 text-sm">★</span>
                <span className="text-sm font-semibold">Google Rating</span>
                <span className="ml-2 text-[11px] text-black/60 underline decoration-dotted">
                  Read reviews
                </span>
              </div>
            </a>
          </div>
        </div>

        {/* Feature cards band */}
        <div className="mt-6 -mx-4 sm:-mx-6 lg:-mx-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-2 md:gap-3">
            {featureCards.map((f, i) => (
              <div key={i} className="px-4 sm:px-6 lg:px-8">
                <div className="rounded-2xl bg-white border-2 border-black p-4 sm:p-5 text-left shadow-[4px_4px_0_#000] hover:shadow-[6px_6px_0_#FF2714] transition-shadow">
                  <div className="flex items-center gap-3">
                    <span className="inline-flex size-11 items-center justify-center rounded-xl border-2 border-black overflow-hidden">
                      <Image src={f.icon} alt={f.title} width={28} height={28} className="w-7 h-7 object-contain" />
                    </span>
                    <h3 className="text-sm sm:text-base font-bold leading-snug text-black">{f.title}</h3>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Background vector from reference (optional) */}
      <Image
        src="/hero-vector1.svg"
        height={345}
        width={120}
        alt="Hero Vector"
        className="hidden sm:block absolute"
        style={{ top: "45%" }}
        loading="lazy"
      />
    </section>
  );
};

export default HeroSection;
