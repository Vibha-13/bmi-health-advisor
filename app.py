import streamlit as st
import pandas as pd

# Title of the app
st.title("BMI Calculator & Health Advisor")

# Input fields
weight = st.number_input("Enter your weight (in kg):", min_value=1.0)
height = st.number_input("Enter your height (in meters):", min_value=0.1)

# BMI calculation
if height > 0:   
    bmi = weight / (height * height)
    st.write(f"Your BMI is: {bmi:.2f}")
    
    # Progress bar showing BMI level
    progress = int(bmi)  # We can use BMI as the scale for progress bar
    st.progress(progress / 40)  # Adjusting scale for a more visual result
    
    # Health advice with emojis and tips
    if bmi < 18.5:
        st.write("You are underweight. 🏃‍♂️💪")
        st.write("**Health Tips:**")
        st.write("1. Increase calorie intake with healthy foods.")
        st.write("2. Focus on strength training exercises.")
        st.write("3. Get enough sleep for recovery.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a healthy weight. 😊🌱")
        st.write("**Health Tips:**")
        st.write("1. Maintain a balanced diet.")
        st.write("2. Stay active with regular exercises.")
        st.write("3. Keep up your healthy lifestyle!")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight. ⚠️")
        st.write("**Health Tips:**")
        st.write("1. Reduce sugary and fried foods.")
        st.write("2. Try 30 minutes of walking daily.")
        st.write("3. Get at least 7–8 hours of sleep.")
    else:
        st.write("You are obese. 🚨")
        st.write("**Health Tips:**")
        st.write("1. Consult a healthcare provider for a plan.")
        st.write("2. Focus on reducing calorie intake.")
        st.write("3. Incorporate more cardio and strength training exercises.")

# Load dataset for BMI category distribution
df = pd.read_csv('your_dataset.csv')

# ——— BMI Category Chart ———
st.subheader("📊 BMI Category Distribution")

# Automatically find the BMI-category column
bmi_col = None
for col in df.columns:
    low = col.lower().replace(" ", "")
    if "bmi" in low and "class" in low:
        bmi_col = col
        break

if bmi_col:
    st.write(f"Using column: **{bmi_col}**")
    counts = df[bmi_col].value_counts()
    st.bar_chart(counts)
else:
    st.error("Couldn’t find a BMI-category column (looking for name containing “bmi”+“class”).")
.
