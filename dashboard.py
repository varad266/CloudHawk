# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials, firestore
# import pandas as pd
# import plotly.express as px
# import time
#
# # Initialize Firebase
# cred = credentials.Certificate("cloudhawk-firebase.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()
#
# st.set_page_config(page_title="CloudHawk Dashboard", layout="wide")
#
# st.title("🌐 CloudHawk - System Monitoring Dashboard")
#
#
# def fetch_data():
#     docs = db.collection("system_metrics").stream()
#     data = []
#
#     for doc in docs:
#         system_data = doc.to_dict()
#         system_data["client_id"] = doc.id
#         data.append(system_data)
#
#     return pd.DataFrame(data)
#
#
# # Streamlit Live Dashboard
# while True:
#     df = fetch_data()
#     if not df.empty:
#         st.subheader("🔍 System Metrics Overview")
#
#         col1, col2, col3 = st.columns(3)
#
#         with col1:
#             st.metric("💻 CPU Usage (%)", f"{df['cpu_usage'].mean():.2f} %")
#         with col2:
#             st.metric("🖥️ RAM Usage (%)", f"{df['ram_usage'].mean():.2f} %")
#         with col3:
#             st.metric("💾 Disk Usage (%)", f"{df['disk_usage'].mean():.2f} %")
#
#         st.subheader("📈 Live System Performance")
#
#         fig_cpu = px.line(df, x="timestamp", y="cpu_usage", color="client_id", title="CPU Usage Over Time")
#         fig_ram = px.line(df, x="timestamp", y="ram_usage", color="client_id", title="RAM Usage Over Time")
#         fig_disk = px.line(df, x="timestamp", y="disk_usage", color="client_id", title="Disk Usage Over Time")
#
#         st.plotly_chart(fig_cpu, use_container_width=True, key="cpu_chart")
#         st.plotly_chart(fig_ram, use_container_width=True, key="ram_chart")
#         st.plotly_chart(fig_disk, use_container_width=True, key="disk_chart")
#
#     time.sleep(5)  # Refresh every 5 seconds





# import streamlit as st
# import psutil
# import time
# import plotly.graph_objs as go
# import uuid  # For unique keys
#
# # Set Streamlit page configuration
# st.set_page_config(page_title="CloudHawk - System Monitoring", layout="wide")
#
# # Function to fetch system metrics
# def get_system_metrics():
#     return {
#         "cpu": psutil.cpu_percent(interval=1),
#         "ram": psutil.virtual_memory().percent,
#         "disk": psutil.disk_usage('/').percent
#     }
#
# # Function to create a Plotly chart
# def create_chart(metric_name, value, color):
#     fig = go.Figure(go.Indicator(
#         mode="gauge+number",
#         value=value,
#         title={'text': f"{metric_name} Usage (%)"},
#         gauge={'axis': {'range': [0, 100]}, 'bar': {'color': color}}
#     ))
#     return fig
#
# # Streamlit UI Layout
# st.title("🌐 CloudHawk - System Monitoring Dashboard")
#
# # Create placeholders for dynamic updates
# cpu_placeholder = st.empty()
# ram_placeholder = st.empty()
# disk_placeholder = st.empty()
#
# # Live System Performance Updates
# st.subheader("📈 Live System Performance")
#
# while True:
#     # Get current system metrics
#     metrics = get_system_metrics()
#
#     # Update CPU Usage Chart
#     with cpu_placeholder:
#         st.plotly_chart(create_chart("CPU", metrics["cpu"], "blue"), use_container_width=True)
#
#     # Update RAM Usage Chart
#     with ram_placeholder:
#         st.plotly_chart(create_chart("RAM", metrics["ram"], "green"), use_container_width=True)
#
#     # Update Disk Usage Chart
#     with disk_placeholder:
#         st.plotly_chart(create_chart("Disk", metrics["disk"], "red"), use_container_width=True)
#
#     time.sleep(2)  # Refresh every 2 seconds





