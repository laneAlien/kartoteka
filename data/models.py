from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

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
