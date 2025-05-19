import sys
import requests
from client.client import AddEquipmentDialog, EditEquipmentDialog
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, 
                             QPushButton, QVBoxLayout, QWidget, QFormLayout, QLineEdit, 
                             QMessageBox, QDialog)
from admin_panel import AdminPanel
from login_dialog import LoginDialog
from request_form import RequestForm

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

        self.button_admin_panel = QPushButton("Панель администратора", self)
        self.button_admin_panel.clicked.connect(self.open_admin_panel)

        self.button_login = QPushButton("Вход", self)
        self.button_login.clicked.connect(self.open_login_dialog)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.button_refresh)
        self.layout.addWidget(self.button_add_equipment)
        self.layout.addWidget(self.button_add_request)
        self.layout.addWidget(self.button_admin_panel)
        self.layout.addWidget(self.button_login)

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
        dialog = RequestForm(self)
        dialog.exec_()
        self.load_data()

    def edit_equipment(self, row, column):
        item_id = int(self.table.item(row, 0).text())
        dialog = EditEquipmentDialog(self, item_id)
        dialog.exec_()
        self.load_data()

    def open_admin_panel(self):
        admin_panel = AdminPanel(self)
        admin_panel.exec_()

    def open_login_dialog(self):
        login_dialog = LoginDialog(self)
        if login_dialog.exec_() == QDialog.Accepted:
            QMessageBox.information(self, "Успех", "Вы успешно вошли в систему.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
