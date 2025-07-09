
import streamlit as st

st.set_page_config(page_title='HustlerMob', page_icon='🛡️', layout='centered')

st.markdown(
    """
    <style>
    body { background-color: #0d0d0d !important; color: #e0e0e0 !important; }
    .stButton>button {
        background-color: #caa53b !important;
        color: black !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
    }
    .stTextInput>div>div>input {
        background-color: #1a1a1a;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

st.image("logo.png", width=200)
st.title("HustlerMob – Kein Tool. Eine Haltung.")

st.markdown("""
**Reagiere digital auf analoge Einschüchterung.**  
Lade dein Dokument hoch und erhalte einen passenden Antworttext – direkt, gezielt, selbst.
""")

uploaded_file = st.file_uploader("📄 Dokument hochladen (PDF, JPG, PNG)", type=["pdf", "jpg", "jpeg", "png"])


tone = st.radio(
    "🎙️ Wähle den Tonfall deiner Antwort:",
    ["Sachlich (kostenlos)", "Bestimmt (Pro)", "Eskalation (Pro)"],
    index=0,
    disabled=False
)

if st.button("Antwort generieren"):

    if not uploaded_file:
        st.error("Bitte lade zuerst ein Dokument hoch.")
    else:
        with st.spinner("Analysiere dein Dokument..." if tone.startswith("Sachlich") else "Pro-Funktion wird geladen..."):
            st.markdown("""---""")
            st.subheader("📬 Deine Antwort:")
            st.code("""
WIDERSPRUCH

Sehr geehrte Damen und Herren,

hiermit lege ich gegen Ihren Bescheid vom [Datum des Schreibens], Aktenzeichen [Aktenzeichen], fristgerecht Widerspruch ein.

Begründung:
Der von Ihnen dargestellte Sachverhalt ist unvollständig und die daraus gezogenen Schlussfolgerungen sind rechtlich nicht haltbar. Insbesondere die Anwendung von § [relevanter Paragraph] des [relevantes Gesetzbuch] ist in diesem Fall nicht zutreffend, da [kurze, klare Begründung].

Ich fordere Sie auf, den Sachverhalt unter Berücksichtigung der von mir eingereichten Unterlagen erneut zu prüfen und den angefochtenen Bescheid vollumfänglich aufzuheben.

Eine detaillierte Begründung erfolgt nach Akteneinsicht. Bitte bestätigen Sie mir den Eingang dieses Widerspruchs schriftlich.

Mit freundlichen Grüßen,

[Ihr Name]
""", language="text")
            st.success("Text generiert. Du kannst ihn nun kopieren oder anpassen.")
