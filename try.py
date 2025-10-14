<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>React.JS Workshop — Dataplay</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root{
      --bg:#0f172a;
      --ink:#0b1220;
      --muted:#6b7280;
      --brand:#f59e0b;       /* amber */
      --brand-2:#f97316;     /* orange */
      --paper:#ffffff;
      --card:#ffffff;
      --ring:rgba(0,0,0,.08);
      --shadow:0 10px 30px rgba(0,0,0,.08);
      --radius:18px;
      --gap:24px;
      --container:1080px;
    }
    *{box-sizing:border-box}
    html{scroll-behavior:smooth}
    body{
      margin:0;
      font-family:Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, "Segoe UI Emoji", "Apple Color Emoji", "Noto Color Emoji", sans-serif;
      color:var(--ink);
      background:#f6f7fb;
      line-height:1.5;
    }
    a{text-decoration:none;color:inherit}
    /* ===== Navbar ===== */
    .navbar{
      position:sticky; top:0; inset-inline:0;
      height:66px;
      background:#222;
      color:#fff;
      z-index:1000;
      box-shadow:0 2px 10px rgba(0,0,0,.15);
    }
    .nav-inner{
      max-width:var(--container);
      margin:auto;
      height:100%;
      display:flex; align-items:center; justify-content:space-between;
      padding:0 16px;
    }
    .brand{
      display:flex; align-items:center; gap:12px;
      font-weight:700; letter-spacing:.2px;
      white-space:nowrap;
    }
    .brand small{font-weight:600;color:#d1d5db;opacity:.9}
    .nav-links{display:flex; align-items:center; gap:8px;}
    .nav-links a{
      color:#e5e7eb; padding:8px 12px; border-radius:10px; font-weight:600;
    }
    .nav-links a:hover{background:rgba(255,255,255,.08)}
    .burger{display:none;background:transparent;border:0;color:#fff;font-size:28px;line-height:0;cursor:pointer}
    /* ===== Hero ===== */
    .hero{
      background:linear-gradient(180deg,var(--brand) 0%, var(--brand-2) 100%);
      color:#fff;
      padding:32px 16px 48px;
    }
    .hero-wrap{
      max-width:var(--container); margin:auto;
      display:grid;
      grid-template-columns:140px 1fr 140px;
      gap:16px;
      align-items:stretch;
      min-height:280px;
    }
    .hero-logo{
      background:rgba(255,255,255,.15);
      border-radius:14px;
      overflow:hidden;
      display:grid; place-items:center;
    }
    .hero-logo img{width:100%; height:100%; object-fit:cover}
    .hero-card{
      background:var(--paper);
      color:var(--ink);
      border-radius:var(--radius);
      box-shadow:var(--shadow);
      padding:28px 28px;
      display:flex; flex-direction:column; gap:10px;
      justify-content:center;
      text-align:center;
    }
    .kicker{font-weight:700;color:#ef4444; text-transform:uppercase; letter-spacing:.12em; font-size:12px}
    h1{margin:4px 0 6px; font-size:28px; line-height:1.2}
    .sub{color:#374151; font-weight:500; margin:0 0 8px}
    .meta{display:grid; gap:6px; margin-top:6px; color:#111827; font-weight:600}
    .meta b{font-weight:800}
    /* ===== Sections ===== */
    .section{padding:56px 16px}
    .container{max-width:var(--container); margin:auto}
    .section h2{text-align:center; font-size:24px; margin:0 0 16px}
    .section p.lead{max-width:880px; margin:0 auto 8px; color:#374151}
    /* About */
    .about-card{
      background:var(--card); border-radius:var(--radius); box-shadow:var(--shadow);
      padding:26px; max-width:900px; margin:18px auto 0; text-align:center;
    }
    /* Agenda */
    .agenda{
      background:linear-gradient(180deg,#fff7ed 0,#fff 100%);
    }
    .agenda-list{
      max-width:860px; margin:6px auto 0; display:grid; gap:10px;
      background:var(--card); border-radius:var(--radius); box-shadow:var(--shadow); padding:18px;
    }
    .agenda-item{
      display:grid; grid-template-columns:auto 1fr auto; gap:14px; align-items:center;
      padding:10px 12px; border-radius:12px; border:1px solid var(--ring);
    }
    .agenda-item .num{
      width:34px; height:34px; display:grid; place-items:center; border-radius:10px;
      background:#111827; color:#fff; font-weight:800;
    }
    .agenda-item .title{font-weight:700}
    .agenda-item .time{color:#4b5563; font-weight:700; white-space:nowrap}
    /* Speakers */
    .speaker-grid{
      max-width:980px; margin:18px auto 0;
      display:grid; gap:16px; grid-template-columns:1fr;
    }
    .speaker{
      background:var(--card); border-radius:var(--radius); box-shadow:var(--shadow);
      padding:14px 16px; display:flex; align-items:center; gap:14px;
    }
    .avatar{
      width:56px; height:56px; border-radius:50%;
      background:#eef2ff; display:grid; place-items:center; font-weight:800; font-size:18px; color:#3730a3;
      border:2px solid #e5e7eb;
    }
    .role{color:#6b7280; font-weight:600}
    /* Contact */
    .contact-card{
      background:var(--card); border-radius:var(--radius); box-shadow:var(--shadow);
      padding:22px; max-width:820px; margin:18px auto 0; text-align:center;
    }
    footer{
      background:#111827; color:#d1d5db; padding:18px 16px; text-align:center; font-weight:600
    }
    /* ===== Responsive ===== */
    @media (max-width: 900px){
      .hero-wrap{grid-template-columns:80px 1fr 80px}
      h1{font-size:24px}
    }
    @media (max-width: 720px){
      .burger{display:inline-block}
      .nav-links{display:none; position:absolute; top:66px; right:12px; background:#111; border:1px solid rgba(255,255,255,.08); padding:8px; border-radius:12px; box-shadow:0 12px 30px rgba(0,0,0,.25)}
      .nav-links a{display:block; padding:10px 12px}
      .nav-links.open{display:block}
      .hero-wrap{grid-template-columns:1fr; gap:12px}
      .hero-logo{height:84px}
      .hero-card{text-align:left}
      .speaker-grid{grid-template-columns:1fr}
    }
  </style>
</head>
<body>
  <!-- ===== NAVBAR ===== -->
  <header class="navbar" role="banner">
    <div class="nav-inner">
      <div class="brand">
        <span>React.JS Workshop</span>
        <small>by Dataplay</small>
      </div>
      <button class="burger" aria-label="Toggle menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>
      <nav class="nav-links" aria-label="Primary">
        <a href="#hero">Home</a>
        <a href="#about">About</a>
        <a href="#agenda">Agenda</a>
        <a href="#speakers">Speakers</a>
        <a href="#contact">Contact</a>
      </nav>
    </div>
  </header>

  <!-- ===== HERO ===== -->
  <section id="hero" class="hero" aria-label="Hero">
    <div class="hero-wrap">
      <div class="hero-logo" aria-hidden="true">
        <!-- College / Partner Logo (left) -->
        <img alt="College logo" src="data:image/jpeg;base64,REPLACE_WITH_YOUR_LEFT_LOGO_BASE64_IF_NEEDED">
      </div>
      <div class="hero-card">
        <span class="kicker">Join Us</span>
        <h1>Empowering Students with Real-World Web Design Skills</h1>
        <p class="sub">Join Dataplay’s hands-on Web Design Workshop at Shri Mahaveer College</p>
        <div class="meta" role="list">
          <div role="listitem">📅 <b>Date:</b> 15th October 2025</div>
          <div role="listitem">⏰ <b>Time:</b> 10:00 AM – 12:00 PM</div>
          <div role="listitem">📍 <b>Venue:</b> Computer Science Department Auditorium</div>
        </div>
      </div>
      <div class="hero-logo" aria-hidden="true">
        <!-- Dataplay logo (right) -->
        <img alt="Dataplay logo" src="data:image/jpeg;base64,REPLACE_WITH_YOUR_RIGHT_LOGO_BASE64_IF_NEEDED">
      </div>
    </div>
  </section>

  <!-- ===== ABOUT ===== -->
  <section id="about" class="section">
    <div class="container">
      <h2>About the Workshop</h2>
      <div class="about-card">
        <p class="lead">
          This hands-on workshop aims to bridge the gap between theoretical knowledge and real-world web
          development practices. Students will learn how to structure web pages using HTML, style them with CSS,
          and gain insights into practical industry workflows. The session will focus on applied learning and
          problem-solving in design and development.
        </p>
      </div>
    </div>
  </section>

  <!-- ===== AGENDA ===== -->
  <section id="agenda" class="section agenda">
    <div class="container">
      <h2>Workshop Agenda</h2>
      <div class="agenda-list" role="list">
        <div class="agenda-item" role="listitem">
          <div class="num">1</div>
          <div class="title">Introduction &amp; Icebreaker</div>
          <div class="time">10 mins</div>
        </div>
        <div class="agenda-item" role="listitem">
          <div class="num">2</div>
          <div class="title">Understanding HTML Basics</div>
          <div class="time">20 mins</div>
        </div>
        <div class="agenda-item" role="listitem">
          <div class="num">3</div>
          <div class="title">Styling with CSS</div>
          <div class="time">25 mins</div>
        </div>
        <div class="agenda-item" role="listitem">
          <div class="num">4</div>
          <div class="title">Building Your First Web Page</div>
          <div class="time">30 mins</div>
        </div>
        <div class="agenda-item" role="listitem">
          <div class="num">5</div>
          <div class="title">Q&amp;A and Career Guidance</div>
          <div class="time">15 mins</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== SPEAKERS ===== -->
  <section id="speakers" class="section">
    <div class="container">
      <h2>Speakers</h2>
      <div class="speaker-grid">
        <div class="speaker">
          <div class="avatar" aria-hidden="true">NG</div>
          <div>
            <div class="title" style="font-weight:800">Nishant Gupta</div>
            <div class="role">Co-founder @ Dataplay</div>
          </div>
        </div>
        <div class="speaker">
          <div class="avatar" aria-hidden="true">KS</div>
          <div>
            <div class="title" style="font-weight:800">Kushwant Singh</div>
            <div class="role">Mentor @ Dataplay</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== CONTACT ===== -->
  <section id="contact" class="section">
    <div class="container">
      <h2>Contact</h2>
      <div class="contact-card">
        <p class="lead">
          Questions about the workshop or campus logistics?
        </p>
        <p style="margin:8px 0 0; font-weight:600">📧 hello@dataplay.example &nbsp;&nbsp; | &nbsp;&nbsp; 📞 +91-90000-00000</p>
      </div>
    </div>
  </section>

  <footer>
    © 2025 Dataplay | Shri Mahaveer College Workshop | All Rights Reserved
  </footer>

  <script>
    // Close the mobile menu when clicking a link
    document.querySelectorAll('.nav-links a').forEach(a=>{
      a.addEventListener('click', ()=>document.querySelector('.nav-links').classList.remove('open'));
    });
  </script>
</body>
</html>
