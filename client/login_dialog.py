from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Вход")
        self.setGeometry(200, 200, 300, 150)

        self.layout = QVBoxLayout(self)

        self.label_username = QLabel("Имя пользователя:", self)
        self.layout.addWidget(self.label_username)

        self.username_input = QLineEdit(self)
        self.layout.addWidget(self.username_input)

        self.label_password = QLabel("Пароль:", self)
        self.layout.addWidget(self.label_password)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.button_login = QPushButton("Войти", self)
        self.button_login.clicked.connect(self.login)
        self.layout.addWidget(self.button_login)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        # Здесь должна быть логика проверки пользователя
        if username == "admin" and password == "password":  # Пример проверки
            self.accept()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль.")
