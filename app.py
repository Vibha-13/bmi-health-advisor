import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="BMI Calculator & Health Advisor", layout="centered")

st.title("💪 BMI Calculator & Health Advisor")

# Input fields
weight = st.number_input("Enter your weight (in kg):", min_value=1.0)
height = st.number_input("Enter your height (in meters):", min_value=0.1)

# BMI calculation
if height > 0:
    bmi = weight / (height * height)
    st.write(f"### 📏 Your BMI is: `{bmi:.2f}`")

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    st.write(f"### 🧠 You are: **{category}**")

    # Progress bar showing BMI level
    st.progress(min(bmi / 40, 1.0))  # cap at 1.0 to avoid overfill

    # Tips dictionary
    tips = {
        "Underweight": [
            "Include more calories from healthy fats and proteins.",
            "Consider eating more frequently.",
            "Include strength training exercises."
        ],
        "Normal": [
            "Keep up your balanced diet!",
            "Continue regular physical activity.",
            "Stay hydrated and sleep well."
        ],
        "Overweight": [
            "Reduce sugary and fried foods.",
            "Try 30 minutes of walking daily.",
            "Get at least 7–8 hours of sleep."
        ],
        "Obese": [
            "Consult a nutritionist for a meal plan.",
            "Start with light exercises regularly.",
            "Avoid processed and high-calorie foods."
        ]
    }

    st.markdown("### 🩺 Doctor's Advice")
    for tip in tips[category]:
        st.write("•", tip)

    # Fun BMI category bar chart
    data = {
        'Category': ['Underweight', 'Normal', 'Overweight', 'Obese'],
        'Emoji': ['🦴', '💚', '⚠️', '🚨'],
        'Count': [1 if category == cat else 0 for cat in ['Underweight', 'Normal', 'Overweight', 'Obese']]
    }
    df = pd.DataFrame(data)

    st.markdown("### 📊 Your BMI Category")

    fig, ax = plt.subplots(figsize=(6, 3))
    sns.barplot(data=df, x='Category', y='Count', hue='Emoji', dodge=False, palette='Blues')
    plt.xlabel("BMI Category")
    plt.ylabel("")
    plt.yticks([])
    plt.title("You fall into this category 👇")
    st.pyplot(fig)

else:
    st.warning("Please enter a valid height to calculate BMI.")

