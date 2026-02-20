import os
import requests
from dotenv import load_dotenv

load_dotenv()

def testar_envio():
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    mensagem = "🚀 Teste de automação: O bot da Compesa está online!"

    if not token or not chat_id:
        print("❌ Erro: Verifique se o arquivo .env tem o TOKEN e o CHAT_ID corretamente.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensagem,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=payload)
        resultado = response.json()
        
        if resultado.get("ok"):
            print("✅ Mensagem enviada com sucesso para o Telegram!")
        else:
            print(f"❌ Erro na API do Telegram: {resultado.get('description')}")
            
    except Exception as e:
        print(f"❌ Ocorreu um erro na requisição: {e}")

if __name__ == "__main__":
    testar_envio()