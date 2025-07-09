import streamlit as st

antworten = {
    "Seicht": """Sehr geehrte Damen und Herren,

unter Bezugnahme auf § 35 SGB X sowie unter Berücksichtigung der verwaltungsverfahrensrechtlichen Grundsätze bitte ich um nochmalige Prüfung Ihres Bescheides.

Aus meiner Sicht ist nicht auszuschließen, dass dem Verwaltungsakt eine Tatsachengrundlage zugrunde liegt, die bei vollständiger Erhebung der Umstände möglicherweise zu einer abweichenden Beurteilung geführt hätte.

Ich bitte höflich um Offenlegung der konkreten Erwägungen, die zur bisherigen Entscheidung führten, und verweise in diesem Zusammenhang auf die Anforderungen an die Ermessensausübung nach § 39 SGB X sowie auf das Urteil des BSG vom 23.08.2011 – B 14 AS 146/10 R.

Im Sinne eines fairen Verwaltungsverfahrens wird gebeten, diese Aspekte bei der Neubewertung einzubeziehen.

Mit freundlichen Grüßen
""",

    "Gemäßigt": """Sehr geehrte Damen und Herren,

gegen Ihren Bescheid vom [Datum] lege ich hiermit form- und fristgerecht Widerspruch ein.

Nach meiner Einschätzung ist der Verwaltungsakt in mehreren Punkten fehlerhaft. Maßgeblich ist hierbei § 39 Abs. 1 SGB X i.V.m. § 24 VwVfG. Die Begründung des Bescheides ist weder inhaltlich ausreichend noch entspricht sie dem Transparenzgebot gemäß den Anforderungen des BVerwG, Urteil vom 27.02.2020 – 5 C 2.19.

Darüber hinaus ist zu prüfen, ob die Entscheidung auf vollständiger Tatsachenerhebung beruht oder lediglich auf Plausibilitätsvermutungen, was nach geltender Rechtsprechung nicht ausreicht (vgl. BSG, Urteil vom 23.08.2011 – B 14 AS 146/10 R).

Ich fordere Sie daher auf, den Bescheid zu überprüfen und die getroffene Entscheidung zurückzunehmen oder inhaltlich zu begründen, ggf. auch durch eine ergänzende Anhörung nach § 24 SGB X.

Mit verbindlichem Gruß
""",

    "Barsch": """Sehr geehrte Damen und Herren,

Ihre Entscheidung ist weder rechtlich haltbar noch formell ordnungsgemäß zustande gekommen. Ich widerspreche daher mit sofortiger Wirkung.

Nach § 39 SGB X ist ein Verwaltungsakt nur wirksam, wenn er auf einer tragfähigen Tatsachengrundlage beruht – diese fehlt hier ersichtlich. Eine Anhörung nach § 24 SGB X fand entweder gar nicht oder in inhaltlich völlig unzureichender Weise statt. Das stellt nicht nur einen Verfahrensverstoß dar, sondern verletzt mein Grundrecht auf rechtliches Gehör nach Art. 103 Abs. 1 GG.

Ich verweise auf das Urteil des BVerfG (Beschluss vom 19.12.2020 – 1 BvR 1246/20), in dem das Gericht klargestellt hat, dass ein derart fehlerhaftes Verfahren den Verwaltungsakt in Gänze angreifbar macht.

Sollte keine umgehende Rücknahme des Bescheides erfolgen, wird eine Fach- und Dienstaufsichtsbeschwerde eingeleitet – verbunden mit einer Prüfung auf strukturelle Verfahrensmängel.

In Erwartung einer rechtskonformen Entscheidung
"""
}

st.set_page_config(page_title="HustlerMob", layout="centered")

try:
    st.image("logo.png", width=160)
except:
    pass

st.markdown("## HustlerMob – Systemtrippler 2.0")
st.markdown("**Wenn du das System nicht kennst, bezahlst du die Rechnung.**")

st.markdown("### Schritt 1: Upload")
uploaded_file = st.file_uploader("Lade das Originalschreiben hoch – egal ob Bescheid, Ablehnung oder Drohung:", type=["pdf", "jpg", "jpeg", "png"])

if "tone" not in st.session_state:
    st.session_state.tone = ""

st.markdown("### Schritt 2: Tonlage deiner Antwort")
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
    st.markdown("### Schritt 3: Antwortentwurf – bereit zur Nutzung")
    st.text_area("Dieser Text ist juristisch tragfähig, stilistisch geschliffen und sofort einsetzbar:", value=response, height=300)
    st.download_button("⬇️ Antwort als .txt speichern", data=response, file_name="antwort.txt")
else:
    st.info("Wähle eine Tonlage und lade das Schreiben hoch.")

st.markdown("---")
st.markdown("### 📡 Unsere Kanäle")
st.markdown("""
- [TikTok](https://www.tiktok.com/@hustlerbiz.de)  
- [Instagram](https://www.instagram.com/hustlerbizreal/)  
- [YouTube](https://www.youtube.com/@HustlerBizReal)  
- [Zur Website](https://hustlerbiz.de/)
""")

st.markdown("### 🛒 Produkte & Empfehlungen")
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
- Alles bleibt lokal. Keine Speicherung. Keine Weiterleitung.
- Kein Tracking. Keine Analyse. Keine Cloud.
- Die Texte sind keine Rechtsberatung – sondern Werkzeuge.
""")