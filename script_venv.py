import os
import sys
import subprocess

def criar_ambiente(diretorio_projeto):
    venv_path = os.path.join(diretorio_projeto, 'venv')

    if not os.path.exists(diretorio_projeto):
        print(" O diretório informado não existe.")
        return

    if os.path.exists(venv_path):
        print("  O ambiente virtual já existe.")
        return

    try:
        subprocess.run([sys.executable, '-m', 'venv', venv_path], check=True)
        print(" Ambiente virtual criado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f" Erro ao criar o ambiente virtual: {e}")

def instalar_dependencias(diretorio_projeto, requirements_file):
    venv_pip = os.path.join(diretorio_projeto, 'venv', 'Scripts', 'pip.exe')

    if not os.path.exists(requirements_file):
        print(" O arquivo requirements.txt não foi encontrado.")
        return

    try:
        subprocess.run([venv_pip, 'install', '-r', requirements_file], check=True)
        print(" Dependências instaladas com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f" Erro ao instalar dependências: {e}")

def executar_projeto(diretorio_projeto, script_principal):
    venv_python = os.path.join(diretorio_projeto, 'venv', 'Scripts', 'python.exe')

    if not os.path.exists(venv_python):
        print(" O ambiente virtual não existe. Crie primeiro.")
        return

    try:
        subprocess.run([venv_python, script_principal], check=True)
        print("✅ Projeto executado dentro do ambiente virtual.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o projeto: {e}")

if __name__ == "__main__":
    diretorio = os.path.dirname(os.path.abspath(__file__))
    req = os.path.join(diretorio, 'requirements.txt')
    script = os.path.join(diretorio, 'teste.py')

    criar_ambiente(diretorio)
    instalar_dependencias(diretorio, req)
    executar_projeto(diretorio, script)
