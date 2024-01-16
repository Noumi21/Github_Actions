import pytest
import monitor

TOKEN_TELEGRAM_BOT = '6960080306:AAEQqlt1I-3g1I_r3d5kCWBjS3qAS59cgbg'
id_chat = '6527212555'
mensaje = "Se ha ejecutado el test_main correctamente"

def test_check_port_status():
    # Suponiendo que esta función devuelve True/False
    assert monitor.check_port_status("http://scanme.nmap.org/") is not None

def test_check_service_response():
    # Suponiendo que esta función devuelve True/False
    assert monitor.check_service_response("http://scanme.nmap.org/") is not None

Aquí puedes agregar más pruebas para las funciones específicas en monitor.py
Variables no definidas: TOKEN_TELEGRAM_BOT, id_chat, y mensaje.
Asegúrate de que estén definidas correctamente en tu código.
Si necesitas enviar un mensaje de manera asíncrona, debes hacerlo dentro de una función asíncrona.
Por ejemplo:
def enviar_mensaje():
    monitor.enviar_mensaje_telegram(TOKEN_TELEGRAM_BOT, id_chat, mensaje)

enviar_mensaje() # Llama a esta función para enviar el mensaje.
