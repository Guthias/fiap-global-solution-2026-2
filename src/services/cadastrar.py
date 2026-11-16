
from models.ocorrencia import Ocorrencia
from repository.CsvRepository import CsvRepository
from services.classificacao import classificar_ocorrencia

csv_repo = CsvRepository()


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

    classificar_ocorrencia(nova_ocorrencia)

    csv_repo.adicionar_ocorrencia(nova_ocorrencia)

    print("\nOcorrência cadastrada com sucesso!")
