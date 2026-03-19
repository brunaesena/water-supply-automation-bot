# 🚰 Automação de Abastecimento Compesa (Recife/PE)

Este projeto automatiza a consulta ao calendário de abastecimento de água da Compesa via Web Scraping e envia um cronograma semanal detalhado diretamente para o Telegram.

## 🚀 Como funciona
O script utiliza **Python** com **Playwright** para navegar no mapa interativo (ArcGIS) da Compesa, identifica as classes CSS de cada dia (Normal, Parcial ou Manutenção) e dispara uma mensagem formatada via **Telegram Bot API**.

A execução é 100% gratuita e automatizada através do **GitHub Actions**, rodando todos os dias às 07:00 (Horário de Recife).

## 🛠️ Tecnologias
* [Python 3.10+](https://www.python.org/)
* [Playwright](https://playwright.dev/python/) (Navegação dinâmica)
* [GitHub Actions](https://github.com/features/actions) (Cron job & CI/CD)
* [Telegram Bot API](https://core.telegram.org/bots/api) (Notificações)

## 📋 Pré-requisitos para Replicar
Se você deseja rodar este bot para o seu endereço:

1. **Bot no Telegram:**
   - Fale com o `@BotFather` para criar um bot e obter o `TELEGRAM_TOKEN`.
   - Use o `@userinfobot` para descobrir seu `TELEGRAM_CHAT_ID`.
   - **Importante:** Envie um `/start` para o seu novo bot antes de testar.

2. **Configuração Local:**
   - Clone o repositório.
   - Crie um arquivo `.env` na raiz com suas credenciais:
     ```env
     TELEGRAM_TOKEN=seu_token_aqui
     TELEGRAM_CHAT_ID=seu_id_aqui
     ```
   - Instale as dependências:
     ```bash
     pip install -r requirements.txt
     playwright install chromium
     ```

3. **Deploy Automatizado:**
   - Suba o código para o seu GitHub.
   - Vá em **Settings > Secrets and variables > Actions** e adicione as duas chaves (`TELEGRAM_TOKEN` e `TELEGRAM_CHAT_ID`) como **Repository Secrets**.
   - O fluxo será ativado automaticamente conforme definido em `.github/workflows/daily_check.yml`.

## 🔍 Lógica de Captura (The "Cracking" Logic)
A automação diferencia os estados de abastecimento através das classes CSS das células do calendário:
* `specialdate`: 🔵 Abastecimento Normal
* `intervensao-a`: 💧 Abastecimento Parcial
* `intervensao`: 🔴 Sistema em Manutenção
* Sem classe: ⚪ Sem Abastecimento

---
Desenvolvido por Bruna Sena como um projeto de utilidade pública e estudo de Web Scraping.