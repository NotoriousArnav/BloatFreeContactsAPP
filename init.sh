#!/usr/bin/env bash

echo "[+] Installing Dependencies"
sleep 1
python3 -m pip install -r requirements.txt
echo "[+] Making Database"
sleep 1
python3 manage.py migrate
echo "[+] Creating Admin Account"
sleep 1
python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
echo "[+] Running the server with Gunicorn"
gunicorn contactsapp.wsgi:application
