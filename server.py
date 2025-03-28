import firebase_admin
from firebase_admin import credentials, firestore
import time
import json

# Load Firebase credentials (use your actual path)
cred = credentials.Certificate("cloudhawk-firebase.json")
firebase_admin.initialize_app(cred)

# Firestore database reference
db = firestore.client()
collection_ref = db.collection("system_metrics")


# Function to monitor and display system metrics
def monitor_clients():
    while True:
        print("\nFetching latest system data...")
        docs = collection_ref.stream()

        for doc in docs:
            data = doc.to_dict()
            client_id = doc.id
            print(f"\n📌 Client: {client_id}")
            print(json.dumps(data, indent=2))

            # Alert for high usage
            if data['cpu_usage'] > 80 or data['ram_usage'] > 85:
                print(f"⚠ ALERT! High Usage Detected for {client_id}")

        time.sleep(5)  # Refresh every 5 seconds


# Run the function
if __name__ == "__main__":
    monitor_clients()
