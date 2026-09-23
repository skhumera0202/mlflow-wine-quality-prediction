import pandas as pd
import mlflow

from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load dataset
data = pd.read_csv("data/winequality-red.csv", sep=";")


# Separate features and target
X = data.drop("quality", axis=1)
y = data["quality"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Model parameters
alpha = 0.5
l1_ratio = 0.5


# Create model
model = ElasticNet(
    alpha=alpha,
    l1_ratio=l1_ratio,
    random_state=42
)


# Train model
model.fit(X_train, y_train)


# Predictions
predictions = model.predict(X_test)


# Calculate metrics
mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)


# MLflow experiment
mlflow.set_experiment("Wine Quality Prediction")

with mlflow.start_run():

    # Log parameters
    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ratio", l1_ratio)

    # Log metrics
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2", r2)

    # Log model
    mlflow.sklearn.log_model(model, "model")


# Print results
print("Model trained successfully!")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)
print("MLflow run completed!")