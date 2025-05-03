import streamlit as st

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
        st.warning("You are underweight. 🍃")
        st.markdown("- Try eating nutrient-rich foods.")
        st.markdown("- Include healthy fats and proteins.")
        st.markdown("- Consider speaking to a dietitian.")

    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight. Great job! ✨")
        st.markdown("- Keep maintaining a balanced diet.")
        st.markdown("- Stay active with regular exercises.")
        st.markdown("- Drink plenty of water.")

    elif 25 <= bmi < 29.9:
        st.info("You are overweight. ⚠️")
        st.markdown("- Reduce sugary and fried foods.")
        st.markdown("- Try 30 minutes of walking daily.")
        st.markdown("- Get at least 7–8 hours of sleep.")

    else:
        st.error("You are obese. ❤️‍🩹")
        st.markdown("- Consult a healthcare provider.")
        st.markdown("- Focus on portion control.")
        st.markdown("- Start with low-impact exercises.")