# import streamlit as st
# import psutil
# import time
# import plotly.graph_objs as go
#
# # Set Streamlit page configuration
# st.set_page_config(page_title="CloudHawk - System Monitoring", layout="wide")
#
# # Function to fetch system metrics
# def get_system_metrics():
#     return {
#         "cpu": psutil.cpu_percent(interval=1),
#         "ram": psutil.virtual_memory().percent,
#         "disk": psutil.disk_usage('/').percent
#     }
#
# # Function to create a Plotly gauge chart
# def create_chart(metric_name, value, color):
#     return go.Figure(go.Indicator(
#         mode="gauge+number",
#         value=value,
#         title={'text': f"{metric_name} Usage (%)"},
#         gauge={'axis': {'range': [0, 100]}, 'bar': {'color': color}}
#     ))
#
# # Streamlit UI Layout
# st.title("🌐 CloudHawk - System Monitoring Dashboard")
# st.subheader("📈 Live System Performance")
#
# # Create placeholders for updating charts dynamically
# cpu_placeholder = st.empty()
# ram_placeholder = st.empty()
# disk_placeholder = st.empty()
#
# # Infinite loop for real-time updates
# while True:
#     # Get updated system metrics
#     metrics = get_system_metrics()
#
#     # Update the dashboard with new values
#     cpu_placeholder.plotly_chart(create_chart("CPU", metrics["cpu"], "blue"), use_container_width=True, key="cpu_chart")
#     ram_placeholder.plotly_chart(create_chart("RAM", metrics["ram"], "green"), use_container_width=True,key="ram_chart")
#     disk_placeholder.plotly_chart(create_chart("Disk", metrics["disk"], "red"), use_container_width=True, key="disk_chart")
#
#     # Sleep before the next update
#     time.sleep(2)

#Working dashboard below
# import streamlit as st
# import plotly.graph_objects as go
# import psutil
# import time
#
# # Initialize session state for unique keys
# if "cpu_chart_count" not in st.session_state:
#     st.session_state["cpu_chart_count"] = 0
# if "ram_chart_count" not in st.session_state:
#     st.session_state["ram_chart_count"] = 0
# if "disk_chart_count" not in st.session_state:
#     st.session_state["disk_chart_count"] = 0
#
#
# # Function to create a real-time usage chart
# def create_chart(name, values, color):
#     fig = go.Figure(data=[go.Scatter(y=values, mode='lines', line=dict(color=color))])
#     fig.update_layout(title=f"{name} Usage", xaxis_title="Time", yaxis_title="Usage (%)")
#     return fig
#
#
# # Streamlit title
# st.title("CloudHawk: System Monitoring Dashboard")
#
# # Initialize metrics data
# metrics = {
#     "cpu": [],
#     "ram": [],
#     "disk": []
# }
#
# # Create placeholders for updating charts
# cpu_placeholder = st.empty()
# ram_placeholder = st.empty()
# disk_placeholder = st.empty()
#
# # Real-time data update loop
# while True:
#     # Get system usage data
#     cpu_usage = psutil.cpu_percent(interval=1)
#     ram_usage = psutil.virtual_memory().percent
#     disk_usage = psutil.disk_usage('/').percent
#
#     # Append latest values
#     metrics["cpu"].append(cpu_usage)
#     metrics["ram"].append(ram_usage)
#     metrics["disk"].append(disk_usage)
#
#     # Keep only the last 50 data points for smooth visualization
#     metrics["cpu"] = metrics["cpu"][-50:]
#     metrics["ram"] = metrics["ram"][-50:]
#     metrics["disk"] = metrics["disk"][-50:]
#
#     # Update plots with unique keys to prevent Streamlit errors
#     cpu_placeholder.plotly_chart(
#         create_chart("CPU", metrics["cpu"], "blue"),
#         use_container_width=True,
#         key=f"cpu_chart_{st.session_state['cpu_chart_count']}"
#     )
#
#     ram_placeholder.plotly_chart(
#         create_chart("RAM", metrics["ram"], "green"),
#         use_container_width=True,
#         key=f"ram_chart_{st.session_state['ram_chart_count']}"
#     )
#
#     disk_placeholder.plotly_chart(
#         create_chart("Disk", metrics["disk"], "red"),
#         use_container_width=True,
#         key=f"disk_chart_{st.session_state['disk_chart_count']}"
#     )
#
#     # Increment session state counters to maintain unique keys
#     st.session_state["cpu_chart_count"] += 1
#     st.session_state["ram_chart_count"] += 1
#     st.session_state["disk_chart_count"] += 1
#
#     # Refresh every second
#     time.sleep(1)



# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials, firestore
# import pandas as pd
# import plotly.express as px
#
# # Initialize Firebase (Ensure the service account file is correct)
# cred = credentials.Certificate("cloudhawk-firebase.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()
#
# # Function to Fetch Data for All Systems
# def fetch_system_data():
#     docs = db.collection("system_usage").get()
#     data = []
#
#     for doc in docs:
#         record = doc.to_dict()
#         record["system_id"] = doc.id  # Assuming system ID is stored in Firestore
#         data.append(record)
#
#     return pd.DataFrame(data)
#
# # Load Data
# df = fetch_system_data()
#
# if df.empty:
#     st.error("No data found! Check Firestore collection.")
# else:
#     st.title("📊 CloudHawk System Monitoring Dashboard")
#
#     # List all unique systems
#     systems = df["system_id"].unique()
#
#     # Create a tab for each system
#     tab_list = st.tabs([f"🔹 {sys}" for sys in systems])
#
#     for i, system in enumerate(systems):
#         with tab_list[i]:
#             st.subheader(f"📡 Monitoring: {system}")
#
#             # Filter data for this system
#             sys_data = df[df["system_id"] == system]
#
#             # Create Plots
#             cpu_chart = px.line(sys_data, x="timestamp", y="cpu_usage", title="CPU Usage (%)", color_discrete_sequence=["blue"])
#             ram_chart = px.line(sys_data, x="timestamp", y="ram_usage", title="RAM Usage (%)", color_discrete_sequence=["green"])
#             disk_chart = px.line(sys_data, x="timestamp", y="disk_usage", title="Disk Usage (%)", color_discrete_sequence=["red"])
#
#             # Display Charts with Unique Keys
#             st.plotly_chart(cpu_chart, use_container_width=True, key=f"cpu_{system}")
#             st.plotly_chart(ram_chart, use_container_width=True, key=f"ram_{system}")
#             st.plotly_chart(disk_chart, use_container_width=True, key=f"disk_{system}")

