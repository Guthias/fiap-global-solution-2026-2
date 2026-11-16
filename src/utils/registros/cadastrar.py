
from uuid import uuid4

from models.ocorrencia import Ocorrencia
from repository.CsvRepository import CsvRepository

csv_repo = CsvRepository()

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
    descricao = solicitar_texto("Digite o que aconteceu: ")
    local = solicitar_texto("Digite o local: ")

    nova_ocorrencia = Ocorrencia(
        descricao=descricao,
        local=local,
    )

    csv_repo.adicionar_ocorrencia(nova_ocorrencia)

    print("\nOcorrência cadastrada com sucesso!")
