import json
from pathlib import Path

CAMINHO_JSON = Path(__file__).resolve().parents[3] / "data" / "ocorrencias.json"


def carregar_dados():
    with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_dados(dados):
    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)