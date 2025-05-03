import streamlit as st 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

st.set_page_config(page_title="BMI Calculator & Health Advisor", layout="centered")
st.title("💪 BMI Calculator & Health Advisor")

# User Input
weight = st.number_input("Enter your weight (in kg):", min_value=1.0, step=0.5)
height = st.number_input("Enter your height (in meters):", min_value=0.1, step=0.01)

if weight and height:
    bmi = round(weight / (height ** 2), 2)

    # Determine category
    if bmi < 18.5:
        category = "underweight"
        emoji = "🦴"
    elif 18.5 <= bmi < 25:
        category = "normal"
        emoji = "💚"
    elif 25 <= bmi < 30:
        category = "overweight"
        emoji = "⚠️"
    else:
        category = "obese"
        emoji = "❤️‍🩹"

    st.subheader(f"Your BMI is: {bmi}")
    st.markdown(f"You are **{category}**. {emoji}")

    # Horizontal progress bar
    st.progress(min(bmi / 40, 1.0))

    # Health tips
    st.subheader("💡 Health Tips")
    tips = {
        "underweight": [
            "Eat more frequently.",
            "Choose nutrient-rich foods.",
            "Try smoothies and shakes."
        ],
        "normal": [
            "Keep up the good work!",
            "Maintain a balanced diet.",
            "Stay active every day."
        ],
        "overweight": [
            "Reduce sugary and fried foods.",
            "Try 30 minutes of walking daily.",
            "Get at least 7–8 hours of sleep."
        ],
        "obese": [
            "Consult a healthcare provider.",
            "Focus on portion control.",
            "Start with low-impact exercises."
        ]
    }
    for tip in tips[category]:
        st.write(f"👉 {tip}")

    # BMI Category Chart
    st.subheader("📊 BMI Category Distribution")
    try:
        data = pd.read_csv("bmi.csv")
        if "bmi_class" in data.columns:
            fig, ax = plt.subplots()
            sns.countplot(data=data, x='bmi_class', palette="pastel", ax=ax)
            ax.set_title("BMI Class Counts")
            st.pyplot(fig)
        else:
            st.warning("📁 'bmi_class' column not found in the dataset.")
    except FileNotFoundError:
        st.error("CSV file not found. Please add 'bmi.csv' to your project folder.")

    # Motivational Quote
    st.subheader("🌟 Motivational Quote")
    quotes = [
        "Your body can do it. It's time to convince your mind.",
        "Fitness is not about being better than someone else. It’s about being better than you used to be.",
        "The groundwork of all happiness is health."
    ]
    st.success(random.choice(quotes))


