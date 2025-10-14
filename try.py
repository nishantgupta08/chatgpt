Event handlers cannot be passed to Client Component props.
  <a href=... onClick={function onClick} className=... aria-label=... children=...>
                      ^^^^^^^^^^^^^^^^^^
If you need interactivity, consider converting part of this to a Client Component.

app\page.tsx (18:7) @ Home


  16 |     <>
  17 |       <SocialBadge />
> 18 |       <HeroSection />
     |       ^
  19 |       {/* <Features /> */}
  20 |       {/* <CounsellingForm /> */}
  21 |       <FellowshipPrograms />
Call Stack
7

stringify
<anonymous>
resolveErrorDev
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_5150ccfd._.js (4265:48)
processFullStringRow
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_5150ccfd._.js (4513:29)
processFullBinaryRow
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_5150ccfd._.js (4472:9)
processBinaryChunk
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_5150ccfd._.js (4581:98)
progress
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_5150ccfd._.js (4747:25)
Home
app\page.tsx (18:7)
