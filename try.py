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

  // Fallback 2: nested `homepage.mentors.mentors`
  try {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const nested = (raw as any)?.homepage?.mentors?.mentors as unknown;
    const expertsFromHomepage = sanitizeMentors(nested);
    if (expertsFromHomepage.length > 0) return expertsFromHomepage;
  } catch {
    // ignore shape errors and fall through
  }

  return [];
}