# import streamlit as st
# import pandas as pd
# import firebase_admin
# from firebase_admin import credentials, firestore
# import time
# import matplotlib.pyplot as plt
#
# # 🔹 Load Firebase credentials
# if not firebase_admin._apps:
#     cred = credentials.Certificate("cloudhawk-firebase.json")
#     firebase_admin.initialize_app(cred)
#
# # 🔹 Firestore database reference
# db = firestore.client()
# collection_ref = db.collection("system_metrics")
#
#
# # 🔹 Function to fetch data from Firestore
# def fetch_data():
#     docs = collection_ref.stream()
#     data = [doc.to_dict() for doc in docs]
#
#     if not data:
#         return pd.DataFrame()  # Return empty DataFrame if no data
#
#     df = pd.DataFrame(data)
#
#     # 🔹 Ensure 'client_id' exists before filtering
#     if "client_id" not in df.columns:
#         st.error("⚠ Firestore data is missing 'client_id'. Please check cloudhawk.py!")
#         return pd.DataFrame()  # Return empty DataFrame
#
#     # 🔹 Ensure timestamp is sorted
#     df["timestamp"] = pd.to_datetime(df["timestamp"], format="%H:%M:%S", errors="coerce")
#     df = df.sort_values(by="timestamp", ascending=True)
#
#     return df
#
#
# # 🔹 Streamlit Dashboard Layout
# st.title("📊 CloudHawk Monitoring Dashboard")
# st.markdown("### **Real-time System Metrics for Client & Server**")
# st.write("🔄 Data updates every 5 seconds")
#
# # 🔹 Fetch real-time data
# df = fetch_data()
#
# if df.empty:
#     st.warning("⚠ No data found in Firestore. Waiting for system metrics...")
# else:
#     # 🔹 Separate data for Client & Server
#     client_data = df[df["client_id"] == "Client_2"]
#     server_data = df[df["client_id"] == "Client_1"]
#
#     # 🔹 Display Data Overview
#     st.subheader("📌 Latest Data Snapshot")
#     st.write(df.tail(5))  # Show last 5 records
#
#     # 🔹 Create Subplots for CPU, RAM, and Disk Usage
#     fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 8))
#     fig.suptitle("📊 System Metrics Comparison: Client vs Server", fontsize=14)
#
#     # 🔹 CPU Usage Graphs
#     axes[0, 0].plot(client_data["timestamp"], client_data["cpu_usage"], label="Client CPU Usage", color="blue")
#     axes[0, 1].plot(server_data["timestamp"], server_data["cpu_usage"], label="Server CPU Usage", color="red")
#     axes[0, 0].set_title("Client CPU Usage")
#     axes[0, 1].set_title("Server CPU Usage")
#
#     # 🔹 RAM Usage Graphs
#     axes[1, 0].plot(client_data["timestamp"], client_data["ram_usage"], label="Client RAM Usage", color="green")
#     axes[1, 1].plot(server_data["timestamp"], server_data["ram_usage"], label="Server RAM Usage", color="purple")
#     axes[1, 0].set_title("Client RAM Usage")
#     axes[1, 1].set_title("Server RAM Usage")
#
#     # 🔹 Disk Usage Graphs
#     axes[2, 0].plot(client_data["timestamp"], client_data["disk_usage"], label="Client Disk Usage", color="orange")
#     axes[2, 1].plot(server_data["timestamp"], server_data["disk_usage"], label="Server Disk Usage", color="brown")
#     axes[2, 0].set_title("Client Disk Usage")
#     axes[2, 1].set_title("Server Disk Usage")
#
#     # 🔹 Adjust layout
#     for ax in axes.flat:
#         ax.legend()
#         ax.set_xlabel("Time")
#         ax.set_ylabel("Usage %")
#         ax.tick_params(axis="x", rotation=45)
#
#     st.pyplot(fig)  # Render Matplotlib Graphs in Streamlit
#
# # 🔹 Auto-refresh every 5 seconds
# time.sleep(5)
# st.experimental_rerun()



