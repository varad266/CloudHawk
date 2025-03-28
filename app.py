import psutil
import time
import winsound
from plyer import notification
import smtplib

sender_email = "varad266@gmail.com"
receiver_email = "atharvamadane271003@gmail.com"
password = "dpgo foco ebzm ooli"  # Gmail App password
#
import psutil
import time
import smtplib
import os
import threading
import winsound
from plyer import notification
from dotenv import load_dotenv
import tkinter as tk
from tkinter import Label, Button

# Load environment variables from .env file
load_dotenv()

# Secure Email Credentials
SENDER_EMAIL = os.getenv("varad266@gmail.com")  # Example: varad266@gmail.com
RECEIVER_EMAIL = os.getenv("vedaa2424@gmail.com")  # Example: vedaa2424@gmail.com
EMAIL_PASSWORD = os.getenv("dpgo foco ebzm ooli")  # Use App Password

# Alert Thresholds
CPU_THRESHOLD = 70  # CPU usage %
RAM_THRESHOLD = 80  # RAM usage %

# Global monitoring flag
monitoring = False


def email_alert(subject, message):
    """Send an email alert."""
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, receiver_email, email_message)
        server.quit()
        print("✅ Email Alert Sent!")
    except Exception as e:
        print("❌ ERROR Sending Email:", e)


def system_monitor():
    """Monitor CPU & RAM usage and update the GUI."""
    global monitoring
    while monitoring:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        # Update GUI Labels
        cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        ram_label.config(text=f"RAM Usage: {ram_usage}%")

        print(f"📊 CPU: {cpu_usage}% | RAM: {ram_usage}%")

        if cpu_usage >= CPU_THRESHOLD:
            print("🔥 High CPU Usage Detected!")
            winsound.Beep(1000, 500)
            notification.notify(
                title="⚠️ HIGH CPU USAGE ALERT",
                message=f"CPU Usage: {cpu_usage}%",
                timeout=5
            )
            email_alert("HIGH CPU USAGE ALERT!", f"CPU Usage is at {cpu_usage}%. Check your system.")

        if ram_usage >= RAM_THRESHOLD:
            print("🚨 High RAM Usage Detected!")
            winsound.Beep(1200, 500)
            notification.notify(
                title="⚠️ HIGH RAM USAGE ALERT",
                message=f"RAM Usage: {ram_usage}%",
                timeout=5
            )
            email_alert("HIGH RAM USAGE ALERT!", f"RAM Usage is at {ram_usage}%. Check your system.")

        time.sleep(2)  # Check every 2 seconds


def start_monitoring():
    """Start monitoring in a new thread to avoid freezing the GUI."""
    global monitoring
    if not monitoring:
        monitoring = True
        threading.Thread(target=system_monitor, daemon=True).start()


def stop_monitoring():
    """Stop the monitoring loop."""
    global monitoring
    monitoring = False


# GUI Setup
root = tk.Tk()
root.title("CloudHawk - System Monitor")
root.geometry("400x300")
root.resizable(False, False)

# Labels
title_label = Label(root, text="CloudHawk - System Monitor", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

cpu_label = Label(root, text="CPU Usage: --%", font=("Arial", 12))
cpu_label.pack(pady=5)

ram_label = Label(root, text="RAM Usage: --%", font=("Arial", 12))
ram_label.pack(pady=5)

# Buttons
start_button = Button(root, text="Start Monitoring", font=("Arial", 12), bg="green", fg="white", command=start_monitoring)
start_button.pack(pady=10)

stop_button = Button(root, text="Stop Monitoring", font=("Arial", 12), bg="red", fg="white", command=stop_monitoring)
stop_button.pack(pady=5)

# Run GUI
root.mainloop()


