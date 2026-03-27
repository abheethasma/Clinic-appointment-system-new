from data_service import AppointmentMockDataService


class AppointmentService:
    def __init__(self):
        self.data_service = AppointmentMockDataService()

    def get_all(self):
        return self.data_service.get_all_appointments()

    def get_by_id(self, appointment_id: int):
        return self.data_service.get_appointment_by_id(appointment_id)

    def create(self, appointment_data):
        return self.data_service.add_appointment(appointment_data)

    def update(self, appointment_id: int, appointment_data):
        return self.data_service.update_appointment(appointment_id, appointment_data)

    def delete(self, appointment_id: int):
        return self.data_service.delete_appointment(appointment_id)