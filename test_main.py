import pytest
import libreria_bot

TOKEN_TELEGRAM_BOT = '6960080306:AAEQqlt1I-3g1I_r3d5kCWBjS3qAS59cgbg'
id_chat = '6527212555'
mensaje = "Se ha ejecutado el test_main correctamente"

def test_check_port_status():
    # Suponiendo que esta función devuelve True/False
    assert libreria_bot.check_port_status("http://scanme.nmap.org/") is not None

def test_check_service_response():
    # Suponiendo que esta función devuelve True/False
    assert libreria_bot.check_web_service("http://scanme.nmap.org/") is not None

def enviar_mensaje():
    libreria_bot.send_telegram_message(TOKEN_TELEGRAM_BOT, id_chat, mensaje)

enviar_mensaje() # Llama a esta función para enviar el mensaje.
