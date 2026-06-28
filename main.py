from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas, models, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title= 'Patient Apppointments Tracker',
    description= 'Use FastAPI to track patient records',
    version= '1.0.0'
)

## CREATE(POST)
@app.post("/patients/", response_model= schemas.PatientResponse)
def create_patient(data:schemas.PatientCreate, db:Session= Depends(get_db)):
    return crud.create_patient(db, data)


## READ ALL RECORD (GET)
@app.get("/patients/", response_model= List[schemas.PatientResponse])
def get_all_patients(db:Session= Depends(get_db)):
    return crud.get_all_patients(db)


## READ ONLY ONE RECORD (GET)
@app.get("/patient/{patient_id}", response_model = schemas.PatientResponse)

def get_patient(patient_id:int, db:Session = Depends(get_db)):

    patient = crud.get_patient(db, patient_id)

    if not patient:
        raise HTTPException(404,'Patient not found')
    return patient

## UPDATE RECORD(PUT)
@app.put("/patient/{patient_id}", response_model = schemas.PatientResponse)

def update_patient(patient_id: int, data:schemas.PatientUpdate,db:Session= Depends(get_db)):

    updated_patient = crud.update_patient(db, patient_id, data)

    if not updated_patient:
        raise HTTPException (404, 'Patient not found')
    return updated_patient

## DELETE RECORD (DELETE)
@app.delete("/patient/{patient_id}")

def delete_patient(patient_id:int, db:Session=Depends(get_db)):

    patient = crud.delete_patient(db, patient_id)

    if not patient:
        raise HTTPException(404, 'Patient not found')
    return{"message":"Patient deleted successfully"}