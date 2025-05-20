import sys
import requests
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, 
                             QPushButton, QVBoxLayout, QWidget, QFormLayout, QLineEdit, 
                             QMessageBox, QDialog)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Картотека")
        self.setGeometry(100, 100, 600, 400)

        self.table = QTableWidget(self)
        self.load_data()

        self.button_refresh = QPushButton("Обновить", self)
        self.button_refresh.clicked.connect(self.load_data)

        self.button_add_equipment = QPushButton("Добавить оборудование", self)
        self.button_add_equipment.clicked.connect(self.add_equipment)

        self.button_add_request = QPushButton("Добавить заявку на ремонт", self)
        self.button_add_request.clicked.connect(self.add_repair_request)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.button_refresh)
        self.layout.addWidget(self.button_add_equipment)
        self.layout.addWidget(self.button_add_request)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def load_data(self):
        response = requests.get("http://localhost:5000/api/equipment")
        if response.status_code == 200:
            data = response.json()
            self.table.setRowCount(len(data))
            self.table.setColumnCount(4)  # Измените количество колонок на 4
            for row, item in enumerate(data):
                self.table.setItem(row, 0, QTableWidgetItem(str(item['id'])))
                self.table.setItem(row, 1, QTableWidgetItem(item['name']))
                self.table.setItem(row, 2, QTableWidgetItem(item['type']))
                self.table.setItem(row, 3, QTableWidgetItem(item['location']))
            self.table.cellDoubleClicked.connect(self.edit_equipment)
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось загрузить данные.")

    def add_equipment(self):
        dialog = AddEquipmentDialog(self)
        dialog.exec_()
        self.load_data()

    def add_repair_request(self):
        dialog = AddRepairRequestDialog(self)
        dialog.exec_()
        self.load_data()

    def edit_equipment(self, row, column):
        item_id = int(self.table.item(row, 0).text())
        dialog = EditEquipmentDialog(self, item_id)
        dialog.exec_()
        self.load_data()

class AddEquipmentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить оборудование")
        self.setGeometry(200, 200, 300, 200)

        self.layout = QFormLayout(self)

        self.name_input = QLineEdit(self)
        self.type_input = QLineEdit(self)
        self.location_input = QLineEdit(self)

        self.layout.addRow("Название:", self.name_input)
        self.layout.addRow("Тип:", self.type_input)
        self.layout.addRow("Место:", self.location_input)

        self.button_add = QPushButton("Добавить", self)
        self.button_add.clicked.connect(self.submit)
        self.layout.addWidget(self.button_add)

        self.setLayout(self.layout)

    def submit(self):
        new_equipment = {
            "name": self.name_input.text(),
            "type": self.type_input.text(),
            "location": self.location_input.text(),
        }
        response = requests.post("http://localhost:5000/api/equipment/", json=new_equipment)
        if response.status_code == 201:
            QMessageBox.information(self, "Успех", "Оборудование добавлено.")
            self.accept()
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось добавить оборудование.")

class EditEquipmentDialog(QDialog):
    def __init__(self, parent, equipment_id):
        super().__init__(parent)
        self.equipment_id = equipment_id
        self.setWindowTitle("Редактировать оборудование")
        self.setGeometry(200, 200, 300, 200)

        self.layout = QFormLayout(self)
        self.name_input = QLineEdit(self)
        self.type_input = QLineEdit(self)
        self.location_input = QLineEdit(self)

        self.layout.addRow("Название:", self.name_input)
        self.layout.addRow("Тип:", self.type_input)
        self.layout.addRow("Место:", self.location_input)

        self.button_update = QPushButton("Обновить", self)
        self.button_update.clicked.connect(self.submit)
        self.layout.addWidget(self.button_update)

        self.setLayout(self.layout)
        self.load_equipment_data()

    def load_equipment_data(self):
        response = requests.get(f"http://localhost:5000/api/equipment/{self.equipment_id}")
        if response.status_code == 200:
            data = response.json()
            self.name_input.setText(data['name'])
            self.type_input.setText(data['type'])
            self.location_input.setText(data['location'])

    def submit(self):
        updated_equipment = {
            "name": self.name_input.text(),
            "type": self.type_input.text(),
            "location": self.location_input.text(),
        }
        response = requests.put(f"http://localhost:5000/api/equipment/{self.equipment_id}", json=updated_equipment)
        if response.status_code == 200:
            QMessageBox.information(self, "Успех", "Оборудование обновлено.")
            self.accept()
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось обновить оборудование.")

class AddRepairRequestDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить заявку на ремонт")
        self.setGeometry(200, 200, 300, 200)

        self.layout = QFormLayout(self)

        self.equipment_id_input = QLineEdit(self)
        self.description_input = QLineEdit(self)

        self.layout.addRow("ID оборудования:", self.equipment_id_input)
        self.layout.addRow("Описание:", self.description_input)

        self.button_add = QPushButton("Добавить", self)
        self.button_add.clicked.connect(self.submit)
        self.layout.addWidget(self.button_add)

        self.setLayout(self.layout)

    def submit(self):
        new_request = {
            "equipment_id": self.equipment_id_input.text(),
            "description": self.description_input.text(),
        }
        response = requests.post("http://localhost:5000/api/repair_requests/", json=new_request)
        if response.status_code == 201:
            QMessageBox.information(self, "Успех", "Заявка на ремонт добавлена.")
            self.accept()
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось добавить заявку на ремонт.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

