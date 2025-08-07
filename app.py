import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from treatment import get_recommendations
from utils import load_and_preprocess
from gtts import gTTS
import base64
import os

st.set_page_config(page_title="🍃🌿 Plant Disease Detector", layout="centered")

# === Load GIF and Convert to Base64 ===
def get_base64_gif(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

gif_base64 = get_base64_gif("plant_disease_app/assets/bg.gif")

# === Voice Assistant ===
def speak_text(disease_name, rec, filename="plant_audio.mp3"):
    formatted_name = disease_name.replace('_', ' ')
    speech_text = (
        f"The detected disease is {formatted_name}. "
        f"Organic treatment: {rec['organic']}. "
        f"Chemical treatment: {rec['chemical']}. "
        f"Prevention tips: {rec['prevention']}."
    )
    tts = gTTS(text=speech_text, lang='en')
    tts.save(filename)
    with open(filename, "rb") as audio_file:
        audio_bytes = audio_file.read()
    b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
        <audio autoplay controls>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """
    return audio_html

# === Custom CSS with Background and Animations ===
st.markdown(f"""
    <style>
    .stApp {{
        background: url("data:image/gif;base64,{gif_base64}") no-repeat center center fixed;
        background-size: cover;
        color: black;
        font-family: 'Segoe UI', sans-serif;
    }}

    h1, h2, h3, .stMarkdown p {{
        color: black !important;
    }}

    .stButton>button {{
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
        transition: 0.3s;
    }}

    .stButton>button:hover {{
        background-color: #388E3C;
        transform: scale(1.05);
    }}

    @keyframes fall {{
        0% {{ transform: translateY(-100px) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(100vh) rotate(360deg); opacity: 0; }}
    }}

    @keyframes floatUp {{
        0% {{ transform: translateY(100vh); opacity: 1; }}
        100% {{ transform: translateY(-100vh); opacity: 0; }}
    }}

    .emoji {{
        position: fixed;
        font-size: 32px;
        z-index: 9999;
        animation: fall 12s linear infinite;
    }}

    .emoji-butterfly {{
        font-size: 28px;
        animation: floatUp 20s linear infinite;
    }}

    .emoji:nth-child(1) {{ left: 3%; animation-delay: 0s; }}
    .emoji:nth-child(2) {{ left: 10%; animation-delay: 2s; }}
    .emoji:nth-child(3) {{ left: 17%; animation-delay: 4s; }}
    .emoji:nth-child(4) {{ left: 24%; animation-delay: 6s; }}
    .emoji:nth-child(5) {{ left: 31%; animation-delay: 8s; }}
    .emoji:nth-child(6) {{ left: 38%; animation-delay: 1s; }}
    .emoji:nth-child(7) {{ left: 45%; animation-delay: 3s; }}
    .emoji:nth-child(8) {{ left: 52%; animation-delay: 5s; }}
    .emoji:nth-child(9) {{ left: 59%; animation-delay: 7s; }}
    .emoji:nth-child(10) {{ left: 66%; animation-delay: 9s; }}
    .emoji:nth-child(11) {{ left: 73%; animation-delay: 4s; }}
    .emoji:nth-child(12) {{ left: 80%; animation-delay: 6s; }}
    .emoji:nth-child(13) {{ left: 87%; animation-delay: 8s; }}
    .emoji:nth-child(14) {{ left: 94%; animation-delay: 2s; }}
    </style>

    <!-- Falling Leaves and Flying Emojis -->
    <div class="emoji">🍃</div>
    <div class="emoji">🍂</div>
    <div class="emoji">🍁</div>
    <div class="emoji">🌿</div>
    <div class="emoji">🌱</div>
    <div class="emoji">🍃</div>
    <div class="emoji">🍂</div>
    <div class="emoji">🍁</div>
    <div class="emoji">🌿</div>
    <div class="emoji">🌱</div>
    <div class="emoji emoji-butterfly">🦋</div>
    <div class="emoji emoji-butterfly">🦋</div>
    <div class="emoji emoji-butterfly">🦋</div>
    <div class="emoji emoji-butterfly">🦋</div>
""", unsafe_allow_html=True)

# === Load Model and Classes ===
model = load_model("plant_disease_app/model/plant_disease_model.keras")
with open("plant_disease_app/model/classes.txt", "r") as f:
    class_names = f.read().splitlines()

# === Main Interface ===
st.title("🌿 Plant Disease Detector")
st.markdown("Upload a plant leaf image to detect disease and get organic and chemical treatment suggestions.")

uploaded_file = st.file_uploader("📷 Upload a leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with st.spinner("🌿 Analyzing your plant..."):
        st.image(uploaded_file, caption="🌿 Uploaded Leaf Image", use_container_width=True)
        img = load_and_preprocess(uploaded_file)
        prediction = model.predict(img)
        class_index = np.argmax(prediction)
        confidence = prediction[0][class_index]

        if confidence < 0.7:
            st.subheader("⚠️ Unable to confidently detect disease")
            st.warning("The uploaded image doesn't match any known disease confidently. Please upload a clearer leaf image.")
        else:
            disease_name = class_names[class_index]
            rec = get_recommendations(disease_name)

            # === Results ===
            formatted_name = disease_name.replace('_', ' ')
            st.subheader(f"🦠 Detected Disease: {formatted_name}")

            st.markdown("### 🌱 Organic Treatment")
            st.markdown(f"<div style='color:black'>{rec['organic']}</div>", unsafe_allow_html=True)

            st.markdown("### 💊 Chemical Treatment")
            st.markdown(f"<div style='color:black'>{rec['chemical']}</div>", unsafe_allow_html=True)

            st.markdown("### 🛡️ Prevention Tips")
            st.markdown(f"<div style='color:black'>{rec['prevention']}</div>", unsafe_allow_html=True)

            # === Voice Assistant Button ===
            if st.button("🔊 Speak Diagnosis"):
                audio_html = speak_text(disease_name, rec)
                st.markdown(audio_html, unsafe_allow_html=True)

