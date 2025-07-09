import streamlit as st

st.set_page_config(page_title="HustlerMob", layout="centered")
st.write("✅ HustlerMob gestartet")

# Minimaler Style
st.markdown("""
<style>
body, .stApp {
    background-color: white;
    color: black;
    font-family: Arial, sans-serif;
}
h1, h2, h3 {
    color: #caa53b;
}
.stButton>button {
    background-color: #caa53b !important;
    color: black !important;
    font-weight: bold;
    border-radius: 6px;
    padding: 10px 20px;
}
.linkbox {
    background: #f1f1f1;
    border-left: 5px solid #caa53b;
    padding: 10px 15px;
    margin: 20px 0;
}
.hustlerletter {
    background-color: #000;
    color: white;
    padding: 15px;
    border-radius: 6px;
    font-weight: bold;
}
.hustlerletter a {
    color: #ffffff;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# Logo anzeigen
try:
    st.image("logo.png", width=160)
except:
    st.write("🖼️ Logo nicht geladen")

st.markdown("## HustlerMob – Systemtrippler 2.0")
st.markdown("**Wenn du das System nicht kennst, bezahlst du die Rechnung.**")

# Datei und Ton-Auswahl
uploaded_file = st.file_uploader("📄 Behördenschreiben hochladen", type=["pdf", "jpg", "jpeg", "png"])
tone = st.radio("🗣️ Wähle deinen Antwortstil:", ["Seicht", "Neutral", "Barsch"], index=0)

if uploaded_file and tone:
    if tone == "Seicht":
        response = "Sehr geehrte Damen und Herren,\n\n[...] § 35 SGB X [...] BSG, Urteil vom 23.08.2011 – B 14 AS 146/10 R [...]"
    elif tone == "Neutral":
        response = "Hiermit lege ich fristgerecht Widerspruch ein.\n\n[...] § 39 Abs. 1 SGB X [...] BVerwG, Urteil vom 27.02.2020 [...]"
    else:
        response = "Ich widerspreche mit sofortiger Wirkung.\n\n[...] Art. 103 Abs. 1 GG [...] § 24 SGB X [...] BVerfG 1 BvR 1246/20 [...]"
    st.text_area("📄 Antwortvorschlag", value=response, height=300)
    st.download_button("⬇️ Antworttext herunterladen", data=response, file_name="antwort.txt")
else:
    st.info("Bitte ein offizielles Schreiben hochladen und Ton auswählen.")

# Socials
st.markdown("### 📡 Folge & unterstütze uns", unsafe_allow_html=True)
st.markdown("""
<div class="linkbox">
🔗 <a href="https://www.tiktok.com/@hustlerbiz.de" target="_blank">TikTok</a><br>
🔗 <a href="https://www.instagram.com/hustlerbizreal/" target="_blank">Instagram</a><br>
🔗 <a href="https://www.youtube.com/@HustlerBizReal" target="_blank">YouTube</a><br>
🔗 <a href="https://hustlerbiz.de/" target="_blank">hustlerbiz.de</a>
</div>
""", unsafe_allow_html=True)

# Produkte
st.markdown("### 🛒 Unsere Produkte", unsafe_allow_html=True)
st.markdown("""
<div class="linkbox">
📘 <a href="https://hustlerbiz.de/b/3790l" target="_blank">Kinderbücher</a><br>
📗 <a href="https://hustlerbiz.de/b/qovdu" target="_blank">Dreifaltigkeit (E-Book)</a>
</div>
""", unsafe_allow_html=True)

# Tipp
st.markdown("""
<div class="hustlerletter">
📬 Unser Tipp: <a href="https://hustlerbiz.de/b/NZUso" target="_blank">Jetzt den HustlerLetter abonnieren</a>
</div>
""", unsafe_allow_html=True)

# FAQ + Datenschutz
st.markdown("### ❓ Häufige Fragen")
st.markdown("👉 [Zur FAQ-Seite](https://www.hustlermob.de/faq/)")

st.markdown("---")
with st.expander("🔐 Was passiert mit meinen Daten?"):
    st.markdown("""
- Alles bleibt lokal auf deinem Gerät.
- Keine Weiterleitung. Keine Speicherung. Kein Tracking.
- Die generierten Texte sind keine Rechtsberatung.
    """)
