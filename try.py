// app/page.tsx
"use client";

import { useEffect, useState } from "react";

// Example imports — keep your actual paths/aliases
import SocialBadge from "@/components/SocialBadge";
import HeroSection from "@/components/HeroSection";
import CounsellingForm from "@/components/CounsellingForm";
import FellowshipPrograms from "@/components/FellowshipPrograms";
import CourseSectionPro from "@/components/CourseSectionPro";
import Mentors from "@/components/Mentors";
import Testimonials from "@/components/Testimonials";
import WhoCanApply from "@/components/WhoCanApply";
import WorkshopGallery from "@/components/WorkshopGallery";

function Modal({
  open,
  onClose,
  children,
}: {
  open: boolean;
  onClose: () => void;
  children: React.ReactNode;
}) {
  // Do not render if closed
  if (!open) return null;

  return (
    <div
      aria-modal="true"
      role="dialog"
      aria-labelledby="counselling-title"
      className="fixed inset-0 z-50 flex items-center justify-center p-4"
      onKeyDown={(e) => {
        if (e.key === "Escape") onClose();
      }}
    >
      {/* Backdrop with blur */}
      <div
        className="absolute inset-0 bg-black/40 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Modal panel */}
      <div
        className="relative z-10 w-full max-w-2xl rounded-2xl bg-white p-6 shadow-xl outline-none"
        role="document"
      >
        <button
          onClick={onClose}
          className="absolute right-3 top-3 rounded-full px-3 py-1 text-sm font-medium text-gray-600 hover:bg-gray-100"
          aria-label="Close"
          type="button"
        >
          ✕
        </button>

        <h2 id="counselling-title" className="sr-only">
          Book a Counselling Session
        </h2>

        {children}
      </div>
    </div>
  );
}

export default function Home() {
  const [open, setOpen] = useState(false);

  // Lock body scroll when modal is open
  useEffect(() => {
    if (open) document.body.classList.add("overflow-hidden");
    else document.body.classList.remove("overflow-hidden");
    return () => document.body.classList.remove("overflow-hidden");
  }, [open]);

  // Close on ESC globally (helpful if focus is outside modal)
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setOpen(false);
    };
    if (open) window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open]);

  return (
    <>
      {/* Top content */}
      <SocialBadge />
      <HeroSection />

      {/* Single CTA to open the modal */}
      <div className="flex items-center justify-center py-8">
        <button
          type="button"
          onClick={() => setOpen(true)}
          className="rounded-xl px-6 py-3 text-lg border border-gray-300 shadow-sm hover:bg-gray-50 transition"
          aria-haspopup="dialog"
          aria-controls="counselling-modal"
        >
          Book Counselling
        </button>
      </div>

      {/* Rest of the page */}
      <FellowshipPrograms />
      <CourseSectionPro />
      <Mentors />
      <Testimonials />
      <WhoCanApply />
      <WorkshopGallery />

      {/* Modal with blurred background */}
      <Modal open={open} onClose={() => setOpen(false)}>
        {/* If your CounsellingForm supports onSuccess, uncomment the next line and remove the one after it */}
        {/* <CounsellingForm onSuccess={() => setOpen(false)} /> */}
        <CounsellingForm />
      </Modal>
    </>
  );
}
