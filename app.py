from hustlermob_antworten_final import antworten


import streamlit as st

st.set_page_config(page_title="HustlerMob", layout="centered")

st.write("✅ HustlerMob gestartet")

try:
    st.image("logo.png", width=160)
except:
    pass

st.markdown("## HustlerMob – Systemtrippler 2.0")
st.markdown("**Wenn du das System nicht kennst, bezahlst du die Rechnung.**")

uploaded_file = st.file_uploader("📄 Behördenschreiben hochladen", type=["pdf", "jpg", "jpeg", "png"])

if "tone" not in st.session_state:
    st.session_state.tone = ""

# Benutzerdefinierte Textauswahl mit HTML und JavaScript
st.markdown("### 🗣️ Wähle deinen Antwortstil:")

selection_style = '''
<style>
.option-text {
    font-size: 18px;
    margin: 10px 0;
    cursor: pointer;
    color: white;
    background-color: #333;
    padding: 8px 15px;
    border-radius: 5px;
    display: inline-block;
}
.option-text:hover {
    background-color: #555;
}
.active-option {
    background-color: #008080 !important;
}
</style>
'''

st.markdown(selection_style, unsafe_allow_html=True)

clicked = st.empty()

def set_tone(selected_tone):
    st.session_state.tone = selected_tone

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Seicht"):
        set_tone("Seicht")
with col2:
    if st.button("Gemäßigt"):
        set_tone("Gemäßigt")
with col3:
    if st.button("Barsch"):
        set_tone("Barsch")

tone = st.session_state.tone


if uploaded_file and tone:
    response = antworten.get(tone, "Keine passende Antwort gefunden.")
    st.text_area("📄 Antwortvorschlag", value=response, height=300)
    st.download_button("⬇️ Antworttext herunterladen", data=response, file_name="antwort.txt")
else:
    st.info("Bitte ein offizielles Schreiben hochladen und Stil auswählen.")
st.info("Bitte ein offizielles Schreiben hochladen und Stil auswählen.")

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
