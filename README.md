# 🌦️ Weather Rain Prediction

A machine learning project that predicts whether it will rain tomorrow using historical Australian weather data.

## 📌 Project Overview

The goal of this project is to build a machine learning model that predicts the target variable `RainTomorrow` based on weather conditions such as temperature, rainfall, humidity, pressure, and wind information.

The project includes data preprocessing, exploratory analysis, model training, evaluation, threshold optimization, feature importance analysis, and a Streamlit web application.

## 🎯 Objective

Predict:

- **Yes** → Rain tomorrow
- **No** → No rain tomorrow

## 📊 Dataset

The project uses the Australian weather dataset containing historical observations from multiple locations.

The target variable is:
RainTomorrow

## The dataset contains weather information including:

Minimum and maximum temperature
Rainfall
Wind speed
Wind direction
Humidity
Atmospheric pressure
Temperature at 9am and 3pm
RainToday
Location
Date

## 🔧 Data Preprocessing

**The following preprocessing steps were performed:**

Missing-value handling
Date conversion
Extraction of:
Year
Month
Day
Categorical feature encoding using one-hot encoding
Separation of features (X) and target (y)
Train-test split
Model training and evaluation

After preprocessing, the model uses **109** input features.

## 🤖 Models
Different machine learning experiments were performed, including:
Logistic Regression
Random Forest
The Random Forest model provided the best overall performance for the final application.

## 🖥️ Streamlit Application
A Streamlit web application was developed to allow users to enter weather conditions and receive a prediction.
The application provides:
Location selection
Temperature inputs
Rainfall
Wind information
Humidity
Atmospheric pressure
Wind directions
RainToday
Date
Rain probability
Rain/No-Rain prediction
Reset button
Model performance information
