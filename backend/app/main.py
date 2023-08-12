from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

origins = ["http://localhost", "http://localhost:8080", "http://localhost:8000", "http://localhost:63342"]  # Recorded frontend URLs
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

profile_db = {
    'patient_name': "John Doe",
    'age': 60,
    'diagnosis': "Alzheimer’s disease",
    "profile_picture": "https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_1280.png",
    "patient_address": "Delhi, India",
    'notes': "Early Onset Dementia"
}

patient_data = []
patient_alerts = []
patient_reminders = []
patient_sleep_data = []

# Route to get patient profile
@app.get("/patient/profile")
def get_patient_profile():
    return profile_db

# Route to update patient parameters
@app.put("/patient/profile")
def update_patient_params(patient_updates: dict):
    profile_db.update(patient_updates)
    return {"message": "Patient parameters updated"}

@app.get("/patient/location")
def get_patient_location():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    iframe_src = f"https://www.openstreetmap.org/export/embed.html?bbox={longitude - 1}%2C{latitude - 1}%2C{longitude + 1}%2C{latitude + 1}&amp;layer=mapnik&amp;marker={latitude}%2C{longitude}"
    return {"iframe_src": iframe_src}

@app.get("/patient/vitals")
def get_patient_vitals():
    heart_rate = random.randint(70, 120)
    blood_pressure = [random.randint(70, 95), random.randint(100, 140)]
    spo2 = random.randint(80, 98)
    blood_glucose = random.randint(60, 110)
    return {
        "heart_rate": heart_rate,
        "blood_pressure": blood_pressure,
        "spo2": spo2,
        "blood_glucose": blood_glucose
    }

@app.get("/patient/ehr")
def get_patient_ehr():
    return {
        "message": "Work in progress",
        "must contain": "EHR DATA"
    }

@app.get("/patient/alerts")
def get_alerts():
    if len(patient_alerts) == 0:
        return ["You don't have any Alerts"]
    else:
        return patient_alerts

@app.put("/patient/alerts/put")
def post_alerts(alert: str):
    patient_alerts.append(alert)

@app.get("/patient/reminders")
def get_reminders():
    if len(patient_reminders) == 0:
        return ["You don't have any Reminders"]
    else:
        return patient_reminders

@app.put("/patient/reminders/put")
def post_reminders(reminder: str):
    patient_reminders.append(reminder)

@app.get("/patient/sleep_data")
def get_patient_sleep_data():
    if len(patient_sleep_data) == 0:
        return ["No Sleep Data Available"]
    else:
        return patient_sleep_data

@app.put("/patient/sleep_data/put")
def put_patient_sleep_data(date, duration):
    patient_sleep_data.append({date: duration})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
