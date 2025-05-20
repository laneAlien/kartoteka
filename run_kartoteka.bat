@echo off
setlocal

echo 🧪 Проверка Docker...
docker info >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ Docker не запущен!
    pause
    exit /b
)

cd /d %~dp0

echo 🔄 Удаление старого контейнера...
docker-compose down

echo 🧱 Сборка образа...
docker-compose build

echo 🐘 Запуск PostgreSQL и API...
docker-compose up -d db web

echo ⏳ Ожидание запуска сервера...
timeout /t 5 >nul

echo 🚀 Запуск клиента...
start "" "%~dp0dist\kartoteka.exe"
