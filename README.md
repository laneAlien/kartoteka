### Полный файл для README.md

```markdown
# Картотека

## Описание
Проект "Картотека" представляет собой систему управления оборудованием и заявками на ремонт, реализованную с использованием Flask и PyQt5.

## Структура проекта
```
kartoteka/
├── client/              # PyQt5 GUI
│   ├── main_window.py
│   ├── login_dialog.py
│   ├── request_form.py
│   ├── admin_panel.py
├── core/                # Бизнес-логика
│   ├── validators.py
│   ├── utils.py
├── data/                # Репозитории
│   ├── repository.py
│   ├── models.py
├── server/              # Flask API
│   └── app.py
├── report/              # Генерация отчётов
│   ├── pdf_export.py
│   ├── excel_export.py
├── tests/               # Тесты
│   ├── test_equipment.py
├── venv/                # Виртуальное окружение (создано вами)
├── README.md            # Документация
├── requirements.txt     # Зависимости
└── docker-compose.yml    # Docker конфигурация (опционально)
```

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone <URL>
   cd kartoteka
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск сервера
Запустите сервер Flask:
```bash
python server/app.py
```

## Запуск клиента
Запустите GUI на PyQt5:
```bash
python client/main_window.py
```

## Тестирование
Запустите тесты:
```bash
python -m unittest discover -s tests
```

## Лицензия
Этот проект лицензирован под MIT License.
```

