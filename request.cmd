@echo off
chcp 65001 >nul

echo ==============================
echo Установка библиотеки requests
echo ==============================
python -m pip install --user requests

echo.
echo ------------------------------
echo Запуск скрипта cat_requests.py
echo ------------------------------
echo.
python cat_requests.py
echo.
echo ------------------------------------------------------------------------------------------
echo.

pause
