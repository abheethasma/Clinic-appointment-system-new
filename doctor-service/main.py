from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Doctor, DoctorCreate, DoctorUpdate
from service import DoctorService

app = FastAPI(title="Doctor Microservice", version="1.0.0")

doctor_service = DoctorService()


@app.get("/")
def read_root():
    return {"message": "Doctor Microservice is running"}


@app.get("/api/doctors", response_model=List[Doctor])
def get_all_doctors():
    return doctor_service.get_all()


@app.get("/api/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    doctor = doctor_service.get_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


@app.post("/api/doctors", response_model=Doctor, status_code=status.HTTP_201_CREATED)
def create_doctor(doctor: DoctorCreate):
    return doctor_service.create(doctor)


@app.put("/api/doctors/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, doctor: DoctorUpdate):
    updated_doctor = doctor_service.update(doctor_id, doctor)
    if not updated_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated_doctor


@app.delete("/api/doctors/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id: int):
    success = doctor_service.delete(doctor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return None