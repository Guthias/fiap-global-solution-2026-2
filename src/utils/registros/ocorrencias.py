
import json


def carregar_dados():
    with open("../data/ocorrencias.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados


def salvar_dados(dados):
    with open("../data/ocorrencias.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def cadastrar_ocorrencia():
    ...