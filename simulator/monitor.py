# File: monitor.py
# Author: Lex Albrandt
#

# Imports
import random
import time
import json
import paho.mqtt.client as mqtt

# Set up a broker and client
BROKER = "localhost"
PORT = 1883

# Create a client object and connect to the MQTT broker via TCP
client = mqtt.Client()
client.connect(BROKER, PORT)

def generate_vitals():
    """
    This function returns a python dictionary that servces as a vital sign snapshot 
    for a single patient

    Returns:
        Python Dictionary: Patient vitals snapshot
    """
    
    return {
        "device id": "monitor-001",
        "patient-id": "patient-001",
        "heart_rate": random.randint(50, 110),
        "spo2": random.randint(94, 100),
        "systolic_bp": random.randint(80, 120),
        "diastolic_bp": random.randint(60, 90),
        "timestamp": time.time()
    }

# Runs indefinitely
while True:

    data = generate_vitals()

    client.publish(
        "hospital/patient/telemetry",
        json.dumps(data)
    )

    print(data)

    time.sleep(1)