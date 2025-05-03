import streamlit as st
import pandas as pd

# Title of the app
st.title("💪 BMI Calculator & Health Advisor")

# Load the CSV
try:
    df = pd.read_csv("bmi.csv")  # Load your dataset
    st.subheader("📋 Dataset Preview")
    st.write(df.head())           # Show first 5 rows
    st.write("**Columns in the dataset:**", df.columns.tolist())
except Exception as e:
    st.error(f"❌ Error loading dataset: {e}")
    st.stop()

# Identify the BMI category column
bmi_cat_col = None
for col in df.columns:
    if "bmi" in col.lower() and "class" in col.lower():
        bmi_cat_col = col
        break

if not bmi_cat_col:
    st.error("❌ Could not find any column with 'bmi' and 'class' in its name.")
    st.stop()

# Show raw counts of the BMI class column
st.subheader(f"📊 Distribution of `{bmi_cat_col}`")
counts = df[bmi_cat_col].value_counts()
st.write("**Raw counts for each BMI category:**")
st.write(counts)  # Show raw counts

# Plot the bar chart
st.subheader(f"📈 Bar Chart of `{bmi_cat_col}`")
st.bar_chart(counts)

# BMI calculator
weight = st.number_input("Weight (kg):", min_value=1.0)
height = st.number_input("Height (m):", min_value=0.1)

if height > 0:
    bmi = weight / (height * height)
    st.write(f"**Your BMI is:** {bmi:.2f}")

    if bmi < 18.5:
        st.warning("Underweight 🍃")
    elif bmi < 25:
        st.success("Normal weight ✨")
    elif bmi < 30:
        st.info("Overweight ⚠️")
    else:
        st.error("Obese ❤️‍🩹")
