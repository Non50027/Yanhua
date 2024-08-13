@echo off
if "%1"=="" ( goto start ) else ( goto %1 )

:-f
:freeze
pip freeze > requirements.txt
exit 0

:-i
:install 
pip install -r requirements.txt
exit 0

:-m
:migrate
python backend/manage.py makemigrations %2
python backend/manage.py migrate %2
exit 0

:start
python backend/manage.py makemigrations %2
python backend/manage.py migrate %2
python backend/manage.py runserver
timeout /t 5 /nobreak
goto start