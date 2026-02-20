# 🚰 Automação de Abastecimento Compesa

## 1. Objetivo
O objetivo deste projeto é automatizar a verificação do calendário de abastecimento de água para uma rua específica no portal da Compesa (Recife/PE). A automação deve realizar a consulta diariamente, extrair os dados de abastecimento da semana e enviar uma notificação para o usuário.

## 2. Arquitetura e Tecnologias

Para garantir que o projeto seja **100% gratuito** e de fácil manutenção, a seguinte stack foi definida:

* **Linguagem:** [Python 3.x](https://www.python.org/)
* **Web Scraping:** [Playwright](https://playwright.dev/python/) ou [Selenium](https://www.selenium.dev/)
    * *Justificativa:* O site utiliza ArcGIS (mapas dinâmicos), exigindo a renderização de JavaScript para que os elementos de busca e o popup de calendário fiquem visíveis.
* **Hospedagem / CI/CD:** [GitHub Actions](https://github.com/features/actions)
    * *Justificativa:* Permite a execução de scripts agendados (cron jobs) de forma gratuita em repositórios públicos ou privados (dentro da cota mensal).
* **Notificação:** [Telegram Bot API](https://core.telegram.org/bots/api)
    * *Justificativa:* Gratuito, simples de implementar via requests e permite o envio de mensagens formatadas.

---

## 3. Fluxo de Execução (Workflow)

1.  **Trigger:** O GitHub Actions dispara o script diariamente em um horário pré-definido (ex: 07:00 BRT).
2.  **Navegação:** * O script acessa a URL do calendário da Compesa.
    * Interage com o campo de busca (`#search_input`).
    * Insere o endereço configurado e seleciona a sugestão correspondente.
3.  **Extração:**
    * O script aguarda a renderização do popup/tooltip do calendário.
    * Captura as informações de status (Ex: "Abastecimento Parcial", "Sistema em Manutenção") para a data atual ou semana.
4.  **Notificação:**
    * O script formata os dados capturados.
    * Envia a mensagem via HTTP Post para o Bot do Telegram.

---

## 4. Estrutura do Projeto (Sugestão)

```text
├── .github/
│   └── workflows/
│       └── daily_check.yml  # Configuração do agendamento
├── src/
│   ├── scraper.py           # Lógica de navegação e extração
│   └── notifier.py          # Integração com API do Telegram
├── requirements.txt         # Dependências (playwright, requests, etc.)
└── .env.example             # Exemplo de variáveis de ambiente (Token, ChatID)
```

## 5. Variáveis de Ambiente Necessárias

* Para segurança e versionamento, os seguintes dados devem ser configurados nos Secrets do repositório GitHub:

- TELEGRAM_TOKEN: Token gerado pelo @BotFather.

- TELEGRAM_CHAT_ID: ID do chat ou grupo que receberá a mensagem.

- TARGET_ADDRESS: O endereço completo a ser pesquisado no mapa.

## 6. Próximos Passos

[ X ] Criar o Bot no Telegram e obter o Token e ChatID.

[ ] Desenvolver o script de scraping localmente (modo headed).

[ ] Mapear os seletores CSS/XPath dos elementos do calendário.

[ ] Configurar o Workflow do GitHub Actions para execução headless.

Nota: Este é um projeto de uso pessoal para fins de estudo e utilidade doméstica.