import joblib
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# 🔹 Load Firebase credentials
cred = credentials.Certificate("cloudhawk-firebase.json")
firebase_admin.initialize_app(cred)

# 🔹 Firestore database reference
db = firestore.client()

# 🔹 Load the trained AI model
model = joblib.load("cloudhawk_ai_model.pkl")

# Function to fetch the latest system metrics
def fetch_latest_metrics():
    collection_ref = db.collection("system_metrics")
    docs = collection_ref.order_by("timestamp", direction=firestore.Query.DESCENDING).limit(1).stream()

    data = []
    for doc in docs:
        record = doc.to_dict()
        record["client_id"] = doc.id  # Ensure client_id is included
        data.append(record)

    return pd.DataFrame(data) if data else None

# 🔹 Fetch latest system data
latest_data = fetch_latest_metrics()

if latest_data is None or latest_data.empty:
    print("⚠ No recent system data found in Firestore!")
else:
    # 🔹 Select relevant features
    X_new = latest_data[["cpu_usage", "ram_usage", "disk_usage"]]

    # 🔹 Make prediction
    prediction = model.predict(X_new)[0]
    print("🚨 Predicted System Status:", "⚠ Outage Expected!" if prediction == 1 else "✅ System Stable")

    # 🔹 Store Prediction in Firestore
    latest_data["predicted_outage"] = int(prediction)
    db.collection("system_predictions").document(latest_data["client_id"].iloc[0]).set(latest_data.to_dict("records")[0])
    print("✅ Prediction stored in Firestore!")
