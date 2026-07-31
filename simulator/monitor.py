# File: monitor.py
# Author: Lex Albrandt
#

# Imports
import random
import time
import json
import paho.mqtt.client as mqtt


# Broker and client Constants
BROKER = "localhost"
PORT = 1883

class PatientState():

    def __init__(self):
        self.heart_rate = 75
        self.spo2 = 98
        self.systolic_bp = 120
        self.diastolic_bp = 80

    def update(self):
        self.heart_rate += random.gauss(0, 1)
        self.spo2 += random.gauss(0, 0.5) 
        self.systolic_bp += random.gauss(0, 1)
        self.diastolic_bp += random.gauss(0, 0.05)
    
        self.heart_rate = max(40, min(self.heart_rate, 180))
        self.spo2 = max(70, min(self.spo2, 100))

    def get_vitals(self):
        
        return {
            "heart_rate": round(self.heart_rate),
            "spo2": round(self.spo2),
            "blood_pressure": {
                "systolic_bp": round(self.systolic_bp),
                "diastolic_bp": round(self.diastolic_bp)
            }
        }

patient = PatientState()

# Create a client object and connect to the MQTT broker via TCP
client = mqtt.Client()
client.connect(BROKER, PORT)

# Run loop
while True:

    patient.update()

    # Use dictionary unpacking into the data dictionary
    data = {
        "device": {
            "id": "monitor-001",
            "type": "patient-monitor"
        },
        "patient": {
            "id": "patient-001"
        },
        "timestamp": time.time(),
        "vitals": patient.get_vitals()
    }

    # Serialize as a JSON file
    # Sends to MQTT broker
    client.publish(
        "hospital/patient/telemetry",
        json.dumps(data)
    )

    print(json.dumps(data, indent=2))

    time.sleep(1)