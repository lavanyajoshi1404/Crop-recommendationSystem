# Crop-recommendation System
🌾 Machine Learning based Crop Recommendation System using Logistic Regression, deployed with Streamlit to suggest suitable crops based on soil nutrients and climate conditions.
# 🌾 Crop Recommendation System

A Machine Learning based web application that recommends the most suitable crop to grow based on soil nutrients and climate conditions.  
The model is trained using Logistic Regression and deployed using Streamlit for an interactive user experience.

---

## 📌 Problem Statement

Farmers often struggle to decide which crop to grow due to varying soil nutrients and climatic conditions.  
This project aims to solve that problem by using Machine Learning to recommend the best crop based on environmental factors.

---

## 📊 Dataset Used

- Crop Recommendation Dataset (CSV format)
- Features include:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH value
  - Rainfall
- Target:
  - Crop label

---

## 🧠 Machine Learning Approach

- Model Used: **Logistic Regression**
- Data Preprocessing:
  - Feature Scaling using StandardScaler
  - Label Encoding for crop labels
- Evaluation:
  - Model trained on processed dataset
  - Used for real-time predictions in the web app

---

## 🛠 Tech Stack

- **Programming Language:** Python
- **Libraries:**  
  - NumPy  
  - Pandas  
  - Scikit-learn  
- **Web Framework:** Streamlit
- **Version Control:** Git & GitHub

---

## 🖥 Web Application Features

- User-friendly Streamlit interface
- Sidebar input for soil and climate parameters
- Real-time crop recommendation
- Clean and interactive dashboard layout

---

## 📸 Project Screenshots

### Home Page
![Home Page](images/home.png)

### Crop Recommendation Result
![Result Page](images/result.png)

---

## 🚀 How to Run the Project Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crop-recommendation-system.git
