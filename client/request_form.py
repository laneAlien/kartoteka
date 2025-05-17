from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

class RequestForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Форма заявки на ремонт")
        self.setGeometry(200, 200, 300, 200)

        self.layout = QVBoxLayout(self)

        self.label_equipment_id = QLabel("ID оборудования:", self)
        self.layout.addWidget(self.label_equipment_id)

        self.equipment_id_input = QLineEdit(self)
        self.layout.addWidget(self.equipment_id_input)

        self.label_description = QLabel("Описание проблемы:", self)
        self.layout.addWidget(self.label_description)

        self.description_input = QLineEdit(self)
        self.layout.addWidget(self.description_input)

        self.button_submit = QPushButton("Отправить заявку", self)
        self.button_submit.clicked.connect(self.submit)
        self.layout.addWidget(self.button_submit)

    def submit(self):
        equipment_id = self.equipment_id_input.text()
        description = self.description_input.text()
        # Здесь должна быть логика отправки заявки
        QMessageBox.information(self, "Успех", "Заявка на ремонт отправлена.")
        self.accept()
