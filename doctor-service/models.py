from pydantic import BaseModel
from typing import Optional


class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    email: str
    available_days: str


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: str
    email: str
    available_days: str


class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    available_days: Optional[str] = None