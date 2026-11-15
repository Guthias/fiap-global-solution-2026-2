
from utils.input_numero import input_numero
from utils.registros.arquivos import carregar_dados


def listar_ocorrencias():
    dados = carregar_dados()

    print("\n--- OCORRÊNCIAS ---")
    print("1 - Baixa")
    print("2 - Média")
    print("3 - Alta")
    print("4 - Todas")

    opcao = input_numero("\nEscolha uma opção: ")

    match opcao:
        case 1:
            gravidade = "media"
            gravidade = "baixa"

        case 2:
            gravidade = "media"

        case 3:
            gravidade = "alta"

        case 4:
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
            if ocorrencia["gravidade"].strip().lower() == gravidade
        ]

    if not ocorrencias:
        print("\nNenhuma ocorrência encontrada.")
        return

    print(f"\n--- RESULTADO: {gravidade or 'Todas'} ---")

    for ocorrencia in ocorrencias:
        print("\n-------------------------")
        print(f"ID: {ocorrencia['id']}")
        print(f"Categoria: {ocorrencia.get('categoria', 'Não informada')}")
        print(f"Descrição: {ocorrencia['descricao']}")
        print(f"Local: {ocorrencia['local']}")
        print(f"Data: {ocorrencia['data']}")
        print(f"Gravidade: {ocorrencia['gravidade']}")
        print(f"Status: {ocorrencia['status']}")
