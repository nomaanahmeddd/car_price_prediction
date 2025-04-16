import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load("car_price_model.pkl")

st.title("🚗 Car Price Prediction App")

# Sample inputs - make sure these match your features
engine_size = st.slider("Engine Size", 60, 300, 130)
horsepower = st.slider("Horsepower", 50, 300, 100)
curb_weight = st.slider("Curb Weight (kg)", 1500, 4000, 2500)
width = st.slider("Car Width (inches)", 60, 80, 66)
city_mpg = st.slider("City MPG", 10, 60, 30)

# Create a DataFrame with user inputs
input_df = pd.DataFrame({
    'engine-size': [engine_size],
    'horsepower': [horsepower],
    'curb-weight': [curb_weight],
    'width': [width],
    'city-mpg': [city_mpg],
    # Add other required features with default or dummy values
})

# Fill in missing columns if needed
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0

# Predict
input_dict = {
    'engine-size': engine_size,
    'horsepower': horsepower,
    'curb-weight': curb_weight,
    'width': width,
    'city-mpg': city_mpg,
}

# Create DataFrame
input_df = pd.DataFrame([input_dict])

# Ensure all features from training are present
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0  # or use mean/median if you want more accuracy

# Reorder columns to match training set
input_df = input_df[model.feature_names_in_]

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Car Price: ${round(prediction, 2)}")
