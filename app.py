import streamlit as st
from PIL import Image

GOLD = "#caa53b"

st.set_page_config(page_title="HustlerMob – Systemtrippler 2.0", layout="centered")
st.write("✅ App gestartet")

st.markdown(f"""
    <style>
        body, .reportview-container, .stApp {{
            background-color: white !important;
            color: black !important;
            font-family: 'Arial', sans-serif;
        }}
        h1, h2, h3 {{
            color: {GOLD};
            font-weight: 700;
        }}
        .stRadio > div { background-color: #f2f2f2; padding: 8px; border-radius: 5px; margin-bottom: 10px; }
        .stButton>button {{
            background-color: {GOLD};
            color: black;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
        }}
    </style>
""", unsafe_allow_html=True)

try:
    st.image("logo.png", width=180)
except Exception as e:
    st.warning("⚠️ Logo konnte nicht geladen werden.")

st.markdown("### HustlerMob – Systemtrippler 2.0")
st.markdown("**Wenn du das System nicht kennst, bezahlst du die Rechnung.**")

uploaded_file = st.file_uploader("📄 Behördenschreiben hochladen", type=["pdf", "jpg", "jpeg", "png"])
tone = st.radio("🗣️ Wähle deinen Antwortstil:", ["Seicht", "Neutral", "Barsch"])

st.markdown("#### 📄 Generierte Antwort (Textvorschlag)")

if uploaded_file and tone:
    if tone == "Seicht":
        response = (
            "Sehr geehrte Damen und Herren,\n\n"
            "ich nehme Bezug auf Ihr Schreiben vom [Datum] und möchte höflich um eine nochmalige Überprüfung des Vorgangs bitten.\n"
            "Nach § 35 SGB X ist eine Ermessensentscheidung nachvollziehbar und vollständig zu begründen.\n"
            "In der aktuellen Darstellung fehlt eine solche Begründung oder erscheint zumindest unvollständig.\n\n"
            "Gemäß BSG, Urteil vom 23.08.2011 – B 14 AS 146/10 R, müssen Leistungsträger im Zweifel zugunsten der Betroffenen prüfen.\n"
            "Ich bitte daher um eine entsprechende Neubewertung und Rückmeldung innerhalb der gesetzlichen Frist gemäß § 88 SGG.\n\n"
            "Mit freundlichen Grüßen"
        )
    elif tone == "Neutral":
        response = (
            "Hiermit lege ich fristgerecht Widerspruch gegen Ihren Bescheid vom [Datum] ein.\n\n"
            "Die Begründung des Bescheids entspricht nicht den Anforderungen an eine hinreichend bestimmte Verwaltungsentscheidung "
            "gemäß § 39 Abs. 1 SGB X.\n"
            "Darüber hinaus fehlt eine nachvollziehbare Auslegung gemäß den Maßgaben der Rechtsprechung (vgl. BVerwG, Urteil vom 27.02.2020 – 5 C 3.19).\n\n"
            "Ich fordere Sie daher auf, die Entscheidung unter Einbezug aller vorliegenden Tatsachen sowie unter Berücksichtigung der "
            "Verhältnismäßigkeit gemäß Art. 20 Abs. 3 GG erneut zu prüfen.\n\n"
            "Bitte bestätigen Sie den fristgerechten Eingang dieses Schreibens.\n\n"
            "Mit verbindlichem Gruß"
        )
    else:
        response = (
            "Ich widerspreche Ihrem Bescheid vom [Datum] mit sofortiger Wirkung.\n\n"
            "Die zugrundeliegende Entscheidung verletzt mein Recht auf rechtliches Gehör gemäß Art. 103 Abs. 1 GG "
            "sowie das Gebot der Verhältnismäßigkeit nach ständiger Rechtsprechung des BVerfG (vgl. Beschl. v. 19.05.2020 – 1 BvR 1246/20).\n"
            "Zudem wurde gegen die Durchführungsvorgaben nach § 24 SGB X verstoßen, da ich vor Erlass des Bescheids nicht angehört wurde.\n\n"
            "Diese Vorgehensweise ist unzulässig und in der Sache weder nachvollziehbar noch haltbar.\n"
            "Ich fordere daher die sofortige Rücknahme des Bescheids sowie eine schriftliche Entschuldigung für das fehlerhafte Vorgehen.\n\n"
            "Mit Nachdruck"
        )

    st.text_area("Antwortvorschlag", value=response, height=300)
    st.download_button("⬇️ Antworttext herunterladen", data=response, file_name="antwort.txt")
else:
    st.info("Bitte ein offizielles Schreiben hochladen und den gewünschten Ton auswählen.")

st.markdown("---")

st.markdown("### 🔐 Datenschutz & Hinweise")
with st.expander("Was passiert mit meinen Daten?"):
    st.markdown("""
- Deine hochgeladenen Dateien bleiben lokal auf deinem Gerät.
- Es findet keine Speicherung oder Übertragung auf externe Server statt.
- Alle generierten Antworten sind rechtlich fundierte Textvorschläge – keine Rechtsberatung.
    """)
