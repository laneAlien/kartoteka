## ✅ Обновлённый `README.md`

```markdown
# 📦 Картотека

**Картотека** — это настольное клиент-серверное приложение на Python для учёта оборудования и заявок на ремонт.  
Использует: `PyQt5` (GUI), `Flask` (API), `PostgreSQL` (данные), `Docker` (среда).

---

## 🧱 Структура проекта

```

kartoteka/
├── client/              # 🖥️ Интерфейс PyQt5
│   ├── main\_window\.py
│   ├── login\_dialog.py
│   ├── request\_form.py
│   ├── admin\_panel.py
│   └── ...
├── core/                # 🧠 Бизнес-логика (валидация, утилиты)
│   ├── validators.py
│   ├── utils.py
├── data/                # 💾 ORM-модели и репозитории
│   ├── models.py
│   ├── repository.py
├── server/              # 🌐 Flask API
│   └── app.py
├── report/              # 📊 Отчёты (PDF, Excel)
│   ├── pdf\_export.py
│   ├── excel\_export.py
├── tests/               # 🧪 Тесты
│   └── test\_equipment.py
├── dist/                # 🧰 Скомпилированный .exe клиент (через PyInstaller)
├── docker/              # 🐳 Dockerfile, docker-compose.yml
├── run\_kartoteka.bat    # 🛠️ Батник: запускает всё сразу
├── requirements.txt     # 📦 Зависимости pip
└── README.md

````

---

## 🚀 Быстрый запуск (разработчику)

### 1. Клонировать проект

```bash
git clone https://github.com/yourname/kartoteka.git
cd kartoteka
````

### 2. Установить зависимости (без Docker)

```bash
python -m venv venv
venv\Scripts\activate        # Windows
venv\\Scripts\\activate.bat  # Или
pip install -r requirements.txt
```

### 3. Запустить PostgreSQL и API-сервер

```bash
   docker-compose up --build
   docker-compose up -d db
python server/app.py        # Запуск Flask API
```

### 4. Запустить GUI

```bash
python client/main_window.py
```

---

## 📦 Запуск в режиме "всё-в-одном" (пользователю)

1. Убедитесь, что установлен [Docker Desktop](https://www.docker.com/products/docker-desktop)

2. Запустите:

```bash
run_kartoteka.bat
```

Этот файл поднимает контейнеры и запускает GUI `kartoteka.exe`.

---

## 🧪 Тестирование

```bash
python -m unittest discover -s tests
```

---

## 📜 Лицензия

Проект доступен под MIT License. Используйте и дорабатывайте свободно.

```
