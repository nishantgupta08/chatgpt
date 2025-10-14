// app/page.tsx
import type { Metadata } from "next";
import HomeClient from "@/components/HomeClient";

export const metadata: Metadata = {
  title: "Home",
  description: "Welcome to DataPlay – counselling intake and lead capture.",
};

export default function Page() {
  return <HomeClient />;
}
