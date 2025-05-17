from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pass@localhost/kartoteka"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Модель оборудования
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    location = db.Column(db.String(50))
    installation_date = db.Column(db.Date)

    def save(self):
        db.session.add(self)
        db.session.commit()

# Модель заявки на ремонт
class RepairRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    master_id = db.Column(db.Integer)  # Пример, можно добавить модель пользователей
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.String(20), default='Open')
    opened_at = db.Column(db.DateTime, default=datetime.utcnow)
    closed_at = db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        db.session.commit()

@app.route('/api/equipment/', methods=['GET'])
def list_equipment():
    items = Equipment.query.all()
    return jsonify([{'id': e.id, 'name': e.name, 'type': e.type, 'location': e.location} for e in items])

@app.route('/api/equipment/', methods=['POST'])
def add_equipment():
    data = request.json
    eq = Equipment(
        name=data['name'],
        type=data.get('type'),
        location=data.get('location'),
        installation_date=data.get('installation_date')
    )
    eq.save()
    return jsonify({'id': eq.id}), 201

@app.route('/api/equipment/<int:id>', methods=['PUT'])
def update_equipment(id):
    data = request.json
    equipment = Equipment.query.get_or_404(id)
    equipment.name = data['name']
    equipment.type = data.get('type')
    equipment.location = data.get('location')
    db.session.commit()
    return jsonify({'message': 'Оборудование обновлено.'})

@app.route('/api/equipment/<int:id>', methods=['DELETE'])
def delete_equipment(id):
    equipment = Equipment.query.get_or_404(id)
    db.session.delete(equipment)
    db.session.commit()
    return jsonify({'message': 'Оборудование удалено.'})

@app.route('/api/repair_requests/', methods=['GET'])
def list_repair_requests():
    requests = RepairRequest.query.all()
    return jsonify([{'id': r.id, 'equipment_id': r.equipment_id, 'description': r.description, 'status': r.status} for r in requests])

@app.route('/api/repair_requests/', methods=['POST'])
def add_repair_request():
    data = request.json
    request = RepairRequest(
        equipment_id=data['equipment_id'],
        master_id=data.get('master_id'),
        description=data['description']
    )
    request.save()
    return jsonify({'id': request.id}), 201

@app.route('/api/repair_requests/<int:id>', methods=['PUT'])
def update_repair_request(id):
    data = request.json
    request = RepairRequest.query.get_or_404(id)
    request.description = data['description']
    request.status = data.get('status', request.status)
    db.session.commit()
    return jsonify({'message': 'Заявка обновлена.'})

@app.route('/api/repair_requests/<int:id>', methods=['DELETE'])
def delete_repair_request(id):
    request = RepairRequest.query.get_or_404(id)
    db.session.delete(request)
    db.session.commit()
    return jsonify({'message': 'Заявка удалена.'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создает таблицы в базе данных
    app.run(host='0.0.0.0', port=5000)


