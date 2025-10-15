{/* Feature cards */}
<section aria-label="Program highlights">
  <div role="list" className="grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-4 mb-8">
    {features.map((f: Feature, i: number) => {
      const tones = [
        { grad: "from-blue-500 to-blue-600", ring: "ring-blue-100" },
        { grad: "from-lime-500 to-lime-600", ring: "ring-lime-100" },
        { grad: "from-pink-500 to-fuchsia-500", ring: "ring-pink-100" },
        { grad: "from-orange-500 to-orange-600", ring: "ring-orange-100" },
      ][i % 4];

      const itemClass = [
        "group block rounded-2xl bg-white border border-slate-200 shadow-sm",
        "p-5 sm:p-6 min-h-[112px] h-full",
        "ring-1 ring-transparent",
        tones.ring,
        "transition-all hover:shadow-md hover:-translate-y-[2px]",
        "focus:outline-none focus-visible:ring-2 focus-visible:ring-slate-400",
      ].join(" ");

      const content = (
        <div className="flex items-start gap-4">
          <span
            className={[
              "inline-flex size-12 items-center justify-center rounded-[14px] text-white shadow-md bg-gradient-to-b",
              tones.grad,
            ].join(" ")}
            aria-hidden="true"
          >
            <Image
              src={f.icon}
              alt=""
              width={22}
              height={22}
              className="w-[22px] h-[22px] object-contain filter brightness-0 invert"
            />
          </span>
          <h3 className="text-[15px] sm:text-base font-extrabold text-slate-900 leading-snug">
            {f.title}
          </h3>
        </div>
      );

      return f.href ? (
        <a key={i} href={f.href} role="listitem" className={itemClass}>
          {content}
        </a>
      ) : (
        <div key={i} role="listitem" className={itemClass}>
          {content}
        </div>
      );
    })}
  </div>
</section>
