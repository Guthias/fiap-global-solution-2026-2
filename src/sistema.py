from services.buscar_ocorrencias import buscar_ocorrencias
from utils.exibir_card import exibir_card
from services.cadastrar import cadastrar_ocorrencia
from services.analisar_dados import analisar_dados

def menu_principal():
    exibir_card("Seja Bem-vindo!", "Escolha uma opção:", [
        "1. Cadastrar nova Ocorrência",
        "2. Pesquisar Ocorrências",
        "3. Analisar Ocorrências",
        "",
        "Navegação:",
        "   B - Sair do Programa"
    ])

while True:
    menu_principal()
    opcao = input("Digite a opção desejada: ")

    match opcao:
        case "1":
            cadastrar_ocorrencia()
            input("\nPressione Enter para continuar...")

        case "2":
            "Modulo de pesquisar registros"
            buscar_ocorrencias()
            input("\nPressione Enter para continuar...")

        case "3":
            analisar_dados()
            input("\nPressione Enter para continuar...")

        case "B":
            print("Saindo do programa...")
            break

        case _:
            print("Modulo não implementado. Por favor, escolha uma opção válida.\n")
            input("\nPressione Enter para continuar...")