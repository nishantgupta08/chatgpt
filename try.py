Event handlers cannot be passed to Client Component props.
  <form className=... onSubmit={function onSubmit} children=...>
                               ^^^^^^^^^^^^^^^^^^^
If you need interactivity, consider converting part of this to a Client Component.

app/landing/page.tsx (219:44) @ Page


  217 |
  218 |             {/* RIGHT */}
> 219 |             <div className="lg:col-span-6"><EnrollForm /></div>
      |                                            ^
  220 |           </div>
  221 |
  222 |           {/* partners logos under hero */}
Call Stack
8

Show 5 ignore-listed frame(s)
stringify
<anonymous>
stringify
<anonymous>
Page
app/landing/page.tsx (219:44)
