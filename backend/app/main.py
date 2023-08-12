from fastapi import FastAPI

app = FastAPI()

# In-memory database for patient profiles
profile_db = {
    'patient_name': "John Doe",
    'Age': 60,
    'diagnosis': "Alzheimer’s disease",
}
# Set up CORS
origins = ["http://localhost", "http://localhost:8080", "http://localhost:63343"]  # Add your frontend URLs here
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Route to get patient profile by ID
@app.get("/patient")
def get_patient_profile():
    return profile_db

# Route to update patient parameters
@app.put("/patient")
def update_patient_params(patient_updates: dict):
    profile_db.update(patient_updates)
    return {"message": "Patient parameters updated"}


# Run the server with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
