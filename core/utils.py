def format_equipment_data(equipment):
    return {
        "id": equipment.id,
        "name": equipment.name,
        "type": equipment.type,
        "location": equipment.location,
        "installation_date": equipment.installation_date.isoformat() if equipment.installation_date else None,
    }

def format_repair_request_data(request):
    return {
        "id": request.id,
        "equipment_id": request.equipment_id,
        "description": request.description,
        "status": request.status,
        "opened_at": request.opened_at.isoformat(),
        "closed_at": request.closed_at.isoformat() if request.closed_at else None,
    }
