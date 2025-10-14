import CounsellingForm from "@/components/counelling_form";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen antialiased">
        {children}
        <CounsellingForm /> {/* mounted globally so any page can open it */}
      </body>
    </html>
  );
}
