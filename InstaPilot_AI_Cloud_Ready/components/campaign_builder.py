
def build_campaign():
    import streamlit as st
    topic = st.text_input("Content Topic")
    tone = st.selectbox("Tone", ["Professional", "Witty", "Empathetic", "Sales-Driven", "Motivational"])
    platform = st.multiselect("Platform", ["Instagram", "TikTok"])
    niche = st.selectbox("Niche", ["Nursing", "Pets", "Mental Health", "Finance", "Veterans"])
    if topic:
        return {"topic": topic, "tone": tone, "platform": platform, "niche": niche}
    return None
