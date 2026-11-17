from models.ocorrencia import Categoria, Ocorrencia, Status
from models.ocorrencia import Gravidade
from repository.CsvRepository import CsvRepository
from utils.exibir_card import exibir_card

csv_repo = CsvRepository()

def menu_editar_gravidade(ocorrencia: Ocorrencia):
    while True:
        exibir_card("Editar Gravidade", ocorrencia.id, [
            "Escolha a nova gravidade:",
            "   1 - Baixa",
            "   2 - Média",
            "   3 - Alta",
            "   4 - Crítica",
            "",
            "Navegação:",
            "   B - Voltar"
        ])

        opcao = input("\nEscolha uma opção: ")

        match opcao.upper():
            case "1":
                ocorrencia.atualizar_gravidade(Gravidade.BAIXA, csv_repo)
                break

            case "2":
                ocorrencia.atualizar_gravidade(Gravidade.MEDIA, csv_repo)
                break

            case "3":
                ocorrencia.atualizar_gravidade(Gravidade.ALTA, csv_repo)
                break

            case "4":
                ocorrencia.atualizar_gravidade(Gravidade.CRITICA, csv_repo)
                break

            case "B":
                break

def menu_editar_categoria(ocorrencia: Ocorrencia):
    while True:
        exibir_card("Editar Categoria", ocorrencia.id, [
            "Escolha a nova categoria:",
            "   1 - Segurança",
            "   2 - Saúde",
            "   3 - Meio Ambiente",
            "   4 - Infraestrutura",
            "",
            "Navegação:",
            "   B - Voltar"
        ])

        opcao = input("\nEscolha uma opção: ")

        match opcao.upper():
            case "1":
                ocorrencia.atualizar_categoria(Categoria.SEGURANCA, csv_repo)
                break

            case "2":
                ocorrencia.atualizar_categoria(Categoria.SAUDE, csv_repo)
                break

            case "3":
                ocorrencia.atualizar_categoria(Categoria.MEIO_AMBIENTE, csv_repo)
                break

            case "4":
                ocorrencia.atualizar_categoria(Categoria.INFRAESTRUTURA, csv_repo)
                break

            case "B":
                break

def visualizar_ocorrencia(ocorrencia: Ocorrencia):
    while True:

        acoes_por_status = {
            Status.ABERTA: "  1 - Iniciar Análise",
            Status.EM_ANALISE: "  1 - Concluir Ocorrência",
            Status.CONCLUIDA: "  Ocorrência Concluída"
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
            "  2 - Editar Gravidade",
            "  3 - Editar Categoria",
            "  4 - Editar Descrição",
            "  5 - Editar Local",
            "",
            "Navegação:",
            "   B - Voltar ao Menu de Pesquisa"
        ])

        opcao = input("\nEscolha uma opção: ")

        match opcao.upper():
            case "1":
                ocorrencia.atualizar_status(csv_repo)

            case "2":
                menu_editar_gravidade(ocorrencia)

            case "3":
                menu_editar_categoria(ocorrencia)

            case "4":
                nova_descricao = input("Digite a nova descrição: ")
                ocorrencia.atualizar_descricao(nova_descricao, csv_repo)

            case "5":
                novo_local = input("Digite o novo local: ")
                ocorrencia.atualizar_local(novo_local, csv_repo)

            case "B":
                break