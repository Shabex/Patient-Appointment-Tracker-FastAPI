from sqlalchemy.orm import Session
import models, schemas

## CREATE OPERATION
def create_patient(db: Session, data: schemas.PatientCreate):

    db_create = models.Patient(**data.model_dump())

    db.add(db_create)
    db.commit()
    db.refresh(db_create)
    return db_create


## READ ONLY ONE RECORD
def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

## READ ALL THE RECORDS
def get_all_patients(db: Session):
    return db.query(models.Patient).all()


## UPDATE RECORDS
def update_patient(db:Session, patient_id:int, data: schemas.PatientUpdate):
    db_update = db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not db_update:
        return None
    dictionary = data.model_dump(exclude_unset=True)

    for key, value in dictionary.items():
        setattr(db_update, key, value)
    
    db.commit()
    db.refresh(db_update)
    return db_update


## DELETE OPERATION
def delete_patient(db: Session, patient_id: int):
    db_delete = db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not db_delete:
        return None
    db.delete(db_delete)
    db.commit()
    return db_delete