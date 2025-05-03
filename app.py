import streamlit as st
import pandas as pd
import time
import random

# ——— Page Config ———
st.set_page_config(page_title="BMI Calculator & Health Advisor", layout="centered")
st.title("💪 BMI Calculator & Health Advisor")

# ——— User Inputs ———
weight = st.number_input("Enter your weight (in kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (in meters):", min_value=0.1, step=0.01)

# ——— BMI Calculation & Animated Progress ———
if weight and height:
    bmi = weight / (height ** 2)
    st.markdown(f"### 📏 Your BMI is: **{bmi:.2f}**")

    # Smooth progress-bar animation
    bar = st.progress(0)
    target = int(min(bmi / 40, 1.0) * 100)
    for i in range(target + 1):
        time.sleep(0.01)
        bar.progress(i)

    # ——— Determine Category & Celebration ———
    if bmi < 18.5:
        category = "Underweight"
        st.warning("You are underweight. 🍃")
        st.snow()  # gentle snow effect
        tips = [
            "Include more calories from healthy fats & proteins.",
            "Eat smaller meals more frequently.",
            "Incorporate strength training."
        ]
    elif bmi < 25:
        category = "Normal"
        st.success("You have a normal weight. Great job! ✨")
        st.balloons()  # celebratory balloons
        tips = [
            "Maintain your balanced diet.",
            "Stay active with regular exercise.",
            "Keep drinking plenty of water."
        ]
    elif bmi < 30:
        category = "Overweight"
        st.info("You are overweight. ⚠️")
        tips = [
            "Reduce sugary & fried foods.",
            "Aim for 30 min of walking daily.",
            "Get 7–8 hours of sleep."
        ]
    else:
        category = "Obese"
        st.error("You are obese. ❤️‍🩹")
        tips = [
            "Consult a healthcare provider.",
            "Practice portion control.",
            "Start with low-impact exercises."
        ]

    # ——— Health Tips ———
    st.markdown("### 🩺 Health Tips")
    for tip in tips:
        st.write("•", tip)

    # ——— Motivational Quote ———
    quotes = [
        "“Take care of your body. It's the only place you have to live.”",
        "“A journey of a thousand miles begins with a single step.”",
        "“Small progress each day adds up to big results!”"
    ]
    st.markdown(f"**💬 Motivation:** *{random.choice(quotes)}*")

    # ——— BMI Class Distribution Chart ———
    st.markdown("---")
    st.subheader("📊 BMI Class Distribution in Dataset")

    try:
        df = pd.read_csv("bmi.csv")  # ensure this file is alongside app.py

        # Find the BMI-class column flexibly
        bmi_col = next(
            (c for c in df.columns if "bmi" in c.lower() and "class" in c.lower()),
            None
        )

        if bmi_col:
            counts = df[bmi_col].value_counts()
            st.write(f"Using column: **{bmi_col}**")
            st.bar_chart(counts)
        else:
            st.error("Couldn’t find a column with ‘bmi’+‘class’ in its name.")
    except FileNotFoundError:
        st.error("Dataset file `bmi.csv` not found. Please add it next to this script.")

