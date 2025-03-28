import psutil
import time
import socket  # 🔹 Get unique hostname
import firebase_admin
from firebase_admin import credentials, firestore
from plyer import notification
import smtplib
from email.mime.text import MIMEText

# 🔹 Check if Firebase is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("cloudhawk-firebase.json")
    firebase_admin.initialize_app(cred)

# 🔹 Firestore Reference
db = firestore.client()
collection_ref = db.collection("system_metrics")

# 🔹 Auto-detect client ID using hostname
client_id = socket.gethostname()  # ✅ Unique per machine

# 🔹 Alert Email Configuration
EMAIL_SENDER = "varad266@gmail.com"  # 🔹 Replace with your email
EMAIL_PASSWORD = "dpgo foco ebzm ooli"  # 🔹 Use App Password if using Gmail
EMAIL_RECEIVER = "atharvamadane271003"  # 🔹 Admin's email to receive alerts


# Function to send email alert
def send_email_alert(subject, message):
    try:
        msg = MIMEText(message)
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = subject

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("✅ Email Alert Sent!")
    except Exception as e:
        print(f"⚠ Error Sending Email: {e}")


# Function to send system metrics
def send_system_metrics():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage("/").percent
        timestamp = time.strftime("%H:%M:%S")

        system_data = {
            "client_id": client_id,  # ✅ Unique per machine
            "cpu_usage": cpu_usage,
            "ram_usage": ram_usage,
            "disk_usage": disk_usage,
            "timestamp": timestamp
        }

        # ✅ Store data in Firestore
        collection_ref.document(f"{client_id}_{timestamp}").set(system_data)

        print(f"✅ Data Sent from {client_id}: {system_data}")

        # 🔹 Check for high usage and send alerts
        if cpu_usage > 80 or ram_usage > 85 or disk_usage > 90:
            alert_message = f"⚠ High Resource Usage Detected on {client_id}!\nCPU: {cpu_usage}%\nRAM: {ram_usage}%\nDisk: {disk_usage}%"

            # 🔹 Send Email Alert
            send_email_alert(f"🚨 {client_id} - System Overload Alert", alert_message)

            # 🔹 Show Desktop Notification
            notification.notify(
                title=f"⚠ {client_id} - System Overload Alert",
                message=alert_message,
                timeout=10
            )

        time.sleep(5)  # Send data every 5 seconds


# Run data collection
send_system_metrics()
