from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set up CORS
origins = ["http://localhost", "http://localhost:8080", "http://localhost:63343"]  # Add your frontend URLs here
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database for patient profiles
profile_db = {
    'patient_name': "John Doe",
    'age': 60,
    'diagnosis': "Alzheimer’s disease",
    "profile_picture": "https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_1280.png",
    "patient_address": "Delhi, India",
    'notes': ""
}

patient_data = []

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
    return {
        'message': "Work in progress",
        "must contain": "patient location"
    }

@app.get("/patient/vitals")
def get_patient_vitals():
    return {
        "message": "Work in progress",
        "must contain": "Glucometer, heart rate tracker, GPS tracker, BP monitoring, SPO2"
    }

@app.get("/patient/ehr")
def get_patient_ehr():
    return {
        "message": "Work in progress",
        "must contain": "EHR DATA"
    }


# Run the server with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
