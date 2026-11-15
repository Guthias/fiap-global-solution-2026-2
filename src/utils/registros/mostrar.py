import json

def carregar_dados():
    with open("../data/ocorrencias.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados


def listar_ocorrencias():
    dados = carregar_dados()

    print("\nQual gostaria de ver?")
    print("1 - Baixa")
    print("2 - Média")
    print("3 - Alta")
    print("4 - Todas")

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            gravidade = "Baixa"

        case "2":
            gravidade = "Media"

        case "3":
            gravidade = "Alta"

        case "4":
            gravidade = None

        case _:
            print("Opção inválida!")
            return

    if gravidade is None:
        ocorrencias = dados["ocorrencias"]
    else:
        ocorrencias = [
            ocorrencia
            for ocorrencia in dados["ocorrencias"]
            if ocorrencia["gravidade"].lower() == gravidade
        ]

    if not ocorrencias:
        print("Nenhuma ocorrência encontrada.")
        return

    for ocorrencia in ocorrencias:
        print(f"\nID: {ocorrencia['id']}")
        print(f"Descrição: {ocorrencia['descricao']}")
        print(f"Local: {ocorrencia['local']}")
        print(f"Data: {ocorrencia['data']}")
        print(f"Gravidade: {ocorrencia['gravidade']}")
        print(f"Status: {ocorrencia['status']}")