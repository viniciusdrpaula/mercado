import random
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Variáveis de ambiente para Twilio
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER', 'whatsapp:+14155238886')

def send_message(phone, code):
    """
    Envia um código de ativação via WhatsApp para o número fornecido.
    :param phone: Número de telefone do destinatário (Ex: "+551199999999").
    :param code: Código de ativação a ser enviado.
    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Criar a mensagem
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=f'whatsapp:{phone}',
            body=f"Seu código de ativação é: {code}"
        )

        print(f"Mensagem enviada com sucesso! SID: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def generate_code():
    """
    Gera um código numérico aleatório de 4 dígitos.
    """
    return ''.join(str(random.randint(0, 9)) for _ in range(4))