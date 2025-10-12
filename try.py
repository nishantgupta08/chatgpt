<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Navbar Layout</title>
  <style>
    *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    /* Full-page main container */
    .main {
      width: 100%;
      height: 100vh; /* full viewport height */
      background-color: #f5f5f5;
    }

    /* Navbar styling */
    .navbar {
      width: 100%;
      height: 60px;
      background-color: #222;
      justify-content: space-between;
      align-items: center;
      color: white;
      display: flex      
    }
    .navbar_right ul{
        display: flex;
        justify-content: space-between;
        width: 60%;
        list-style: none;
    }

    /* Left text area */
    .navbar_left {
      width: 20%;
      padding: 20px;
    }

    /* Right text area */
    .navbar_right {
      width: 40%;
      text-align: right;
      display:flex;
    }
    .navbar_right a{
        text-decoration: none;
    }


    .navbar_right ul {
      display: flex;      
    }

    /* Hero Section */
    .hero {
      flex: 1;
      height: 180px;
      display: flex;
      align-items: center;
      background-color: red;
      justify-content: space-between;
      height: 300px;
    }

    .hero_left, .hero_right {
      width: 20%;
      background-color: green;
      height: 100%;
    }
    .hero_left img,.hero_right img{
        width: 100%;
        height: 100%;
    }
    .hero-centre{
        width:60% ;
    }
    </style>
</head>
<body>

  <div class="main">
      <!-- Navbar -->
    <nav>
    <div class="navbar">
      <div class="navbar_left">
        Welcome to React JS Workshop
      </div>
      <div class="navbar_right">
        <ul>
            <li><a href="#hero">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#agenda">Agenda</a></li>
            <li><a href="#speakers">Speakers</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
      </div>
    </div>
    </nav>
    <div class="hero">
      <div class="hero_left">        
        <img src="data:image/jpeg;base64,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">
      </div>
      
      <div class="hero_centre">
        <h1>Empowering Students with Real-World Web Design Skills</h1>
        <p>Join Dataplay’s Hands-on Web Design Workshop at Shri Mahaveer College</p>
        <p>📅 <b>Date:</b> 15th October 2025</p>
        <p>⏰ <b>Time:</b> 10:00 AM - 12:00 PM</p>
        <p>📍 <b>Venue:</b> Computer Science Department Auditorium</p>
      </div>
      <div class="hero_right">
        <img src="data:image/jpeg;base64,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7VcNo+XJc1ZYdhdA5jXl7HXkLgLNPHiAT7EFT9zx+q9R+8H8Nik9t2N+9eS3UkZs+pcIx83m8+oW+suzZZlKfJ+DS0WJOjc58usGMuItpaOOpo48FD7UshV2csViloZYGxRMIa2RzwdTjd54MI5Bo8kGWZGdi+FMfiGVaeRwkGkvEOsENPIEjtXJndmJVdYMVzVA9jnAMD3RaA617DlYm38l6Uylgwy9luDCm2JiYA4jkXHi8juLiVwbRMsHNmWXYbCWtk1NdG599IcDxvYE+iXDzQfPZvjXv9kiCqebvazdyfOZwufEAH6ypeB4b77YgKQO03BN7X5DsVg2WZPrMn009JickL45C1zBG550utZ19TBzGn7K7ct5WmwrFRVzujIAcOiXX4jvatvpdozpf34nwh84cggPvPOSOxrLH1klWvD6CPDqUU9ILNHtPae9da/Fn1300+0peaNjn7TIP434T16YWAHYliIlMkc9KOJ5Pl/yl/X+hjFP61T/ANrN/lqobdjuJNwfBpsSn9GKNz/Gw4DzNh5ryzl/8urswHFcFifNOx5lJazXZxN9RHiVuWNZNrazZvDlillhEg0iZ7nP0ua0k2adBJ6WjmByXRsryQ/JtDMK90bpZXi5jLiNLR0RdwBvdzvYgybOFRjuOYXbMVNLuoiX6vyfTpsCCS4DlZXP3PWN72gnwSU8Y3CVnzXcHjyIb9ta3V07aykfS1Au17XNcO0OFiPUVk2RNmVflTNTMT31O6MamvaHSanMcOzd2vfSefUg0jNmHx4pluoo6wXa6J3kQLtI7wQD5LANieHx1+e2GqGrdRvkaPlNsGny1X8QF6Or4jUUMkDLXcxzRfvFlmGzPZrV5TzGcSxCSBzN05lo3PJuS34zB2dqDV0REBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERB//9k=">
      </div>
    </div>
  </div>

</body>
</html>
