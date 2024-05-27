#!/bin/bash

echo "Paketlarni yangilash..."
sudo apt-get update

echo $'\n\nKerakli paketlarni o‘rnatish...\n\n'
sudo apt-get install -y python3 python3-pip tesseract-ocr libtesseract-dev gnome-screenshot

echo $'\n\nPython kutubxonalarini o‘rnatish...\n\n'
sudo pip3 install pyautogui keyboard opencv-python pytesseract numpy configparser pynput

echo $'\n\nO‘rnatish muvaffaqiyatli amalga oshirildi.\n\n'

echo $'\n\nKalibrovka qilish skriptini ishlatish uchun quyidagi buyruqni ishlating:'
echo $'python3 calibrate.py\n\n'

echo "Kalibrovkadan so‘ng asosiy skriptni ishga tushirish uchun quyidagi buyruqdan foydalaning:"
echo "python3 click.py"