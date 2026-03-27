from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Appointment, AppointmentCreate, AppointmentUpdate
from service import AppointmentService

app = FastAPI(title="Appointment Microservice", version="1.0.0")

appointment_service = AppointmentService()


@app.get("/")
def read_root():
    return {"message": "Appointment Microservice is running"}


@app.get("/api/appointments", response_model=List[Appointment])
def get_all_appointments():
    return appointment_service.get_all()


@app.get("/api/appointments/{appointment_id}", response_model=Appointment)
def get_appointment(appointment_id: int):
    appointment = appointment_service.get_by_id(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment


@app.post("/api/appointments", response_model=Appointment, status_code=status.HTTP_201_CREATED)
def create_appointment(appointment: AppointmentCreate):
    return appointment_service.create(appointment)


@app.put("/api/appointments/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: int, appointment: AppointmentUpdate):
    updated_appointment = appointment_service.update(appointment_id, appointment)
    if not updated_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return updated_appointment


@app.delete("/api/appointments/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(appointment_id: int):
    success = appointment_service.delete(appointment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return None