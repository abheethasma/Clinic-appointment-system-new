from models import Appointment


class AppointmentMockDataService:
    def __init__(self):
        self.appointments = [
            Appointment(
                id=1,
                patient_id=1,
                doctor_id=1,
                appointment_date="2026-03-29",
                appointment_time="10:00 AM",
                reason="Chest pain consultation",
                status="Scheduled"
            ),
            Appointment(
                id=2,
                patient_id=2,
                doctor_id=2,
                appointment_date="2026-03-30",
                appointment_time="02:30 PM",
                reason="Tooth filling",
                status="Scheduled"
            ),
            Appointment(
                id=3,
                patient_id=3,
                doctor_id=3,
                appointment_date="2026-03-31",
                appointment_time="11:15 AM",
                reason="Skin allergy check",
                status="Completed"
            ),
        ]
        self.next_id = 4

    def get_all_appointments(self):
        return self.appointments

    def get_appointment_by_id(self, appointment_id: int):
        return next((a for a in self.appointments if a.id == appointment_id), None)

    def add_appointment(self, appointment_data):
        new_appointment = Appointment(id=self.next_id, **appointment_data.model_dump())
        self.appointments.append(new_appointment)
        self.next_id += 1
        return new_appointment

    def update_appointment(self, appointment_id: int, appointment_data):
        appointment = self.get_appointment_by_id(appointment_id)
        if appointment:
            update_data = appointment_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(appointment, key, value)
            return appointment
        return None

    def delete_appointment(self, appointment_id: int):
        appointment = self.get_appointment_by_id(appointment_id)
        if appointment:
            self.appointments.remove(appointment)
            return True
        return False