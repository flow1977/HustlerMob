
import streamlit as st


antworten = {
    "Seicht": """Sehr geehrte Damen und Herren,

ich habe Ihre Entscheidung aufmerksam geprüft und komme zu dem Schluss, dass sie auf einer Darstellung beruht, die in Teilen nicht meinem tatsächlichen Lebenssachverhalt entspricht.

Ich bin zuversichtlich, dass bei vollständiger Würdigung aller Umstände eine andere Bewertung möglich ist – zumal der Ausgangspunkt der Maßnahme auf Annahmen basiert, die nicht mit belastbaren Fakten unterlegt wurden.

Ich bitte daher um erneute Prüfung – in der Sache, im Ton und im Ziel.

Mit freundlichem Gruß""",

    "Gemäßigt": """Sehr geehrte Damen und Herren,

gegen Ihre Entscheidung lege ich hiermit form- und fristgerecht Widerspruch ein.

Der Vorgang ist weder vollständig geprüft worden, noch sind alle maßgeblichen Tatsachen berücksichtigt worden. Ich erkenne eine fehlerhafte oder zumindest verkürzte Tatsachengrundlage, die zu einer falschen rechtlichen Bewertung geführt hat.

Ich fordere eine Neubeurteilung auf Basis vollständiger Informationen. Sollte dies nicht möglich sein, bitte ich um eine schriftliche Darlegung der Entscheidungsgrundlage mit Bezug auf die konkreten Beweismittel.

Ich erwarte Ihre Antwort.

Mit verbindlichem Gruß""",

    "Barsch": """Sehr geehrte Damen und Herren,

ich widerspreche Ihrer Entscheidung in vollem Umfang.

Die Maßnahme ist weder sachlich haltbar noch rechtlich tragfähig. Es fehlt an nachvollziehbarer Begründung, belastbarer Tatsachengrundlage und fairer Anhörung. Das gesamte Verfahren weist strukturelle Fehler auf, die eine vollständige Rückabwicklung erforderlich machen.

Ich fordere Sie auf, die Entscheidung umgehend zu überprüfen und zurückzunehmen.

Sollte innerhalb von 7 Tagen keine Rückmeldung erfolgen, leite ich eine Dienstaufsichtsbeschwerde ein – mit entsprechender Aktenlage.

Mit Nachdruck"""
}


st.set_page_config(page_title="HustlerMob", layout="centered")

try:
    st.image("logo.png", width=160)
except:
    pass

st.markdown("## HustlerMob – Systemtrippler 2.0")
st.markdown("**Wenn du das System nicht kennst, bezahlst du die Rechnung.**")

st.markdown("### Schritt 1: Lade dein Dokument hoch")
uploaded_file = st.file_uploader("Was auch immer sie dir geschickt haben – lade es hier hoch:", type=["pdf", "jpg", "jpeg", "png"])

if "tone" not in st.session_state:
    st.session_state.tone = ""

st.markdown("### Schritt 2: Wähle deinen Ton")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Seicht"):
        st.session_state.tone = "Seicht"
with col2:
    if st.button("Gemäßigt"):
        st.session_state.tone = "Gemäßigt"
with col3:
    if st.button("Barsch"):
        st.session_state.tone = "Barsch"

tone = st.session_state.tone

if uploaded_file and tone:
    response = antworten.get(tone, "Keine passende Antwort gefunden.")
    st.markdown("### Schritt 3: Dein Antworttext")
    st.text_area("Unten findest du den fertigen Entwurf. Prüfe ihn, passe ihn an – und schick ihn raus.", value=response, height=300)
    st.download_button("⬇️ Als .txt speichern", data=response, file_name="antwort.txt")
else:
    st.info("Dokument hochladen und Ton auswählen, Bruder.")

st.markdown("---")
st.markdown("### 📡 Folge & unterstütze uns")
st.markdown("""
- [TikTok](https://www.tiktok.com/@hustlerbiz.de)  
- [Instagram](https://www.instagram.com/hustlerbizreal/)  
- [YouTube](https://www.youtube.com/@HustlerBizReal)  
- [Zur Website](https://hustlerbiz.de/)
""")

st.markdown("### 🛒 Unsere Produkte")
st.markdown("""
- [Kinderbücher](https://hustlerbiz.de/b/3790l)  
- [E-Book Dreifaltigkeit](https://hustlerbiz.de/b/qovdu)
""")

st.markdown("📬 Unser Newsletter: [Jetzt abonnieren](https://hustlerbiz.de/b/NZUso)")

st.markdown("### ❓ Häufige Fragen")
st.markdown("👉 [Zur FAQ](https://www.hustlermob.de/faq/)")

st.markdown("---")
with st.expander("🔐 Datensicherheit"):
    st.markdown("""
- Alles bleibt lokal. Keine Weiterleitung. Keine Speicherung. Kein Tracking.
- Die Texte sind keine Rechtsberatung – sondern Werkzeuge für Selbstdenkende.
""")
