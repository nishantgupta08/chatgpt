import type { Metadata } from "next";
import HomeClient from "../components/HomeClient";

export const metadata: Metadata = {
  title: "Home",
  description: "Book counselling sessions easily with DataPlay.",
};

export default function Page() {
  return <HomeClient />;
}
