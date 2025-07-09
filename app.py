
import streamlit as st

# Antworttexte in 3 Tonstufen
antworten = {
    "Seicht": '''Sehr geehrte Damen und Herren,

ich habe Ihre Entscheidung aufmerksam geprüft und komme zu dem Schluss, dass sie auf einer Darstellung beruht, die in Teilen nicht meinem tatsächlichen Lebenssachverhalt entspricht.

Ich bin zuversichtlich, dass bei vollständiger Würdigung aller Umstände eine andere Bewertung möglich ist – zumal der Ausgangspunkt der Maßnahme auf Annahmen basiert, die nicht mit belastbaren Fakten unterlegt wurden.

Ich bitte daher um erneute Prüfung – in der Sache, im Ton und im Ziel.

Mit freundlichem Gruß''',

    "Gemäßigt": '''Sehr geehrte Damen und Herren,

gegen Ihre Entscheidung lege ich hiermit form- und fristgerecht Widerspruch ein.

Der Vorgang ist weder vollständig geprüft worden, noch sind alle maßgeblichen Tatsachen berücksichtigt worden. Ich erkenne eine fehlerhafte oder zumindest verkürzte Tatsachengrundlage, die zu einer falschen rechtlichen Bewertung geführt hat.

Ich fordere eine Neubeurteilung auf Basis vollständiger Informationen. Sollte dies nicht möglich sein, bitte ich um eine schriftliche Darlegung der Entscheidungsgrundlage mit Bezug auf die konkreten Beweismittel.

Ich erwarte Ihre Antwort.

Mit verbindlichem Gruß''',

    "Barsch": '''Sehr geehrte Damen und Herren,

ich widerspreche Ihrer Entscheidung in vollem Umfang.

Die Maßnahme ist weder sachlich haltbar noch rechtlich tragfähig. Es fehlt an nachvollziehbarer Begründung, belastbarer Tatsachengrundlage und fairer Anhörung. Das gesamte Verfahren weist strukturelle Fehler auf, die eine vollständige Rückabwicklung erforderlich machen.

Ich fordere Sie auf, die Entscheidung umgehend zu überprüfen und zurückzunehmen.

Sollte innerhalb von 7 Tagen keine Rückmeldung erfolgen, leite ich eine Dienstaufsichtsbeschwerde ein – mit entsprechender Aktenlage.

Mit Nachdruck'''
}

st.set_page_config(page_title="HustlerMob", layout="centered")

# Style Injection
st.markdown("""
<style>
    body { background-color: #000; color: #fff; }
    .main { background-color: #000; }
    h1, h2, h3, .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        color: #caa53b !important;
    }
    .stButton>button {
        background-color: #caa53b;
        color: #000;
        font-weight: bold;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

st.image("logo.png", width=180)
st.title("HustlerMob – Online")
st.markdown("**Wenn du das System nicht kennst, bezahlst du die Rechnung.**")

uploaded = st.file_uploader("📎 Hochladen: Bescheid, Ablehnung oder Forderung", type=["pdf", "png", "jpg", "jpeg"])

tone = st.radio("🗣️ Wie willst du antworten?", ["Seicht", "Gemäßigt", "Barsch"])

if uploaded and tone:
    response = antworten.get(tone, "")
    st.markdown("### 💬 Deine Antwort")
    st.text_area("Du kannst den Text direkt verwenden oder bearbeiten:", value=response, height=300)
    st.download_button("Antworttext herunterladen", data=response, file_name="antwort.txt")
else:
    st.info("Lade ein Dokument hoch und wähle die Tonlage.")

st.markdown("---")
st.markdown("📡 [Zur Hauptseite](https://hustlermob.de)  •  [TikTok](https://www.tiktok.com/@hustlerbiz.de)  •  [Instagram](https://www.instagram.com/hustlerbizreal/)")
