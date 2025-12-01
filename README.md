# Laboratório Experimental - Sistemas de Informação ESPM

<p align="center">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>

# Transcrição de Áudio por IA

### 2025-02

## Integrantes
- [Rafael Arkchimor Lucena](https://github.com/rafaarklu)
- [Enzo Godoy](https://github.com/EnzoGodoy)

## Cliente do Projeto

ESPM

## Descrição do Projeto

Transcrição de áudio por IA.

## Como rodar (ambiente Python)

Se você estiver usando Windows, recomendamos criar um ambiente virtual para isolar dependências. Aqui está um exemplo usando a pasta `.venv` (essa pasta já está ignorada no repositório):

1. Criar o ambiente virtual (no terminal cmd.exe ou PowerShell):

   - cmd.exe:

    python -m venv .venv

   - PowerShell (Windows):

    python -m venv .venv

2. Ativar o ambiente virtual:

   - cmd.exe:

    .venv\Scripts\activate

   - PowerShell:

    . .venv\Scripts\Activate.ps1

3. Instalar dependências:

    pip install -r requirements.txt

4. Rodar a aplicação (exemplo):

    python main.py

Para desativar o ambiente virtual, execute:

    deactivate

Se você estiver usando outro shell (Git Bash / WSL / macOS / Linux), o comando de ativação normalmente é:

    source .venv/bin/activate

## OpenAI API key (necessária para transcrição de áudio)

O projeto usa a SDK OpenAI para transcrever áudio. Você precisa fornecer a sua chave de API por meio da variável de ambiente `OPENAI_API_KEY` (ou `API_KEY` como fallback). Não coloque chaves no código — mantenha-as nas variáveis de ambiente.

Exemplo (temporário, apenas para o terminal atual):

 - cmd.exe:

       set OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

 - PowerShell (temporário para sessão atual):

       $env:OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"

Se quiser salvar permanentemente no Windows, use `setx` (abre um novo terminal para o valor entrar em efeito):

    setx OPENAI_API_KEY "sk-xxxxxxxxxxxxxxxxxxxx"

Ao chamar as rotas que usam áudio, o código validará a presença dessa variável e mostrará uma mensagem clara se estiver ausente.


# Licença

Este projeto é licenciado sob a [MIT License](https://github.com/tech-espm/labs-transcricao-grupo-4/blob/main/LICENSE).

<p align="right">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo-si-512.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>
