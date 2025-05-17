from .models import Equipment, RepairRequest, db

class EquipmentRepository:
    @staticmethod
    def get_all_equipment():
        return Equipment.query.all()

    @staticmethod
    def add_equipment(equipment):
        db.session.add(equipment)
        db.session.commit()

    @staticmethod
    def update_equipment(equipment):
        db.session.commit()

    @staticmethod
    def delete_equipment(equipment):
        db.session.delete(equipment)
        db.session.commit()

class RepairRequestRepository:
    @staticmethod
    def get_all_requests():
        return RepairRequest.query.all()

    @staticmethod
    def add_request(request):
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def update_request(request):
        db.session.commit()

    @staticmethod
    def delete_request(request):
        db.session.delete(request)
        db.session.commit()
