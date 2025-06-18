
def generate_content(topic, tone):
    caption = f"This is a {tone.lower()} caption for: {topic}"
    hashtags = ["#trending", "#growth", "#InstaPilot"]
    cta = "Tap the link in bio to learn more!"
    return {"caption": caption, "hashtags": hashtags, "cta": cta}
