import streamlit as st
import pandas as pd
import time
import random

# Page setup
st.set_page_config(page_title="BMI & Health Advisor", layout="centered")

st.title("🧮 BMI Calculator & Health Advisor")

# Input
age = st.number_input("Enter your age", min_value=1, max_value=120)
height = st.number_input("Enter height (in cm)", min_value=50.0, max_value=250.0)
weight = st.number_input("Enter weight (in kg)", min_value=10.0, max_value=300.0)

# Calculate BMI
if height > 0:
    bmi = round(weight / ((height / 100) ** 2), 2)
    st.markdown(f"### 🧾 Your BMI is: `{bmi}`")

    # Determine category
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
        color = "green"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"

    st.markdown(f"<h3 style='color:{color};'>Category: {category}</h3>", unsafe_allow_html=True)

    # Balloon for Normal
    if category == "Normal":
        st.balloons()

    # ❤️ Heartbeat sound for Obese (autoplay + fallback)
    if category == "Obese":
        st.markdown("## 🚨 Health Alert!")
        st.markdown("""
            <audio autoplay>
                <source src="heartbeat-sound-effects-for-you-122458.mp3" type="audio/mpeg">
            </audio>
        """, unsafe_allow_html=True)
        st.audio("heartbeat-sound-effects-for-you-122458.mp3", start_time=0)
        st.markdown("⬆️ Click above if the sound didn’t auto-play.")

    # Doctor Advice
    st.markdown("## 👨‍⚕️ Doctor's Advice:")
    advice = {
        "Underweight": "Try to include more calories and protein-rich foods. Consult a nutritionist.",
        "Normal": "Great! Keep maintaining your healthy lifestyle.",
        "Overweight": "Consider a balanced diet and regular physical activity.",
        "Obese": "Seek professional medical advice and adopt a healthier routine ASAP."
    }
    st.info(advice[category])

    # Motivational Quotes Carousel
    st.markdown("## 🌟 Motivational Quotes")
    quotes = [
        "“Your body deserves the best.” 💪",
        "“Every healthy choice is a step toward a better you.” 🌱",
        "“Don't wish for it, work for it.” 🔥",
        "“It’s never too early or too late to work towards being the healthiest you.” 🧘‍♀️"
    ]

    idx = random.randint(0, len(quotes) - 1)
    st.success(quotes[idx])

    # Fun Fact
    st.markdown("### 🤓 Fun Fact")
    st.markdown(
        "Did you know? A BMI between 18.5 and 24.9 is linked to lower risks of heart disease and diabetes. "
        "Stay in the zone! 🎯"
    )

else:
    st.warning("Please enter a valid height to calculate BMI.")

