// app/page.tsx
import type { Metadata } from 'next';
import HomeClient from '@/components/HomeClient';

export const metadata: Metadata = {
  title: 'Home',
};

export default function Page() {
  // Server component; no "use client" here
  return <HomeClient />;
}
