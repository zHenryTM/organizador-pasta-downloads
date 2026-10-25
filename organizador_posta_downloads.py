import os
import shutil
from pathlib import Path

downloads = Path.home() / "Downloads"  # Caminho para pasta "Downloads"
extensoes = []
arquivos = os.listdir(os.fsencode(downloads))  # Lista com todos os arquivos contidos em "Downloads"

for arquivo in arquivos:
    arquivo = os.fsdecode(arquivo)
    extensao = Path(arquivo).suffix[1:].upper()
    
    if (extensao not in extensoes):
        extensoes.append(extensao)

for extensao in extensoes:
    try:
        os.mkdir(f"{downloads}/{extensao}")  # Cria uma pasta em "Downloads" com o nome da extensão
    except FileExistsError:
        print("A pasta já existe. Continuar algoritmo normalmente")

for arquivo in arquivos:
    arquivo = os.fsdecode(arquivo)
    origem = downloads / arquivo
    
    if (os.path.isfile(origem)):  # Evita que pastas sejam movidas para dentro de outras pastas
        extensao = Path(arquivo).suffix[1:].upper()
        destino = downloads / extensao / arquivo
        
        shutil.move(origem, destino)
