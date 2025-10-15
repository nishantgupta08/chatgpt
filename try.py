A props object containing a "key" prop is being spread into JSX:
  let props = {key: someKey, role: ..., className: ..., href: ..., children: ...};
  <a {...props} />
React keys must be passed directly to JSX without using spread:
  let props = {role: ..., className: ..., href: ..., children: ...};
  <a key={someKey} {...props} />

Call Stack
21

createConsoleError
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_b0daae9a._.js (1605:71)
handleConsoleError
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_b0daae9a._.js (2203:54)
console.error
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_b0daae9a._.js (2354:57)
jsxDEVImpl
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_9337b2a9._.js (172:147)
exports.jsxDEV
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_9337b2a9._.js (203:16)
<unknown>
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/_298c9d48._.js (503:247)
Array.map
<anonymous>
HeroSection
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/_298c9d48._.js (450:44)
Object.react_stack_bottom_frame
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_react-dom_1e674e59._.js (13072:24)
renderWithHooks
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_react-dom_1e674e59._.js (4091:24)
updateFunctionComponent
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_react-dom_1e674e59._.js (5523:21)
beginWork
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_react-dom_1e674e59._.js (6111:24)
runWithFiberInDEV
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_react-dom_1e674e59._.js (886:74)
performUnitOfWork
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_react-dom_1e674e59._.js (8298:97)
workLoopConcurrentByScheduler
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_react-dom_1e674e59._.js (8294:58)
renderRootConcurrent
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_react-dom_1e674e59._.js (8276:71)
performWorkOnRoot
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_react-dom_1e674e59._.js (7908:176)
performWorkOnRootViaSchedulerTask
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_react-dom_1e674e59._.js (8882:9)
MessagePort.performWorkUntilDeadline
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_next_dist_compiled_5150ccfd._.js (2601:64)
Home
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/_298c9d48._.js (2959:215)
ClientPageRoot
file:///G:/My%20Drive/DataPlay/DATAPLAY_FRONTEND_NextJS/.next/static/chunks/node_modules_9337b2a9._.js (9282:50)
1
2
