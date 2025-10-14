./app/page.tsx (21:14)

Ecmascript file had an error
  19 | import HomeClient from '@/components/HomeClient';
  20 |
> 21 | export const metadata: Metadata = {
     |              ^^^^^^^^
  22 |   title: 'Home',
  23 | };
  24 |

You are attempting to export "metadata" from a component marked with "use client", which is disallowed. Either remove the export, or the "use client" directive. Read more: https://nextjs.org/docs/app/api-reference/directives/use-client

Import traces:
  Client Component Browser:
    ./app/page.tsx [Client Component Browser]
    ./app/page.tsx [Server Component]

  Client Component SSR:
    ./app/page.tsx [Client Component SSR]
    ./app/page.tsx [Server Component]
