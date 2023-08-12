from fastapi import FastAPI

app = FastAPI()

patients = {
    1: {"name": "Alice", "age": 65},
    2: {"name": "Bob", "age": 70},
    3: {"name": "Eve", "age": 75}
}

# Sample route with path parameter
@app.get("/patient/{patient_id}")
def get_patient(patient_id: int):
    if patient_id in patients:
        return patients[patient_id]
    else:
        return {"error": "Patient not found"}

# Sample route with query parameter
@app.get("/patients/")
def get_patients(age: int = None):
    if age is None:
        return patients
    else:
        filtered_patients = {pid: patient for pid, patient in patients.items() if patient["age"] == age}
        return filtered_patients

# Sample route to create a new patient
@app.post("/patient/")
def create_patient(patient_data: dict):
    patient_id = max(patients.keys()) + 1
    patients[patient_id] = patient_data
    return {"message": "Patient created", "patient_id": patient_id}

# Sample route to update patient data
@app.put("/patient/{patient_id}")
def update_patient(patient_id: int, updated_data: dict):
    if patient_id in patients:
        patients[patient_id].update(updated_data)
        return {"message": "Patient data updated"}
    else:
        return {"error": "Patient not found"}

# Sample route to delete a patient
@app.delete("/patient/{patient_id}")
def delete_patient(patient_id: int):
    if patient_id in patients:
        del patients[patient_id]
        return {"message": "Patient deleted"}
    else:
        return {"error": "Patient not found"}
