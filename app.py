import streamlit as st
from PIL import Image

st.set_page_config(page_title="HustlerMob App", layout="centered")
st.write("✅ HustlerMob gestartet")

# Layout-Stil
st.markdown("""
    <style>
        body, .stApp {
            background-color: white;
            color: black;
            font-family: 'Arial', sans-serif;
        }
        h1, h2, h3 {
            color: #caa53b;
        }
        .stButton>button {
            background-color: #caa53b;
            color: black;
            font-weight: bold;
            border-radius: 5px;
        }
        .stRadio > div {
            background-color: #f5f5f5;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        footer {
            margin-top: 40px;
            font-size: 14px;
            color: #888;
        }
        .linkbox {
            background: #f1f1f1;
            border-left: 5px solid #caa53b;
            padding: 10px 15px;
            margin: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Logo
try:
    st.image("logo.png", width=160)
except:
    pass

st.markdown("## HustlerMob – Systemtrippler 2.0")
st.markdown("**Wenn du das System nicht kennst, bezahlst du die Rechnung.**")

# Datei und Auswahl
uploaded_file = st.file_uploader("📄 Behördenschreiben hochladen", type=["pdf", "jpg", "jpeg", "png"])
tone = st.radio("🗣️ Wähle deinen Antwortstil:", ["Seicht", "Neutral", "Barsch"])

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
    st.info("Bitte Schreiben hochladen und Ton auswählen.")

# Social Media + Shop
st.markdown("### 📡 Folge & unterstütze uns")
st.markdown("""
<div class="linkbox">
🔗 [TikTok](https://www.tiktok.com/@hustlerbiz.de)  
🔗 [Instagram](https://www.instagram.com/hustlerbizreal/)  
🔗 [YouTube](https://www.youtube.com/@HustlerBizReal)  
🔗 [hustlerbiz.de](https://hustlerbiz.de/)
</div>
""", unsafe_allow_html=True)

st.markdown("### 🛒 Unsere Produkte")
st.markdown("""
<div class="linkbox">
📘 [Kinderbücher](https://hustlerbiz.de/b/3790l)  
📗 [Dreifaltigkeit (E-Book)](https://hustlerbiz.de/b/qovdu)
</div>
""", unsafe_allow_html=True)

# Werbung
st.markdown("### 📢 Unsere Empfehlung")
st.info("💡 Kennst du schon unsere neuen Schriftsatz-Guides? Exklusiv im Shop!")

# FAQ
st.markdown("### ❓ Häufige Fragen")
st.markdown("👉 [Zur FAQ-Seite](https://www.hustlermob.de/faq/)")

# Datenschutz
st.markdown("---")
with st.expander("🔐 Was passiert mit meinen Daten?"):
    st.markdown("""
- Alles bleibt lokal auf deinem Gerät.
- Keine Weiterleitung. Keine Speicherung. Kein Tracking.
- Die generierten Texte sind keine Rechtsberatung.
    """)
