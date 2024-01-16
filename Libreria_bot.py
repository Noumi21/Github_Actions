# Libreria_bot.py
import requests
import asyncio
from aiogram import Bot

async def check_port_status(url):
    try:
        response = requests.get(url, timeout=5)
        return True if response.status_code == 200 else False
    except requests.exceptions.RequestException as e:
        print(f"Error checking port status: {e}")
        return False

async def check_web_service(url):
    try:
        response = requests.get(url, timeout=5)
        return True if response.status_code == 200 else False
    except requests.exceptions.RequestException as e:
        print(f"Error checking web service: {e}")
        return False

async def send_telegram_message(api_token, chat_id, message):
    bot = Bot(token=api_token)

    try:
        await bot.send_message(chat_id=chat_id, text=message)
        print("Telegram message sent successfully.")
    except Exception as e:
        print(f"Error sending Telegram message: {e}")
    finally:
        await bot.session.close()

# Resto del código...