<a
  href="#contact-us"
  onClick={(e) => {
    e.preventDefault();
    window.dispatchEvent(new CustomEvent('openCounsellingModal'));
  }}
  className="inline-flex items-center justify-center gap-2 rounded-xl bg-black text-white px-6 py-3 font-bold hover:bg-darkBlue focus:outline-none focus-visible:ring-2 focus-visible:ring-black"
  aria-label="Book 1:1 Counselling Session"
>
  <Icon icon="mdi:rocket-launch-outline" className="mr-2 text-xl" />
  Book 1:1 Counselling Session
</a>