# import streamlit as st
# import pandas as pd
# import firebase_admin
# from firebase_admin import credentials, firestore
# import time
# import matplotlib.pyplot as plt
#
# # 🔹 Initialize Firebase (Ensure only one initialization)
# if not firebase_admin._apps:
#     cred = credentials.Certificate("cloudhawk-firebase.json")
#     firebase_admin.initialize_app(cred)
#
# # 🔹 Firestore database reference
# db = firestore.client()
# collection_ref = db.collection("system_metrics")
#
# # 🔹 Function to fetch data from Firestore
# def fetch_data():
#     docs = collection_ref.stream()
#     data = [doc.to_dict() for doc in docs]
#
#     if not data:
#         return pd.DataFrame()  # Return empty DataFrame if no data
#
#     df = pd.DataFrame(data)
#
#     # ✅ Check if 'client_id' column exists
#     if "client_id" not in df.columns:
#         st.error("⚠ Firestore data is missing 'client_id'. Please check cloudhawk.py!")
#         return pd.DataFrame()  # Return empty DataFrame
#
#     # ✅ Ensure timestamp is sorted
#     df["timestamp"] = pd.to_datetime(df["timestamp"], format="%H:%M:%S", errors="coerce")
#     df = df.sort_values(by="timestamp", ascending=True)
#
#     return df
#
# # 🔹 Streamlit Dashboard Layout
# st.title("📊 CloudHawk Monitoring Dashboard")
# st.markdown("### **Real-time System Metrics for Client & Server**")
# st.write("🔄 Data updates every 5 seconds")
#
# # 🔹 Fetch real-time data
# df = fetch_data()
#
# if df.empty:
#     st.warning("⚠ No data found in Firestore. Waiting for system metrics...")
# else:
#     # ✅ Separate data for Client & Server
#     client_data = df[df["client_id"] == "Client_2"]
#     server_data = df[df["client_id"] == "Client_1"]
#
#     # ✅ Display Data Overview
#     st.subheader("📌 Latest Data Snapshot")
#     st.write(df.tail(5))  # Show last 5 records
#
#     # ✅ Create Subplots for CPU, RAM, and Disk Usage
#     fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 8))
#     fig.suptitle("📊 System Metrics Comparison: Client vs Server", fontsize=14)
#
#     # ✅ CPU Usage Graphs
#     axes[0, 0].plot(client_data["timestamp"], client_data["cpu_usage"], label="Client CPU Usage", color="blue")
#     axes[0, 1].plot(server_data["timestamp"], server_data["cpu_usage"], label="Server CPU Usage", color="red")
#     axes[0, 0].set_title("Client CPU Usage")
#     axes[0, 1].set_title("Server CPU Usage")
#
#     # ✅ RAM Usage Graphs
#     axes[1, 0].plot(client_data["timestamp"], client_data["ram_usage"], label="Client RAM Usage", color="green")
#     axes[1, 1].plot(server_data["timestamp"], server_data["ram_usage"], label="Server RAM Usage", color="purple")
#     axes[1, 0].set_title("Client RAM Usage")
#     axes[1, 1].set_title("Server RAM Usage")
#
#     # ✅ Disk Usage Graphs
#     axes[2, 0].plot(client_data["timestamp"], client_data["disk_usage"], label="Client Disk Usage", color="orange")
#     axes[2, 1].plot(server_data["timestamp"], server_data["disk_usage"], label="Server Disk Usage", color="brown")
#     axes[2, 0].set_title("Client Disk Usage")
#     axes[2, 1].set_title("Server Disk Usage")
#
#     # ✅ Adjust layout
#     for ax in axes.flat:
#         ax.legend()
#         ax.set_xlabel("Time")
#         ax.set_ylabel("Usage %")
#         ax.tick_params(axis="x", rotation=45)
#
#     st.pyplot(fig)  # Render Matplotlib Graphs in Streamlit
#
# # ✅ Auto-refresh every 5 seconds (Fixes `st.experimental_rerun()` Error)
# st.write("🔄 Refreshing in 5 seconds...")
# time.sleep(5)
# st.rerun()
# import streamlit as st
# import pandas as pd
# import joblib
# import firebase_admin
# from firebase_admin import credentials, firestore
#
# # 🔹 Load AI Model
# model = joblib.load("cloudhawk_ai_model.pkl")
#
# # 🔹 Initialize Firebase
# if not firebase_admin._apps:
#     cred = credentials.Certificate("cloudhawk-firebase.json")
#     firebase_admin.initialize_app(cred)
#
# db = firestore.client()
# collection_ref = db.collection("system_metrics")
#
#
# # 🔹 Fetch Data
# def fetch_data():
#     docs = collection_ref.stream()
#     data = [doc.to_dict() for doc in docs]
#     return pd.DataFrame(data) if data else pd.DataFrame()
#
#
# # 🔹 Streamlit UI
# st.title("🚀 CloudHawk AI Dashboard")
# st.write("🔄 Monitoring system performance & predicting outages.")
#
# df = fetch_data()
#
# if df.empty:
#     st.warning("⚠ No data available.")
# else:
#     # 🔹 AI Prediction
#     df["outage_prediction"] = model.predict(df[["cpu_usage", "ram_usage", "disk_usage"]])
#
#     # 🔹 Display Results
#     st.dataframe(df[["timestamp", "client_id", "cpu_usage", "ram_usage", "disk_usage", "outage_prediction"]])
#
#     # 🔹 Show Alerts
#     if df["outage_prediction"].sum() > 0:
#         st.error("⚠ ALERT: System crash predicted! Take action.")







# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials, firestore
# import pandas as pd
#
# # 🔹 Load Firebase credentials
# cred = credentials.Certificate("cloudhawk-firebase.json")
# firebase_admin.initialize_app(cred)
#
# # 🔹 Firestore database reference
# db = firestore.client()
#
# st.title("🔥 CloudHawk AI Dashboard")
#
# # Function to fetch latest AI predictions
# def fetch_predictions():
#     collection_ref = db.collection("system_predictions")
#     docs = collection_ref.stream()
#
#     data = []
#     for doc in docs:
#         record = doc.to_dict()
#         record["client_id"] = doc.id
#         data.append(record)
#
#     return pd.DataFrame(data) if data else None
#
# # 🔹 Fetch AI predictions
# predictions_df = fetch_predictions()
#
# if predictions_df is None or predictions_df.empty:
#     st.warning("⚠ No AI Predictions available yet!")
# else:
#     st.dataframe(predictions_df)
#     if predictions_df["predicted_outage"].iloc[0] == 1:
#         st.error("🚨 AI Prediction: System Crash or Outage Expected!")
#     else:
#         st.success("✅ AI Prediction: System Stable")


# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials, firestore
# import pandas as pd
# import plotly.express as px
# import time
#
# # 🔹 Load Firebase credentials
# if not firebase_admin._apps:
#     cred = credentials.Certificate("cloudhawk-firebase.json")
#     firebase_admin.initialize_app(cred)
#
# # 🔹 Firestore database reference
# db = firestore.client()
#
# st.title("🔥 CloudHawk AI Live Dashboard")
#
#
# # Function to fetch latest AI predictions
# def fetch_predictions():
#     collection_ref = db.collection("system_predictions")
#     docs = collection_ref.stream()
#
#     data = []
#     for doc in docs:
#         record = doc.to_dict()
#         record["client_id"] = doc.id
#         data.append(record)
#
#     return pd.DataFrame(data) if data else None


# Function to fetch latest system metrics
# def fetch_metrics():
#     collection_ref = db.collection("system_metrics")
#     docs = collection_ref.stream()
#
#     data = []
#     for doc in docs:
#         record = doc.to_dict()
#         record["client_id"] = doc.id
#         data.append(record)
#
#     return pd.DataFrame(data) if data else None
#
#
# # 🔹 Live Dashboard Updates
# st.subheader("📊 Live System Metrics & AI Predictions")
#
# # Placeholder for real-time updates
# metrics_placeholder = st.empty()
# chart_placeholder = st.empty()
# alert_placeholder = st.empty()
#
# # 🔄 Auto-refresh every 5 seconds
# while True:
#     # Fetch data from Firestore
#     predictions_df = fetch_predictions()
#     metrics_df = fetch_metrics()
#
#     if predictions_df is None or predictions_df.empty:
#         alert_placeholder.warning("⚠ No AI Predictions available yet!")
#     else:
#         # Display AI Predictions Table
#         metrics_placeholder.dataframe(predictions_df)
#
#         # Display System Alert
#         if predictions_df["predicted_outage"].iloc[-1] == 1:
#             alert_placeholder.error("🚨 AI Prediction: System Crash or Outage Expected!")
#         else:
#             alert_placeholder.success("✅ AI Prediction: System Stable")
#
#     if metrics_df is not None and not metrics_df.empty:
#         # Convert timestamp to datetime for visualization
#         metrics_df["timestamp"] = pd.to_datetime(metrics_df["timestamp"], errors='coerce')
#
#         # Sort by timestamp
#         metrics_df = metrics_df.sort_values(by="timestamp")
#
#         # Plot a live graph of CPU, RAM, and Disk Usage
#         fig = px.line(metrics_df, x="timestamp", y=["cpu_usage", "ram_usage", "disk_usage"],
#                       labels={"value": "Usage (%)", "timestamp": "Time"},
#                       title="📈 Live System Performance")
#
#         fig.update_layout(legend_title_text='Metrics')
#
#         # Update the graph
#         chart_placeholder.plotly_chart(fig, use_container_width=True)
#
#     time.sleep(5)  # Refresh every 5 seconds




