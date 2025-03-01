import streamlit as st
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Streamlit App Title
st.title("Student Exam Performance Indicator")

# Form for user input
with st.form("student_form"):
    st.write("### Student Exam Performance Prediction")

    # Input fields
    gender = st.selectbox("Gender", ["Select your Gender", "male", "female"])
    ethnicity = st.selectbox("Race or Ethnicity", ["Select Ethnicity", "group A", "group B", "group C", "group D", "group E"])
    parental_level_of_education = st.selectbox("Parental Level of Education", [
        "Select Parent Education", "associate's degree", "bachelor's degree", "high school", "master's degree", "some college", "some high school"
    ])
    lunch = st.selectbox("Lunch Type", ["Select Lunch Type", "free/reduced", "standard"])
    test_preparation_course = st.selectbox("Test Preparation Course", ["Select Test_course", "none", "completed"])
    reading_score = st.number_input("Reading Score out of 100", min_value=0, max_value=100)
    writing_score = st.number_input("Writing Score out of 100", min_value=0, max_value=100)

    # Submit button
    submitted = st.form_submit_button("Predict your Maths Score")

# If the form is submitted
if submitted:
    # Validate inputs
    if (gender == "Select your Gender" or ethnicity == "Select Ethnicity" or 
        parental_level_of_education == "Select Parent Education" or lunch == "Select Lunch Type" or 
        test_preparation_course == "Select Test_course"):
        st.error("Please fill all the fields!")
    else:
        # Create CustomData object
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=float(reading_score),
            writing_score=float(writing_score)
        )

        # Convert data to DataFrame
        pred_df = data.get_data_as_data_frame()

        # Make prediction
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Display prediction
        st.success(f"The predicted Maths Score is: {results[0]}")