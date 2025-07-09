import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HustlerMob – Dein digitales Ökosystem</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  <style>
    :root { --brand-gold: #caa53b; --dark-bg: #0d0d0d; --card-bg: #1a1a1a; --text-light: #e0e0e0; --text-dark: #000; --border-color: #333; }
    body { font-family: "Roboto", sans-serif; background-color: var(--dark-bg); color: var(--text-light); margin: 0; line-height: 1.7; font-size: 17px; }
    .container { max-width: 960px; margin: 0 auto; padding: 0 20px; }
    header { text-align: center; padding: 60px 20px 40px; }
    .logo { width: 220px; height: auto; margin-bottom: 20px; }
    header h1 { font-family: 'Anton', sans-serif; font-size: 4em; font-weight: 400; text-transform: uppercase; letter-spacing: 4px; color: var(--brand-gold); margin: 0; }
    header p { font-size: 1.25em; color: #aaa; margin-top: 10px; max-width: 600px; margin-left: auto; margin-right: auto; }
    nav { background-color: var(--card-bg); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color); padding: 15px 0; text-align: center; position: sticky; top: 0; z-index: 1000; }
    nav a { color: var(--brand-gold); margin: 0 15px; text-decoration: none; font-weight: bold; transition: color 0.3s ease; }
    nav a:hover { color: #fff; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <svg class="logo" viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
          <rect width="300" height="150" fill="#caa53b"/>
          <rect y="15" width="300" height="120" fill="black"/>
          <text x="50%" y="58" dominant-baseline="middle" text-anchor="middle" font-family="'Anton', sans-serif" font-size="48" fill="white" letter-spacing="4">HUSTLER</text>
          <text x="50%" y="108" dominant-baseline="middle" text-anchor="middle" font-family="'Anton', sans-serif" font-size="48" fill="white" letter-spacing="4">MOB</text>
      </svg>
      <h1>HustlerMob</h1>
      <p>Mehr als eine App. Dein digitales Ökosystem für Selbstbestimmung.</p>
    </header>
    <nav>
      <a href="#about">Was ist das?</a>
      <a href="#features">Funktionen</a>
      <a href="#pricing">Preise</a>
      <a href="https://hustlermob1.streamlit.app/" target="_blank">App starten</a>
    </nav>
    <!-- Dein restlicher HTML-Inhalt hier einfügen -->
  </div>
</body>
</html>
"""

st.components.v1.html(html_code, height=5000, scrolling=True)
