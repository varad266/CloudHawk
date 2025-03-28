import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st
import matplotlib.pyplot as plt
import time

# 🔹 Load Firebase credentials
cred = credentials.Certificate("cloudhawk-firebase.json")
firebase_admin.initialize_app(cred)

# 🔹 Firestore database reference
db = firestore.client()

# 🔹 Streamlit page configuration
st.set_page_config(page_title="Cloud Hawk AI - Real-Time Monitoring", layout="wide")
st.title("🚀 Cloud Hawk AI - Real-Time System Monitoring and Alert System")

# Function to fetch data from Firestore
def fetch_firestore_data():
    collection_ref = db.collection("system_metrics")
    docs = collection_ref.stream()

    data = []
    for doc in docs:
        record = doc.to_dict()
        record["client_id"] = doc.id  # Ensure client_id is included
        data.append(record)

    return pd.DataFrame(data) if data else None

# Initialize an empty DataFrame for real-time updates
live_df = pd.DataFrame()

# Live graph setup
fig, ax = plt.subplots()
st.pyplot(fig)

# Load or train the AI model
try:
    model = joblib.load("cloudhawk_ai_model.pkl")
    st.sidebar.success("✅ Loaded pre-trained AI model!")
except:
    st.sidebar.warning("⚠ No pre-trained model found. Training a new model...")

    # Fetch initial data for training
    initial_df = fetch_firestore_data()

    if initial_df is not None and not initial_df.empty:
        # Add outage label (1 = outage, 0 = normal)
        initial_df["outage"] = ((initial_df["cpu_usage"] > 85) |
                                (initial_df["ram_usage"] > 90) |
                                (initial_df["disk_usage"] > 95)).astype(int)

        # Features and target
        features = ["cpu_usage", "ram_usage", "disk_usage"]
        target = "outage"

        X = initial_df[features]
        y = initial_df[target]

        # Train-Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Model Training
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Model Accuracy
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        st.sidebar.write(f"🎯 Model Accuracy: {accuracy * 100:.2f}%")

        # Save trained model
        joblib.dump(model, "cloudhawk_ai_model.pkl")
        st.sidebar.success("✅ New AI model trained and saved as cloudhawk_ai_model.pkl!")

    else:
        st.sidebar.error("⚠ No data found in Firestore! Please ensure system monitoring is running.")

# Real-time monitoring
st.subheader("📊 Real-Time System Monitoring")
placeholder = st.empty()

try:
    while True:
        # Fetch live data from Firestore
        live_df = fetch_firestore_data()

        if live_df is not None and not live_df.empty:
            live_df["outage"] = ((live_df["cpu_usage"] > 85) |
                                (live_df["ram_usage"] > 90) |
                                (live_df["disk_usage"] > 95)).astype(int)

            # Features for prediction
            features = ["cpu_usage", "ram_usage", "disk_usage"]
            X_live = live_df[features]

            # Real-time predictions
            predictions = model.predict(X_live)
            live_df["prediction"] = predictions

            # Display real-time data
            with placeholder.container():
                st.write(live_df.tail(10))

                # Update live graph
                ax.clear()
                ax.plot(live_df["timestamp"], live_df["cpu_usage"], label="CPU Usage (%)", color="blue")
                ax.plot(live_df["timestamp"], live_df["ram_usage"], label="RAM Usage (%)", color="green")
                ax.plot(live_df["timestamp"], live_df["disk_usage"], label="Disk Usage (%)", color="red")
                ax.legend(loc="upper right")
                ax.set_xlabel("Timestamp")
                ax.set_ylabel("Usage (%)")
                ax.set_title("Real-Time System Monitoring")
                st.pyplot(fig)

        time.sleep(5)  # Fetch data every 5 seconds

except Exception as e:
    st.error(f"⚠ Error: {e}")
