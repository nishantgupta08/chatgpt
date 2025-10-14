"use client";

import { useEffect, useState } from "react";
import Modal from "./Modal";
import CounsellingForm from "./CounsellingForm";

export default function HomeClient() {
  const [open, setOpen] = useState(false);

  // Lock scroll when modal is open
  useEffect(() => {
    if (open) document.body.classList.add("overflow-hidden");
    else document.body.classList.remove("overflow-hidden");
    return () => document.body.classList.remove("overflow-hidden");
  }, [open]);

  // Listen for clicks on any external trigger: [data-counselling-open]
  useEffect(() => {
    const handler = (e: Event) => {
      const target = e.target as HTMLElement | null;
      if (!target) return;
      // Walk up the tree in case the click is on a child of the button
      let el: HTMLElement | null = target;
      while (el && el !== document.body) {
        if (el.hasAttribute("data-counselling-open")) {
          e.preventDefault();
          setOpen(true);
          break;
        }
        el = el.parentElement;
      }
    };

    document.addEventListener("click", handler);
    return () => document.removeEventListener("click", handler);
  }, []);

  return (
    <main>
      {/* Your normal landing content stays as-is in your other components/pages */}

      {/* Modal lives here, opened by any [data-counselling-open] trigger */}
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
"use client";

import { useEffect, useState } from "react";
import Modal from "./Modal";
import CounsellingForm from "./CounsellingForm";

export default function HomeClient() {
  const [open, setOpen] = useState(false);

  // Lock scroll when modal is open
  useEffect(() => {
    if (open) document.body.classList.add("overflow-hidden");
    else document.body.classList.remove("overflow-hidden");
    return () => document.body.classList.remove("overflow-hidden");
  }, [open]);

  // Listen for clicks on any external trigger: [data-counselling-open]
  useEffect(() => {
    const handler = (e: Event) => {
      const target = e.target as HTMLElement | null;
      if (!target) return;
      // Walk up the tree in case the click is on a child of the button
      let el: HTMLElement | null = target;
      while (el && el !== document.body) {
        if (el.hasAttribute("data-counselling-open")) {
          e.preventDefault();
          setOpen(true);
          break;
        }
        el = el.parentElement;
      }
    };

    document.addEventListener("click", handler);
    return () => document.removeEventListener("click", handler);
  }, []);

  return (
    <main>
      {/* Your normal landing content stays as-is in your other components/pages */}

      {/* Modal lives here, opened by any [data-counselling-open] trigger */}
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
