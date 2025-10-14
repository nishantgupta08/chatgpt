Ecmascript file had an error

./app/page.tsx (18:14)

Ecmascript file had an error
  16 |
  17 | // If you have metadata, make sure it's a *named* export:
> 18 | export const metadata = {
     |              ^^^^^^^^
  19 |   title: 'Home',
  20 | };
  21 |

You are attempting to export "metadata" from a component marked with "use client", which is disallowed. Either remove the export, or the "use client" directive. Read more: https://nextjs.org/docs/app/api-reference/directives/use-client

Import traces:
  Client Component Browser:
    ./app/page.tsx [Client Component Browser]
    ./app/page.tsx [Server Component]

  Client Component SSR:
    ./app/page.tsx [Client Component SSR]
    ./app/page.tsx [Server Component]
