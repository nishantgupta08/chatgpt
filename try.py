"use client";

import { useEffect, useState } from "react";
import Modal from "./Modal";
import CounsellingForm from "./CounsellingForm";

export default function HomeClient() {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    if (open) document.body.classList.add("overflow-hidden");
    else document.body.classList.remove("overflow-hidden");
    return () => document.body.classList.remove("overflow-hidden");
  }, [open]);

  return (
    <main>
      <section className="relative isolate" aria-labelledby="hero-title">
        <div className="mx-auto max-w-5xl px-6 py-16">
          <header className="space-y-3 text-center">
            <h1 id="hero-title" className="text-4xl font-semibold tracking-tight">
              DataPlay
            </h1>
            <p className="text-gray-600 max-w-2xl mx-auto">
              A simple way to capture counselling leads and preferences.
            </p>
          </header>

          <div className="mt-10 grid grid-cols-1 md:grid-cols-3 gap-6">
            <Card title="Track Leads" desc="Collect essential contact details quickly." />
            <Card title="Qualify Fast" desc="Lightweight questions to route the right way." />
            <Card title="Follow Up" desc="Export or integrate into your CRM flow." />
          </div>

          <div className="mt-12 flex items-center justify-center">
            <button
              type="button"
              onClick={() => setOpen(true)}
              className="rounded-xl px-5 py-2.5 border border-gray-300 shadow-sm hover:bg-gray-50"
              aria-haspopup="dialog"
              aria-expanded={open}
              aria-controls="counselling-modal"
            >
              Book Counselling
            </button>
          </div>
        </div>
      </section>

      <Modal
        id="counselling-modal"
        title="Book a Counselling Session"
        open={open}
        onClose={() => setOpen(false)}
      >
        <CounsellingForm onSuccess={() => setOpen(false)} />
      </Modal>
    </main>
  );
}

function Card({ title, desc }: { title: string; desc: string }) {
  return (
    <div className="rounded-2xl border border-gray-200 p-6 shadow-sm">
      <h3 className="text-lg font-semibold">{title}</h3>
      <p className="mt-1 text-gray-600">{desc}</p>
    </div>
  );
}
