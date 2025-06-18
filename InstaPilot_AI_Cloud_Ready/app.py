
import streamlit as st
from components.campaign_builder import build_campaign
from components.tone_engine import generate_content
from components.offer_vault import load_offers
from components.monetization_strategy import suggest_strategy

st.set_page_config(page_title="InstaPilot AI", layout="centered")
st.title("📸 InstaPilot AI")
st.write("Create AI-powered Instagram/TikTok campaigns with monetization built-in.")

campaign = build_campaign()

if campaign:
    st.subheader("✍️ AI-Generated Content")
    content = generate_content(campaign["topic"], campaign["tone"])
    st.text_area("Caption", content["caption"], height=100)
    st.write("Hashtags:", ", ".join(content["hashtags"]))
    st.write("CTA:", content["cta"])

    st.subheader("📈 Monetization Strategy")
    st.write(suggest_strategy(campaign["niche"]))

    st.subheader("🎁 Offer Vault")
    offers = load_offers(campaign["niche"])
    st.selectbox("Choose an Offer:", offers)
