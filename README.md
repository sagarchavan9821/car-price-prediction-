# car-price-prediction-
# 🚗 Ford Car Price Predictor

A Machine Learning web application that predicts the market value of used Ford cars based on their specific features and condition.

## 📌 Project Overview
Buying or selling a used car often involves a lot of uncertainty. This project uses a **Linear Regression** model trained on a dataset of thousands of Ford vehicles to provide data-driven price estimates. By analyzing variables like mileage, age, and engine size, the app helps users understand the fair market value of a vehicle instantly.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Analysis:** Pandas, Seaborn, Matplotlib
* **Machine Learning:** Scikit-Learn (Linear Regression, StandardScaler)
* **Web Framework:** Streamlit
* **Deployment:** Streamlit Cloud / GitHub

## 📂 Project Structure
* `ford.csv`: The raw dataset containing car details.
* `eda.py`: Standalone script for Exploratory Data Analysis and visualizations.
* `preprocessing.py`: Logic for data cleaning and One-Hot Encoding.
* `model.py`: Training script that splits data, scales features, and exports the model.
* `app.py`: The Streamlit code for the interactive web interface.
* `main.py`: The entry point for the local training pipeline.



## 📊 Performance
The model is evaluated using the **R² Score**, which measures how well the independent variables explain the variability of the car prices.
* **Current R² Score:** ~0.80+ (depending on training)

## 🚀 How to Run Locally
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/Sagar Chavan/Sagarchavan9821.git](https://github.com/Sagarchavan/sagarchavan9821.git)
