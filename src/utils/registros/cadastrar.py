
import json
from datetime import datetime


def carregar_dados():
    with open("../data/ocorrencias.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados


def salvar_dados(dados):
    with open("../data/ocorrencias.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def verificar_data():
    while True:
        data = input("Digite a data (DD/MM/AAAA): ")

        try:
            data_formatada = datetime.strptime(data, "%d/%m/%Y")
            return data_formatada.strftime("%Y-%m-%d")

        except ValueError:
            print("Data inválida! Tente novamente.")


def identificar_gravidade(descricao):

    descricao = descricao.lower()

    palavras_altas = [
        "risco", "acidente", "perigo",
        "fio caido", "bueiro aberto"
    ]

    palavras_medias = [
        "buraco", "lampada queimada",
        "calcada quebrada"
    ]

    for palavra in palavras_altas:
        if palavra in descricao:
            return "Alta"

    for palavra in palavras_medias:
        if palavra in descricao:
            return "Media"

    return "Baixa"

def solicitar_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Este campo não pode ficar vazio!")

def cadastrar_ocorrencia():
    dados = carregar_dados()

    descricao = solicitar_texto("Digite o que aconteceu: ")
    local = solicitar_texto("Digite o local: ")

    gravidade = identificar_gravidade(descricao)
    data = verificar_data()

    dados["ultimo_id"] += 1
    novo_id = str(dados["ultimo_id"]).zfill(3)

    nova_ocorrencia = {
        "id": novo_id,
        "descricao": descricao,
        "local": local,
        "data": data,
        "gravidade": gravidade,
        "status": "em analise"
    }

    dados["ocorrencias"].append(nova_ocorrencia)

    salvar_dados(dados)

    print("\nOcorrência cadastrada com sucesso!")
    print(f"Gravidade identificada: {gravidade}")
