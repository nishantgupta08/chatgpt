// In your page.tsx (where you want the section to appear)
import IndiaLearnersMap from "@/components/IndiaLearnersMap";

{/* …somewhere after “Led by Industry Experts” or before Testimonials */}
<IndiaLearnersMap
  mapSrc="/india-map.svg" // put an India silhouette in /public
  title="Learners Across India"
  subtitle="From Jaipur to Bengaluru — a growing community from top institutes."
/>
