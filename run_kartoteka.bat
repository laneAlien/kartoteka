@echo off
echo Запуск базы и API...
cd /d %~dp0docker
docker-compose up -d

timeout /t 5

echo Запуск клиентского интерфейса...
start "" "%~dp0dist\kartoteka.exe"
