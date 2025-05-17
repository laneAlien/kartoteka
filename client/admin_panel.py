from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem

class AdminPanel(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Панель администратора")
        self.setGeometry(200, 200, 600, 400)

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Панель администратора", self)
        self.layout.addWidget(self.label)

        self.table = QTableWidget(self)
        self.layout.addWidget(self.table)

        self.button_refresh = QPushButton("Обновить", self)
        self.button_refresh.clicked.connect(self.load_data)
        self.layout.addWidget(self.button_refresh)

        self.load_data()

    def load_data(self):
        # Здесь можно добавить логику для загрузки данных
        pass
