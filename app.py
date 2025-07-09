import streamlit as st

st.set_page_config(page_title="HustlerMob", layout="centered")

st.write("✅ HustlerMob gestartet")

# Kein CSS mehr – absolute Klartext-Darstellung
try:
    st.image("logo.png", width=160)
except:
    pass

st.markdown("## HustlerMob – Systemtrippler 2.0")
st.markdown("**Wenn du das System nicht kennst, bezahlst du die Rechnung.**")

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

# Einfacher Textblock ohne Boxen
st.markdown("### 📡 Folge & unterstütze uns")
st.markdown("""
- [TikTok](https://www.tiktok.com/@hustlerbiz.de)  
- [Instagram](https://www.instagram.com/hustlerbizreal/)  
- [YouTube](https://www.youtube.com/@HustlerBizReal)  
- [hustlerbiz.de](https://hustlerbiz.de/)
""")

st.markdown("### 🛒 Unsere Produkte")
st.markdown("""
- [Kinderbücher](https://hustlerbiz.de/b/3790l)  
- [Dreifaltigkeit (E-Book)](https://hustlerbiz.de/b/qovdu)
""")

st.markdown("📬 Unser Tipp: [Jetzt den HustlerLetter abonnieren](https://hustlerbiz.de/b/NZUso)")

st.markdown("### ❓ Häufige Fragen")
st.markdown("👉 [Zur FAQ-Seite](https://www.hustlermob.de/faq/)")

st.markdown("---")
with st.expander("🔐 Was passiert mit meinen Daten?"):
    st.markdown("""
- Alles bleibt lokal auf deinem Gerät.  
- Keine Weiterleitung. Keine Speicherung. Kein Tracking.  
- Die generierten Texte sind keine Rechtsberatung.
    """)
