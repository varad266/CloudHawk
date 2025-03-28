import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# 🔹 Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("cloudhawk-firebase.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
collection_ref = db.collection("system_metrics")

# 🔹 Fetch Data
docs = collection_ref.stream()
data = [doc.to_dict() for doc in docs]
df = pd.DataFrame(data)

# 🔹 Convert Timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"], format="%H:%M:%S", errors="coerce")

# 🔹 Generate "Outage" Labels (Basic Rule-Based)
df["outage"] = ((df["cpu_usage"] > 90) & (df["ram_usage"] > 85)) | (df["disk_usage"] > 95)
df["outage"] = df["outage"].astype(int)  # Convert to 0 or 1

# 🔹 Save for AI Training
df.to_csv("system_metrics_labeled.csv", index=False)

print(df.head())  # Preview data
