from models.ocorrencia import Ocorrencia
from utils.exibir_card import exibir_card


def visualizar_ocorrencia(ocorrencia: Ocorrencia):
    while True:
        exibir_card("Exibindo Detalhes", ocorrencia.id, [
            "Detalhes da Ocorrência:",
            f"  Descrição: {ocorrencia.descricao}",
            f"  Local: {ocorrencia.local}",
            f"  Status: {ocorrencia.status.value}",
            f"  Data de Criação: {ocorrencia.data}",
            f"  Gravidade: {ocorrencia.gravidade.value if ocorrencia.gravidade else 'Não especificada'}",
            f"  Categoria: {ocorrencia.categoria.value if ocorrencia.categoria else 'Não especificada'}",
            "",
            "Navegação:",
            "   B - Voltar ao Menu de Pesquisa"
        ])

        opcao = input("\nEscolha uma opção: ")

        match opcao.upper():
            case "B":
                break