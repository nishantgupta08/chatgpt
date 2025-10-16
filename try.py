function extractExperts(raw: ContentRoot): Expert[] {
  // Preferred: top-level `experts` array
  if (isWrapped(raw)) {
    const fromTop = (raw as { experts?: unknown }).experts;
    const expertsTop = sanitizeExperts(fromTop);
    if (expertsTop.length > 0) return expertsTop;
  }

  // Fallback 1: top-level `mentors` array
  if (isWrapped(raw)) {
    const mentors = (raw as { mentors?: unknown }).mentors;
    const expertsFromMentors = sanitizeMentors(mentors);
    if (expertsFromMentors.length > 0) return expertsFromMentors;
  }

  // Fallback 2: nested `homepage.mentors.mentors` (as in provided content.json)
  try {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const nested = (raw as any)?.homepage?.mentors?.mentors as unknown;
    const expertsFromHomepage = sanitizeMentors(nested);
    // Prevent duplicate role entries (e.g., designation appearing twice)
    const cleanedExperts = expertsFromHomepage.map((e) => {
      if (e.role) {
        const parts = e.role.split(/,\s*/);
        const unique = Array.from(new Set(parts));
        return { ...e, role: unique.join(", ") };
      }
      return e;
    });
    if (cleanedExperts.length > 0) return cleanedExperts;
  } catch {
    // ignore shape errors and fall through
  }

  return [];
}
