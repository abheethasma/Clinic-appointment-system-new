from models import Doctor


class DoctorMockDataService:
    def __init__(self):
        self.doctors = [
            Doctor(
                id=1,
                name="Dr. Silva",
                specialization="Cardiologist",
                phone="0772223344",
                email="dr.silva@example.com",
                available_days="Monday, Wednesday, Friday"
            ),
            Doctor(
                id=2,
                name="Dr. Peris",
                specialization="Dentist",
                phone="0715556677",
                email="dr.peris@example.com",
                available_days="Tuesday, Thursday, Saturday"
            ),
            Doctor(
                id=3,
                name="Dr. Fernando",
                specialization="Dermatologist",
                phone="0758889900",
                email="dr.fernando@example.com",
                available_days="Monday, Thursday"
            ),
        ]
        self.next_id = 4

    def get_all_doctors(self):
        return self.doctors

    def get_doctor_by_id(self, doctor_id: int):
        return next((d for d in self.doctors if d.id == doctor_id), None)

    def add_doctor(self, doctor_data):
        new_doctor = Doctor(id=self.next_id, **doctor_data.model_dump())
        self.doctors.append(new_doctor)
        self.next_id += 1
        return new_doctor

    def update_doctor(self, doctor_id: int, doctor_data):
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            update_data = doctor_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(doctor, key, value)
            return doctor
        return None

    def delete_doctor(self, doctor_id: int):
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            self.doctors.remove(doctor)
            return True
        return False