from services.buscar_ocorrencias import buscar_ocorrencias
from utils.exibir_card import exibir_card
from services.cadastrar import cadastrar_ocorrencia
from services.analisar_dados import analisar_dados
from services.historico import exibir_historico
from services.importar import importar_e_validar

def menu_principal():
    exibir_card("Seja Bem-vindo!", "Escolha uma opção:", [
        "1. Cadastrar nova Ocorrência",
        "2. Pesquisar Ocorrências",
        "3. Analisar Ocorrências",
        "4. Histórico de mudanças",
        "5. Importar e validar registros",
        "",
        "Navegação:",
        "   B - Sair do Programa"
    ])

while True:
    menu_principal()
    opcao = input("Digite a opção desejada: ")

    match opcao.upper():
        case "1":
            cadastrar_ocorrencia()
            input("\nPressione Enter para continuar...")

        case "2":
            "Modulo de pesquisar registros"
            buscar_ocorrencias()

        case "3":
            analisar_dados()
            input("\nPressione Enter para continuar...")

        case "4":
            exibir_historico()
            input("\nPressione Enter para continuar...")

        case "5":
            importar_e_validar()
            input("\nPressione Enter para continuar...")

        case "B":
            print("Saindo do programa...")
            break