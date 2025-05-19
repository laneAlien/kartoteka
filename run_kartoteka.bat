@echo off
echo Проверка Docker...
docker info >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ Docker не запущен!
    pause
    exit /b
)

cd /d %~dp0

echo 🛠 Сборка образов...
docker-compose build

echo 🐘 Запуск PostgreSQL...
docker-compose up -d db

timeout /t 5 >nul

echo 🚀 Запуск клиента...
start "" "%~dp0dist\kartoteka.exe"
