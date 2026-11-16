from repository.CsvRepository import CsvRepository
from utils.exibir_card import exibir_card
from utils.input_numero import input_numero
from utils.registros.cadastrar import cadastrar_ocorrencia
from utils.registros.mostrar import listar_ocorrencias
from utils.registros.analisar_dados import analisar_dados
from utils.registros.atualizar import atualizar_ocorrencia

def menu_principal():
    exibir_card("Seja Bem-vindo!", "Escolha uma opção:", [
        "1. Adicionar novo Registro",
        "2. Pesquisar Registros",
        "3. Atualizar Registro",
        "4. Analise de Dados",
        "5. Mostrar ocorrencias",
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
            input("Pressione Enter para continuar...")

        case 2:
            "Modulo de pesquisar registros"
        case 3:
            atualizar_ocorrencia()
            input("Pressione Enter para continuar...")
        case 4:
            analisar_dados()
            input("Pressione Enter para continuar...")
        case 5:
            listar_ocorrencias()
            input("Pressione Enter para continuar...")
        case 404:
            csv_repo = CsvRepository()
            ocorrencias = csv_repo.listar_todos()
            print(f"Total de ocorrencias: {len(ocorrencias)}")
            input("Pressione Enter para continuar...")
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("Modulo não implementado. Por favor, escolha uma opção válida.\n")
            input("Pressione Enter para continuar...")