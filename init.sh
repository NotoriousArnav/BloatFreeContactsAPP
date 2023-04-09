#!/usr/bin/env bash

echo "[+] Installing Dependencies"
sleep 1
python3 -m pip install -r requirements.txt
echo "[+] Making Database"
sleep 1
python3 manage.py migrate
echo "[+] Creating Admin Account"
sleep 1
python3 manage.py createsuperuser
