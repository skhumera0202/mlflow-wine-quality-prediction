# 🍷 Wine Quality Prediction with MLflow
![Python](https://img.shields.io/badge/Python-3.12-blue)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-orange)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-green)

> A machine learning project that predicts red wine quality and tracks experiments, parameters, metrics, and models using MLflow.

---

## ⭐ Project Highlights

- 🍷 Predicts wine quality using machine learning
- 🤖 Uses ElasticNet Regression
- 📊 Evaluates the model using MAE, RMSE, and R²
- 📈 Tracks experiments with MLflow
- ⚙️ Logs model parameters and metrics
- 💾 Logs the trained model
- 🐍 Built with Python, Pandas, NumPy and Scikit-learn

## 📌 Project Overview

This project uses Machine Learning to predict the quality of red wine based on its physicochemical properties.

The main goal is not only to train a Machine Learning model, but also to understand how **MLflow can be used to track experiments, parameters, metrics, and trained models**.

---

## 🎯 Objective

Build a Wine Quality Prediction model and track the complete Machine Learning experiment using MLflow.

This project covers:

- Data loading and exploration
- Data preparation
- Train-test splitting
- Model training
- Model evaluation
- MLflow experiment tracking
- Logging parameters and metrics
- Logging the trained model

---

## 📊 Dataset

The project uses the **Wine Quality Red** dataset.

The dataset contains physicochemical measurements of red wine, including:

- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol

**The target variable is:**

**Quality**

The dataset contains **1,599 records and 12 columns**.

---

## 🤖 Machine Learning Model

I used the **ElasticNet Regression** model from Scikit-learn.

### Model Parameters


alpha = 0.5
l1_ratio = 0.5

## 📊 Model Results

**The trained model was evaluated on the test dataset using three metrics:**

| Metric | Result |
|---|---:|
| MAE | 0.6189 |
| RMSE | 0.7628 |
| R² Score | 0.1096 |

### Metric Explanation

- **MAE (Mean Absolute Error):** Measures the average difference between predicted and actual wine quality.

- **RMSE (Root Mean Squared Error):** Measures prediction error and gives more weight to larger errors.

- **R² Score:** Indicates how much of the variation in wine quality is explained by the model.

## 📈 MLflow Experiment Tracking

MLflow was used to track the machine learning experiment.

**Experiment:**

Wine Quality Prediction

**Tracked Parameters:**

alpha = 0.5
l1_ratio = 0.5

**Tracked Metrics:**
MAE  = 0.6188630472
RMSE = 0.7627945217
R²   = 0.1096399918

The trained model was also logged in MLflow.

## 🖥️ MLflow UI

The experiment can be viewed using the MLflow UI.

**Run:**

mlflow ui

**Then open:**

http://127.0.0.1:5000

**In the MLflow dashboard, you can view:**

1. 📊 Experiment runs
2. ⚙️ Model parameters
3. 📈 Evaluation metrics
4. 🤖 Logged model
5. ⏱️ Run duration
6. 📄 Source file

## 📁 Project Structure
---
mlflow-project/
│
├── app.py
├── winequality-red.csv
├── README.md
├── mlflow.db
├── mlruns/
└── venv/
---

venv/ should normally be added to .gitignore and should not be uploaded to GitHub.

## ⚙️ Installation
**1. Clone the repository:**

git clone <YOUR-GITHUB-REPOSITORY-URL>

**2. Open the project folder:**

cd mlflow-project

**3. Create a virtual environment:**

py -3.12 -m venv venv

**4. Activate the virtual environment:**

**Windows PowerShell:**

.\venv\Scripts\Activate.ps1

**5. Install dependencies:**

pip install pandas numpy scikit-learn mlflow
▶️ Run the Project

**Run the Python application:**

python app.py

You should see the model training results in the terminal.

**Example:**

Model trained successfully!

MAE: 0.6188630472018415

RMSE: 0.762794521686023

R2: 0.10963999179642603

MLflow run completed!

## 📊 View MLflow Dashboard

**Start MLflow:**

mlflow ui

**Open:**

http://127.0.0.1:5000

**Select:**

Wine Quality Prediction

Then open the training run to view the parameters, metrics, and logged model.

## 💡 What I Learned

**Through this project, I practiced:**

- Data loading with Pandas
- Data preprocessing
- Train-test splitting
- Machine learning model training
- Model prediction
- Model evaluation
- MAE, RMSE and R² metrics
- MLflow experiment tracking
- Logging parameters and metrics
- Logging a machine learning model
- Viewing experiments through the MLflow UI

## 🚀 Future Improvements

**Some possible improvements for this project are:**

* Try different machine learning algorithms
* Compare multiple models
* Improve model performance
* Add data visualization
* Add feature importance analysis
* Create a prediction interface
* Deploy the trained model
* Add a simple web application

## 👩‍💻 Author

**Humera Shaikh**

Github:https://github.com/skhumera0202

This project was created as part of my machine learning and MLOps learning journey.

**⭐ If you found this project useful, feel free to explore the repository and share your feedback!**