from utils.exibir_card import exibir_card
from utils.input_numero import input_numero

def menu_principal():
    exibir_card("Seja Bem-vindo!", "Escolha uma opção:", [
        "1. Adicionar novo Registro",
        "2. Pesquisar Registros",
        "3. Atualizar Registro",
        "4. Analise de Dados",
        "",
        "0. Sair"
    ])


while True:
    menu_principal()
    opcao = input_numero("Digite a opção desejada: ")
    match opcao:
        case 1:
            "Modulo de adicionar novo registro"
        case 2:
            "Modulo de pesquisar registros"
        case 3:
            "Modulo de atualizar registro"
        case 4:
            "Modulo de analise de dados"
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("Modulo não implementado. Por favor, escolha uma opção válida.\n")
            input("Pressione Enter para continuar...")