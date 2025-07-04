@echo off
echo Simulating Gunicorn Deployment...
REM In real Linux deployment: gunicorn feedback_portal.wsgi:application
REM We simulate by running Django server instead
call .venv\Scripts\activate.bat
python manage.py runserver 0.0.0.0:8000
