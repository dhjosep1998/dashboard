import sys
import os
import subprocess
import venv

def criar_ambiente(diretorio_projeto):
    if not os.path.exists(diretorio_projeto):
        print("O diretório informado não existe")
        return
    
    venv_path = os.path.join(diretorio_projeto, 'venv')
    if os.path.exists(venv_path):
        print("Ambiente virtual já existe.")
        return

    try:
        venv.create(venv_path, with_pip=True)
        print("Ambiente virtual criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar o ambiente virtual: {e}")


def instalar_dependencias(diretorio_projeto, requirements_file):
    if not os.path.exists(requirements_file):
        print("O arquivo requirements.txt não foi encontrado.")
        return
    
    
    if os.name == 'nt': 
        pip_path = os.path.join(diretorio_projeto, 'venv', 'Scripts', 'pip.exe')
    else: #linux 
        pip_path = os.path.join(diretorio_projeto, 'venv', 'bin', 'pip')

    try:
        subprocess.run([pip_path, 'install', '-r', requirements_file], check=True)
        print("Dependências instaladas com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar dependências: {e}")


def main():
    diretorio_projeto = sys.argv[1]
    requirements_file = os.path.join(diretorio_projeto, 'requirements.txt') 
    criar_ambiente(diretorio_projeto)
    instalar_dependencias(diretorio_projeto, requirements_file)


if __name__ == "__main__":
    main()
