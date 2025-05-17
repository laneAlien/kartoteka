def validate_equipment_data(data):
    if not data.get('name'):
        raise ValueError("Название оборудования обязательно.")
    if not data.get('type'):
        raise ValueError("Тип оборудования обязателен.")
    if not data.get('location'):
        raise ValueError("Место установки обязательно.")

def validate_repair_request_data(data):
    if not data.get('equipment_id'):
        raise ValueError("ID оборудования обязателен.")
    if not data.get('description'):
        raise ValueError("Описание заявки обязательно.")
