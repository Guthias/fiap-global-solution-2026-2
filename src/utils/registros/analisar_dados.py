import json

def carregar_dados():
    with open("../data/ocorrencias.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados

def analisar_dados():
    dados = carregar_dados
    ocorrencias = dados["ocorrencias"]

    total = len(ocorrencias)

    if total == 0:
        print("Nenhuma ocorrência cadastrada")
        return

    print(f"\nTotal de ocorrências: {total}")
