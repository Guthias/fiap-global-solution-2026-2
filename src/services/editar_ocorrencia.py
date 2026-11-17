
from repository.CsvRepository import CsvRepository
from utils.exibir_card import exibir_card
from models.ocorrencia import Status, Gravidade


csv_repo = CsvRepository()


def editar_ocorrencia():
    ocorrencias = csv_repo.listar_todos()

    if not ocorrencias:
        exibir_card(
            "EDITAR OCORRÊNCIA",
            "AVISO",
            ["Nenhuma ocorrência cadastrada."]
        )
        return

    conteudo = []

    for ocorrencia in ocorrencias:
        conteudo.append(f"ID: {ocorrencia.id[:8]}")
        conteudo.append(f"Descrição: {ocorrencia.descricao}")
        conteudo.append(f"Local: {ocorrencia.local}")
        conteudo.append("")

    exibir_card(
        "EDITAR OCORRÊNCIA",
        "OCORRÊNCIAS CADASTRADAS",
        conteudo
    )

    identificador = input(
        "\nDigite o ID da ocorrência que deseja editar: "
    )

    ocorrencias_encontradas = [
        ocorrencia for ocorrencia in ocorrencias
        if ocorrencia.id.startswith(identificador)
    ]

    if len(ocorrencias_encontradas) == 0:
        print("Ocorrência não encontrada.")
        return

    if len(ocorrencias_encontradas) > 1:
        print("Mais de uma ocorrência encontrada. Digite mais caracteres do ID.")
        return

    ocorrencia_selecionada = ocorrencias_encontradas[0]

    exibir_card(
        "EDITAR OCORRÊNCIA",
        "REGISTRO SELECIONADO",
        [
            f"ID: {ocorrencia_selecionada.id[:8]}",
            f"Descrição: {ocorrencia_selecionada.descricao}",
            f"Local: {ocorrencia_selecionada.local}"
        ]
    )

    exibir_card(
        "EDITAR OCORRÊNCIA",
        "ALTERAR STATUS",
        [
            "1. Aberta",
            "2. Em análise",
            "3. Concluída",
            "",
            "0. Cancelar"
        ]
    )

    opcao = input("Escolha o novo status: ")

    match opcao:
        case "1":
            ocorrencia_selecionada.status = Status.ABERTA

        case "2":
            ocorrencia_selecionada.status = Status.EM_ANALISE

        case "3":
            ocorrencia_selecionada.status = Status.CONCLUIDA

        case "0":
            return

        case _:
            print("Opção inválida.")
            return

    exibir_card(
        "EDITAR OCORRÊNCIA",
        "ALTERAR GRAVIDADE",
        [
            "1. Baixa",
            "2. Média",
            "3. Alta",
            "4. Crítica",
            "",
            "0. Cancelar"
        ]
    )

    opcao = input("Escolha a nova gravidade: ")

    match opcao:
        case "1":
            ocorrencia_selecionada.gravidade = Gravidade.BAIXA

        case "2":
            ocorrencia_selecionada.gravidade = Gravidade.MEDIA

        case "3":
            ocorrencia_selecionada.gravidade = Gravidade.ALTA

        case "4":
            ocorrencia_selecionada.gravidade = Gravidade.CRITICA

        case "0":
            return

        case _:
            print("Opção inválida.")
            return

    csv_repo.atualizar_ocorrencia(ocorrencia_selecionada)

    exibir_card(
        "EDIÇÃO CONCLUÍDA",
        "DADOS ATUALIZADOS",
        [
            f"Status: {ocorrencia_selecionada.status.value}",
            f"Gravidade: {ocorrencia_selecionada.gravidade.value}"
        ]
    )
