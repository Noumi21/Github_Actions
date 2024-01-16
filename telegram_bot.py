# Telegram_bot.py

import asyncio
from libreria_bot import check_port_status, check_web_service, send_telegram_message

async def main():
    url = "http://scanme.nmap.org/"
    interval = 300  # Intervalo entre pruebas en segundos (en este caso, 5 minutos)
    api_token = "6960080306:AAEQqlt1I-3g1I_r3d5kCWBjS3qAS59cgbg"
    chat_id = "6527212555"

    if not await check_port_status(url):
        await send_telegram_message(api_token, chat_id, "El puerto del servicio web no responde o está cerrado.")
    elif not await check_web_service(url):
        await send_telegram_message(api_token, chat_id, "El servicio web responde, pero el servicio web está inactivo.")
    else:
        await send_telegram_message(api_token, chat_id, "El servicio web responde correctamente")

if __name__ == "__main__":
    asyncio.run(main())
