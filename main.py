from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory database for patient profiles
patients_db = {}

# Route to create a new patient profile
@app.post("/patient/")
def create_patient_profile(patient_name: str, age: int, diagnosis: str):
    patient_id = len(patients_db) + 1
    new_patient = {
        "patient_name": patient_name,
        "age": age,
        "diagnosis": diagnosis
    }
    patients_db[patient_id] = new_patient
    return {"message": "Patient profile created", "patient_id": patient_id}

# Route to get patient profile by ID
@app.get("/patient/{patient_id}")
def get_patient_profile(patient_id: int):
    if patient_id in patients_db:
        return patients_db[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

# Route to update patient parameters
@app.put("/patient/{patient_id}")
def update_patient_params(patient_id: int, patient_updates: dict):
    if patient_id in patients_db:
        patients_db[patient_id].update(patient_updates)
        return {"message": "Patient parameters updated"}
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

# Run the server with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
