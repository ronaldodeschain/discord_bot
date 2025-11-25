# Projeto de Bot para Discord em Python

Este é um projeto de um bot para Discord desenvolvido em Python, utilizando a biblioteca `discord.py`. O bot é projetado para interagir com usuários, gerenciar o servidor e, potencialmente, tocar áudio em canais de voz.

## Funcionalidades (Exemplo)

*   **Comandos de Interação:** Responde a comandos básicos dos usuários.
*   **Gerenciamento de Áudio:** Capaz de entrar em canais de voz e tocar música (baseado na dependência `audioop-lts`).
*   **Configuração Segura:** Utiliza um arquivo `.env` para carregar o token do bot, mantendo-o seguro e fora do código-fonte.

## Pré-requisitos

*   Python 3.8 ou superior
*   Pip (gerenciador de pacotes do Python)
*   Uma conta no Discord e um token de bot. Você pode criar um aqui.

## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento local.

1.  **Clone o repositório:**
    ```bash
    git clone <URL-DO-SEU-REPOSITORIO>
    cd <NOME-DO-DIRETORIO>
    ```

2.  **Crie e ative um ambiente virtual:**
    *   **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas Python necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione o token do seu bot.
    ```
    DISCORD_TOKEN=SEU_TOKEN_DO_DISCORD_AQUI
    ```

## Como Executar

Após a instalação, você pode iniciar o bot com o seguinte comando (supondo que o arquivo principal se chame `bot.py`):

```bash
python bot.py
