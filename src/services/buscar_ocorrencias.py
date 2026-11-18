from models.ocorrencia import Status
from repository.CsvRepository import CsvRepository
from services.exibir_ocorrencias_paginadas import exibir_ocorrencias_paginadas
from utils.exibir_card import exibir_card

csv_repo = CsvRepository()

def filtrar_ocorrencias_por_status(status):
    ocorrencias = csv_repo.listar_todos()
    
    ocorrencias_filtradas = [ocorrencia for ocorrencia in ocorrencias if ocorrencia.status == status]
    
    return ocorrencias_filtradas

def menu_busca_por_status():
    while True:
        exibir_card("Pesquisar Ocorrências por Status", "Escolha uma opção:", [
            "1. Aberta",
            "2. Em análise",
            "3. Concluída",
            "",
            "Navegação"
            "  B - Voltar ao Menu de Pesquisa"
        ])

        opcao = input("Digite a opção desejada: ")
        ocorrencias = []

        match opcao.upper():
            case "1":
                ocorrencias = filtrar_ocorrencias_por_status(Status.ABERTA)
            case "2":
                ocorrencias = filtrar_ocorrencias_por_status(Status.EM_ANALISE)
            case "3":
                ocorrencias = filtrar_ocorrencias_por_status(Status.CONCLUIDA)

            case "B":
                break

        exibir_ocorrencias_paginadas(ocorrencias, "Escolha uma ocorrencia para exibir mais detalhes:", "Resultado da Pesquisa")

def buscar_ocorrencias():
    while True:
        exibir_card("Pesquisar Ocorrências", "Escolha uma opção:", [
            "1. Pesquisar Todas",
            "2. Pesquisar por Status",
            "",
            "Navegação",
            "  B - Voltar ao Menu Principal"
        ])

        opcao = input("Digite a opção desejada: ")

        match opcao:
            case "1":
                ocorrencias = csv_repo.listar_todos()
                exibir_ocorrencias_paginadas(
                    ocorrencias=ocorrencias,
                    mensagem="Mostrando todas as ocorrencias")

            case "2":
                menu_busca_por_status()

            case "B":
                break

            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.\n")