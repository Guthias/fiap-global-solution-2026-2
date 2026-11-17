from repository.CsvRepository import CsvRepository
from services.buscar_ocorrencias import buscar_ocorrencias
from utils.exibir_card import exibir_card
from utils.input_numero import input_numero
from services.cadastrar import cadastrar_ocorrencia
from utils.registros.mostrar import listar_ocorrencias
from utils.registros.analisar_dados import analisar_dados
from utils.registros.atualizar import atualizar_ocorrencia

def menu_principal():
    exibir_card("Seja Bem-vindo!", "Escolha uma opção:", [
        "1. Cadastrar nova Ocorrência",
        "2. Pesquisar Ocorrências",
        "3. Atualizar Ocorrência",
        "4. Análise de Dados",
        "5. Mostrar Ocorrências",
        "",
        "404. Testes (REMOVER NA VERSÃO FINAL)",
        "",
        "0. Sair"
    ])


while True:
    menu_principal()
    opcao = input_numero("Digite a opção desejada: ")
    match opcao:
        case 1:
            cadastrar_ocorrencia()
            input("\nPressione Enter para continuar...")

        case 2:
            "Modulo de pesquisar registros"
            buscar_ocorrencias()
            input("\nPressione Enter para continuar...")
            
        case 3:
            atualizar_ocorrencia()
            input("\nPressione Enter para continuar...")

        case 4:
            analisar_dados()
            input("\nPressione Enter para continuar...")

        case 5:
            listar_ocorrencias()
            input("\nPressione Enter para continuar...")

        case 404:
            csv_repo = CsvRepository()
            ocorrencias = csv_repo.listar_todos()
            print(f"Total de ocorrencias: {len(ocorrencias)}")
            input("\nPressione Enter para continuar...")

        case 0:
            print("Saindo do programa...")
            break

        case _:
            print("Modulo não implementado. Por favor, escolha uma opção válida.\n")
            input("\nPressione Enter para continuar...")