import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import plotly.express as px

# 🔹 Load Firebase credentials
cred = credentials.Certificate("cloudhawk-firebase.json")
firebase_admin.initialize_app(cred)

# 🔹 Firestore database reference
db = firestore.client()

st.title("🔥 CloudHawk AI Dashboard")

# Function to fetch system metrics
def fetch_system_metrics():
    collection_ref = db.collection("system_metrics")
    docs = collection_ref.stream()

    data = []
    for doc in docs:
        record = doc.to_dict()
        data.append(record)

    return pd.DataFrame(data) if data else None

# Function to fetch AI predictions
def fetch_predictions():
    collection_ref = db.collection("system_predictions")
    docs = collection_ref.stream()

    data = []
    for doc in docs:
        record = doc.to_dict()
        record["client_id"] = doc.id
        data.append(record)

    return pd.DataFrame(data) if data else None

# 🔹 Fetch system metrics
metrics_df = fetch_system_metrics()

# 🔹 Fetch AI predictions
predictions_df = fetch_predictions()

# 🔹 Display System Metrics
if metrics_df is None or metrics_df.empty:
    st.warning("⚠ No system metrics available yet!")
else:
    st.subheader("📊 System Metrics")

    # 🔹 Separate data for both laptops
    laptop_1_data = metrics_df[metrics_df["client_id"] == "Client_1"]
    laptop_2_data = metrics_df[metrics_df["client_id"] == "Client_2"]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💻 Laptop 1 (Client_1)")
        if not laptop_1_data.empty:
            st.metric("CPU Usage", f"{laptop_1_data['cpu_usage'].iloc[-1]}%")
            st.metric("RAM Usage", f"{laptop_1_data['ram_usage'].iloc[-1]}%")
            st.metric("Disk Usage", f"{laptop_1_data['disk_usage'].iloc[-1]}%")
        else:
            st.warning("No data available for Laptop 1")

    with col2:
        st.subheader("💻 Laptop 2 (Server_1)")
        if not laptop_2_data.empty:
            st.metric("CPU Usage", f"{laptop_2_data['cpu_usage'].iloc[-1]}%")
            st.metric("RAM Usage", f"{laptop_2_data['ram_usage'].iloc[-1]}%")
            st.metric("Disk Usage", f"{laptop_2_data['disk_usage'].iloc[-1]}%")
        else:
            st.warning("No data available for Laptop 2")

    # 🔹 Live Graph for CPU Usage
    st.subheader("📈 Live System Usage Graphs")

    fig_cpu = px.line(metrics_df, x="timestamp", y="cpu_usage", color="client_id", title="CPU Usage Over Time")
    fig_ram = px.line(metrics_df, x="timestamp", y="ram_usage", color="client_id", title="RAM Usage Over Time")
    fig_disk = px.line(metrics_df, x="timestamp", y="disk_usage", color="client_id", title="Disk Usage Over Time")

    st.plotly_chart(fig_cpu)
    st.plotly_chart(fig_ram)
    st.plotly_chart(fig_disk)

# 🔹 Display AI Predictions
if predictions_df is None or predictions_df.empty:
    st.warning("⚠ No AI Predictions available yet!")
else:
    st.subheader("🧠 AI Model Predictions")
    st.dataframe(predictions_df)

    if predictions_df["predicted_outage"].iloc[0] == 1:
        st.error("🚨 AI Prediction: System Crash or Outage Expected!")
    else:
        st.success("✅ AI Prediction: System Stable")

st.info("🔄 Dashboard refreshes automatically as new data arrives.")

