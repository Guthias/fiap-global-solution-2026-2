from models.ocorrencia import Ocorrencia, Status
from repository.CsvRepository import CsvRepository
from utils.exibir_card import exibir_card

csv_repo = CsvRepository()

def visualizar_ocorrencia(ocorrencia: Ocorrencia):
    while True:

        acoes_por_status = {
        Status.ABERTA: "   1 - Iniciar Análise",
        Status.EM_ANALISE: "   1 - Concluir Ocorrência",
        Status.CONCLUIDA: "   Ocorrência Concluída"
    }
        exibir_card("Exibindo Detalhes", ocorrencia.id, [
            "Detalhes da Ocorrência:",
            f"  Descrição: {ocorrencia.descricao}",
            f"  Local: {ocorrencia.local}",
            f"  Status: {ocorrencia.status.value}",
            f"  Data de Criação: {ocorrencia.data}",
            f"  Gravidade: {ocorrencia.gravidade.value if ocorrencia.gravidade else 'Não especificada'}",
            f"  Categoria: {ocorrencia.categoria.value if ocorrencia.categoria else 'Não especificada'}",
            "",
            "Interação:",
            acoes_por_status.get(ocorrencia.status, "\r"),
            "",
            "Navegação:",
            "   B - Voltar ao Menu de Pesquisa"
        ])

        opcao = input("\nEscolha uma opção: ")

        match opcao.upper():
            case "1":
                ocorrencia.atualizar_status(csv_repo)
            case "B":
                break