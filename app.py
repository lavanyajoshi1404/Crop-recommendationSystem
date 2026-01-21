import streamlit as st
import pickle
import numpy as np

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# ------------------ Load Model ------------------
model = pickle.load(open("crop_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# ------------------ Title Section ------------------
st.markdown(
    "<h1 style='text-align: center;'>🌾 Crop Recommendation System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Machine Learning based crop suggestion using soil & climate data</p>",
    unsafe_allow_html=True
)

st.divider()

# ------------------ Sidebar Inputs ------------------
st.sidebar.header("🌱 Soil Parameters")

N = st.sidebar.number_input("Nitrogen (N)", 0, 200, 50)
P = st.sidebar.number_input("Phosphorus (P)", 0, 200, 50)
K = st.sidebar.number_input("Potassium (K)", 0, 200, 50)

st.sidebar.header("🌦 Climate Parameters")

temperature = st.sidebar.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.sidebar.number_input("Humidity (%)", 0.0, 100.0, 70.0)
ph = st.sidebar.number_input("pH Value", 0.0, 14.0, 6.5)
rainfall = st.sidebar.number_input("Rainfall (mm)", 0.0, 500.0, 200.0)

# ------------------ Main Layout ------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Entered Values Overview")
    st.metric("🌡 Temperature (°C)", temperature)
    st.metric("💧 Humidity (%)", humidity)
    st.metric("🌧 Rainfall (mm)", rainfall)

with col2:
    st.subheader("🧪 Soil Health")
    st.metric("🌿 Nitrogen (N)", N)
    st.metric("🌾 Phosphorus (P)", P)
    st.metric("🍃 Potassium (K)", K)
    st.metric("⚗ pH Value", ph)

st.divider()

# ------------------ Prediction ------------------
st.subheader("🌱 Crop Recommendation")

if st.button("🚜 Recommend Best Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    crop = le.inverse_transform(prediction)

    st.success(f"✅ **Recommended Crop:** 🌾 **{crop[0]}**")
    st.balloons()

# ------------------ Info Section ------------------
st.info("""
🔍 **How it works**
- Uses Machine Learning (Logistic Regression)
- Trained on soil nutrients & climate conditions
- Helps farmers and researchers select suitable crops

📌 **Steps**
1. Enter soil and climate parameters
2. Click on *Recommend Best Crop*
3. Get instant crop suggestion
""")

# ------------------ Footer ------------------
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with ❤️ using Streamlit & Machine Learning</p>",
    unsafe_allow_html=True
)
