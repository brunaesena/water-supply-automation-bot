import os
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import requests

load_dotenv()

def enviar_telegram(mensagem):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": mensagem, "parse_mode": "Markdown"})

def executar_automacao_semanal():
    endereco = "Alto José do Pinho, Recife, Pernambuco"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("🌍 Acessando calendário da Compesa...")
        page.goto("https://giscomp.compesa.com.br/calendario.html", wait_until="networkidle")
        
        page.wait_for_selector("#search_input")
        page.fill("#search_input", endereco)
        page.keyboard.press("Enter")
        
        print("⏳ Aguardando processamento do mapa (7s)...")
        page.wait_for_timeout(7000)

        # Lógica JS baseada na descoberta das classes específicas
        dados_calendario = page.evaluate("""
            () => {
                const celulas = document.querySelectorAll('td.jqx-calendar-cell');
                const resultados = {};
                
                celulas.forEach(td => {
                    const dia = td.innerText.trim();
                    const classes = td.className.toLowerCase();
                    const isOtherMonth = classes.includes('other-month');
                    
                    if (dia && !isOtherMonth) {
                        let status = "⚪ Sem Abastecimento";

                        // A ordem aqui é fundamental para não haver sobreposição
                        if (classes.includes('specialdate')) {
                            status = "🔵 Abastecimento Normal";
                        } 
                        else if (classes.includes('intervensao-a')) {
                            status = "💧 Abastecimento Parcial";
                        }
                        else if (classes.includes('intervensao')) {
                            status = "🔴 Sistema em Manutenção";
                        }
                        
                        resultados[dia] = status;
                    }
                });
                return resultados;
            }
        """)

        hoje = datetime.now()
        dias_pt = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
        linhas_relatorio = []

        for i in range(7):
            data_alvo = hoje + timedelta(days=i)
            dia_str = str(data_alvo.day)
            dia_semana = dias_pt[data_alvo.weekday()]
            
            status = dados_calendario.get(dia_str, "⚪ Sem Info")
            linhas_relatorio.append(f"{dia_semana} - {dia_str.zfill(2)} - {status}")

        relatorio_final = "\n".join(linhas_relatorio)
        mensagem_completa = f"🚰 *Cronograma Compesa*\n📍 {endereco}\n\n{relatorio_final}"
        
        print("\n" + mensagem_completa)
        enviar_telegram(mensagem_completa)
        
        browser.close()

if __name__ == "__main__":
    executar_automacao_semanal()