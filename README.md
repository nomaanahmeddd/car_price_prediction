# 🚗 Car Price Prediction App

This is a machine learning-powered web app built using **Streamlit** that predicts the price of a car based on its features like engine size, horsepower, weight, width, mileage, etc.

The model is trained on a cleaned and preprocessed dataset using **Random Forest Regressor**, which gave the best performance among several models tested. The app is designed to be lightweight, interactive, and easy to use.

---

## ✨ Features

- 🔍 Input car details to predict the estimated price
- 📊 Trained with data cleaning, feature engineering, and cross-validation
- 📈 Compares models like Random Forest, Gradient Boosting, and Linear Regression
- 🔢 Visualizes top 10 important features using permutation importance
- ⚙️ Deployable via Streamlit Cloud or locally
- 📁 Well-structured and beginner-friendly project

---

## 🧠 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Joblib

---

## 🚀 How to Run Locally


# 1. Clone the Repository

  git clone https://github.com/your-username/car-price-prediction.git
  cd car-price-prediction

# 2. Install Required Libraries
  pip install -r requirements.txt

# 3. Run the Streamlit App

  streamlit run app.py
## 📊 Model Performance Summary
| Model              | Cross-Validated R² | Test R²  | Test RMSE |
|-------------------|--------------------|----------|-----------|
| Random Forest      | 0.391              | 0.937    | 2579.07   |
| Gradient Boosting  | 0.481              | 0.936    | 2599.53   |
| Linear Regression  | 0.253              | 0.897    | 3282.77   |

📬 Contact
Author: Khaja Noman Ahmed
LinkedIn: [www.linkedin.com/in/khajanomanahmed]
