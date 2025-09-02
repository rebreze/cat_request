@echo off

echo ==============================
echo Установка библиотеки requests
echo ==============================
python -m pip install --user requests

echo.
echo ------------------------------
echo Запуск скрипта cat_facts.py
echo ------------------------------
python cat_facts.py

pause
