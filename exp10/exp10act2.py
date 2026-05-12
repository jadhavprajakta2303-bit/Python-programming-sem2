# Create a BMI health checker app.
"""
Created on Tue May 12 13:24:55 2026

@author: Prajakta Jadhav
"""
# BMI Health Result Calculator App using Streamlit

import streamlit as st

# Title
st.title("BMI Health Result Calculator")

# User Input
name = st.text_input("Enter Your Name")

weight = st.number_input("Enter Weight (kg)", min_value=1.0)

height = st.number_input("Enter Height (meters)", min_value=0.1)

# Calculate BMI
if st.button("Calculate BMI"):

    bmi = weight / (height ** 2)

    st.subheader(f"Hello {name}")

    st.write(f"Your BMI is: {bmi:.2f}")

    # BMI Result
    if bmi < 18.5:
        st.warning("Health Status: Underweight")

    elif bmi >= 18.5 and bmi < 24.9:
        st.success("Health Status: Normal Weight")

    elif bmi >= 25 and bmi < 29.9:
        st.warning("Health Status: Overweight")

    else:
        st.error("Health Status: Obese")
