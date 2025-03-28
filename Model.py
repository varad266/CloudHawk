import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 🔹 Load Data
df = pd.read_csv("system_metrics_labeled.csv")

# 🔹 Features & Target
X = df[["cpu_usage", "ram_usage", "disk_usage"]]
y = df["outage"]

# 🔹 Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🔹 Test Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# 🔹 Save Model
joblib.dump(model, "cloudhawk_ai_model.pkl")

