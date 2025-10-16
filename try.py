 ⨯ ./app/landing/page.tsx:230:20
Parsing ecmascript source code failed
  228 |
  229 |   return [];
> 230 | }(raw: ContentRoot): Expert[] {
      |                    ^
  231 |   // Preferred: top-level `experts` array
  232 |   if (isWrapped(raw)) {
  233 |     const fromTop = (raw as { experts?: unknown }).experts;

Expected '=>', got ':'
