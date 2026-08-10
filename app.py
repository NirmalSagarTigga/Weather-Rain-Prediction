import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load model and saved files
# -----------------------------

st.title("🌦️ Weather Rain Prediction")

st.write("Predict whether it will rain tomorrow using Machine Learning.")


model = joblib.load("rain_prediction_random_forest.pkl")
threshold = joblib.load("rain_prediction_threshold.pkl")
features = joblib.load("rain_prediction_features.pkl")

# -----------------------------
# Weather Information
# -----------------------------

st.header("🌤️ Weather Information")

location = st.selectbox(
    "Location",
    [
        "Sydney",
        "Melbourne",
        "Brisbane",
        "Perth",
        "Adelaide",
        "Canberra",
        "Darwin",
        "Hobart",
        "Cairns",
        "Townsville"
    ]
)

col1, col2 = st.columns(2)

with col1:
    min_temp = st.number_input(
        "Minimum Temperature (°C)",
        value=15.0
    )

with col2:
    max_temp = st.number_input(
        "Maximum Temperature (°C)",
        value=25.0
    )

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    value=2.0
)

# -----------------------------
# Wind
# -----------------------------

st.subheader("💨 Wind Information")

col1, col2 = st.columns(2)

with col1:
    wind_gust_speed = st.number_input(
        "Wind Gust Speed (km/h)",
        min_value=0.0,
        value=35.0
    )

with col2:
    wind_speed_9am = st.number_input(
        "Wind Speed 9am (km/h)",
        min_value=0.0,
        value=15.0
    )

wind_speed_3pm = st.number_input(
    "Wind Speed 3pm (km/h)",
    min_value=0.0,
    value=20.0
)

# -----------------------------
# Humidity
# -----------------------------

st.subheader("💧 Humidity")

col1, col2 = st.columns(2)

with col1:
    humidity_9am = st.number_input(
        "Humidity 9am (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

with col2:
    humidity_3pm = st.number_input(
        "Humidity 3pm (%)",
        min_value=0.0,
        max_value=100.0,
        value=65.0
    )

# -----------------------------
# Pressure
# -----------------------------

st.subheader("🌡️ Pressure")

col1, col2 = st.columns(2)

with col1:
    pressure_9am = st.number_input(
        "Pressure 9am (hPa)",
        value=1015.0
    )

with col2:
    pressure_3pm = st.number_input(
        "Pressure 3pm (hPa)",
        value=1012.0
    )

# -----------------------------
# Temperature
# -----------------------------

st.subheader("🌡️ Temperature")

col1, col2 = st.columns(2)

with col1:
    temp_9am = st.number_input(
        "Temperature 9am (°C)",
        value=18.0
    )

with col2:
    temp_3pm = st.number_input(
        "Temperature 3pm (°C)",
        value=24.0
    )
# -----------------------------
# Wind Directions
# -----------------------------

st.subheader("🧭 Wind Directions")

wind_directions = [
    "N", "NNE", "NE", "ENE",
    "E", "ESE", "SE", "SSE",
    "S", "SSW", "SW", "WSW",
    "W", "WNW", "NW", "NNW"
]

col1, col2 = st.columns(2)

with col1:
    wind_gust_dir = st.selectbox(
        "Wind Gust Direction",
        wind_directions
    )

with col2:
    wind_dir_9am = st.selectbox(
        "Wind Direction 9am",
        wind_directions
    )

wind_dir_3pm = st.selectbox(
    "Wind Direction 3pm",
    wind_directions
)

# -----------------------------
# Rain Today
# -----------------------------

st.subheader("🌧️ Today's Rain")

rain_today_text = st.selectbox(
    "Did it rain today?",
    ["No", "Yes"]
)

rain_today = 1 if rain_today_text == "Yes" else 0

# -----------------------------
# Date
# -----------------------------

st.subheader("📅 Date")

col1, col2, col3 = st.columns(3)

with col1:
    year = st.number_input(
        "Year",
        min_value=2007,
        max_value=2025,
        value=2017,
        step=1
    )

with col2:
    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=6,
        step=1
    )

with col3:
    day = st.number_input(
        "Day",
        min_value=1,
        max_value=31,
        value=15,
        step=1
    )
# -----------------------------
# Prediction
# -----------------------------

st.header("🔮 Prediction")

if st.button("Predict Rain Tomorrow"):

    # Create an empty row containing all 109 features
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=features
    )

    # Fill numerical features
    input_data["MinTemp"] = min_temp
    input_data["MaxTemp"] = max_temp
    input_data["Rainfall"] = rainfall
    input_data["WindGustSpeed"] = wind_gust_speed
    input_data["WindSpeed9am"] = wind_speed_9am
    input_data["WindSpeed3pm"] = wind_speed_3pm
    input_data["Humidity9am"] = humidity_9am
    input_data["Humidity3pm"] = humidity_3pm
    input_data["Pressure9am"] = pressure_9am
    input_data["Pressure3pm"] = pressure_3pm
    input_data["Temp9am"] = temp_9am
    input_data["Temp3pm"] = temp_3pm
    input_data["RainToday"] = rain_today

    # Date features
    input_data["Year"] = year
    input_data["Month"] = month
    input_data["Day"] = day

    # One-hot encoded Location
    location_column = "Location_" + location

    if location_column in input_data.columns:
        input_data[location_column] = 1

    # One-hot encoded Wind Gust Direction
    gust_column = "WindGustDir_" + wind_gust_dir

    if gust_column in input_data.columns:
        input_data[gust_column] = 1

    # One-hot encoded Wind Direction 9am
    dir9_column = "WindDir9am_" + wind_dir_9am

    if dir9_column in input_data.columns:
        input_data[dir9_column] = 1

    # One-hot encoded Wind Direction 3pm
    dir3_column = "WindDir3pm_" + wind_dir_3pm

    if dir3_column in input_data.columns:
        input_data[dir3_column] = 1

    # Get probability of rain
    probability = model.predict_proba(input_data)[0][1]

    # Apply our selected threshold
    prediction = "Yes" if probability >= threshold else "No"

    # Display result
    st.subheader("🌦️ Prediction Result")

    st.metric(
        "Rain Probability",
        f"{probability:.1%}"
    )

    if prediction == "Yes":
        st.error("🌧️ Rain is likely tomorrow!")
    else:
        st.success("☀️ Rain is unlikely tomorrow!")

# -----------------------------
# Reset
# -----------------------------

st.divider()

if st.button("🔄 Reset", use_container_width=True):
    st.rerun()
# -----------------------------
# About the Model
# -----------------------------

st.divider()

st.subheader("📊 About the Model")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Model", "Random Forest")

with col2:
    st.metric("Accuracy", "85.19%")

with col3:
    st.metric("ROC-AUC", "0.876")

with col4:
    st.metric("Features", "109")

st.write("**Decision Threshold:** 0.35")

st.write("**Most Important Feature:** Humidity3pm")