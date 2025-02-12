# masalan shu botga start bossa men guruhlardagi yozishmalar yoki shaxsiydagilarni ko'ra olamanmi

# ChatGPT said:
# Ha, agar o‘zingizning Telegram akkauntingiz bilan ishlasangiz, Telethon yoki Pyrogram orqali guruhlardagi va shaxsiy chatlardagi yozishmalarni o‘qishingiz va saqlashingiz mumkin.

# Muhim eslatma:
# Faqat o‘z akkauntingiz yoki ruxsatingiz bo‘lgan bot orqali ishlashingiz mumkin. Boshqa odamlarning ma’lumotlarini ruxsatsiz olish Telegram qoidalariga va qonunga zid!

# Shaxsiy va guruhdagi xabarlarni olish (Telegram API orqali)
# Quyidagi Telethon kod shaxsiy chatlar va guruhlardagi yozishmalarni o‘qib beradi:

# 1. Telegram API uchun login qilish

from telethon.sync import TelegramClient

api_id = 123456  # O'zingizning API ID
api_hash = "abcdef1234567890abcdef1234567890"  # O'zingizning API Hash

with TelegramClient("session_name", api_id, api_hash) as client:
    me = client.get_me()
    print(f"✅ Logged in as {me.first_name}")

    # Shaxsiy chatlar va guruhlarni ko‘rish
    for dialog in client.iter_dialogs():
        print(f"📂 Chat: {dialog.name} | ID: {dialog.id}")

# 📌 Natija: Barcha chatlar va guruhlarni ko‘rish mumkin bo‘ladi.

# 2. Ma'lum bir chatdan xabarlarni olish

chat_id = input("Chat yoki guruh ID sini kiriting: ")

with TelegramClient("session_name", api_id, api_hash) as client:
    messages = client.get_messages(chat_id, limit=10)  # Oxirgi 10 ta xabarni olish
    for message in messages:
        print(f"{message.sender_id}: {message.text}")

# 📌 Natija: Kiritilgan chat yoki guruh ID dagi oxirgi 10 ta xabarni ko‘rasiz.

# 3. Barcha guruhlardan yozishmalarni olish va saqlash
with TelegramClient("session_name", api_id, api_hash) as client:
    for dialog in client.iter_dialogs():
        if dialog.is_group:  # Faqat guruhlarni olish
            print(f"📂 Guruh: {dialog.name} | ID: {dialog.id}")
            messages = client.get_messages(dialog.id, limit=5)  # Oxirgi 5 xabar
            for message in messages:
                print(f"📩 {message.sender_id}: {message.text}")

# 📌 Natija: Barcha guruhlardagi oxirgi 5 ta xabarni o‘qib beradi.

# Avtomatik xabar monitoring qilish (Live kuzatish)
# Agar siz real vaqt rejimida xabarlarni olishni xohlasangiz, handler qo‘shish kerak:

from telethon import TelegramClient, events

api_id = 123456
api_hash = "abcdef1234567890abcdef1234567890"

client = TelegramClient("session_name", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    print(f"📩 {event.chat_id}: {event.text}")

client.start()
print("✅ Telegram bot ishga tushdi...")
client.run_until_disconnected()

# 📌 Natija: Barcha chatlardagi har bir yangi xabarni real vaqtda ko‘rish mumkin bo‘ladi.

# Qo‘shimcha imkoniyatlar
# O‘z guruhingiz yoki kanalingizni boshqarish
# Avtomatik xabar yuborish
# Guruhdagi spamlarni filtr qilish
# Xabarlarni CSV yoki JSON ga saqlash
# Qaysi yo‘nalishda davom etamiz? 🚀








# Pentesting uchun foydali metodlar
# Telethon orqali guruhlardagi xabarlarni olish

async for message in client.iter_messages("group_name"):
    print(message.text)

# Pyrogram orqali foydalanuvchi haqidagi ma'lumotlarni olish
user = app.get_users("username")
print(user.id, user.first_name, user.last_name)

# Aiogram orqali botga kelgan xabarlarni logga yozish
@dp.message_handler()
async def log_message(message: types.Message):
    print(f"{message.from_user.id}: {message.text}")
