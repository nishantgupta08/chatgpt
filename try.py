function extractExperts(raw: ContentRoot): Expert[] {
  
  // Fallback 2: nested `homepage.mentors.mentors` (as in provided content.json)
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

(raw: ContentRoot): Expert[] {

  {
    const mentors = (raw as { mentors?: unknown }).mentors;
    const expertsFromMentors = sanitizeMentors(mentors);
    if (expertsFromMentors.length > 0) return expertsFromMentors;
  }

  return [];
}.experts;
    const expertsTop = sanitizeExperts(fromTop);
    if (expertsTop.length > 0) return expertsTop;
  }
  // If not present at the top level, try to derive none (fallback handled at callsite)
  return [];
}
