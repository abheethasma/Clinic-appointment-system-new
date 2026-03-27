from data_service import DoctorMockDataService


class DoctorService:
    def __init__(self):
        self.data_service = DoctorMockDataService()

    def get_all(self):
        return self.data_service.get_all_doctors()

    def get_by_id(self, doctor_id: int):
        return self.data_service.get_doctor_by_id(doctor_id)

    def create(self, doctor_data):
        return self.data_service.add_doctor(doctor_data)

    def update(self, doctor_id: int, doctor_data):
        return self.data_service.update_doctor(doctor_id, doctor_data)

    def delete(self, doctor_id: int):
        return self.data_service.delete_doctor(doctor_id)