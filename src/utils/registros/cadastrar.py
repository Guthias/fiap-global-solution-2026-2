from utils.registros.arquivos import carregar_dados, salvar_dados
from datetime import datetime
from utils.registros.atualizar import registrar_evento

def verificar_data():
    while True:
        data = input("Digite a data (DD/MM/AAAA): ")

        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data

        except ValueError:
            print("Data inválida! Tente novamente.")

def identificar_gravidade(descricao):

    descricao = descricao.lower()

    palavras_altas = [
        "risco", "acidente", "perigo",
        "fio caido", "bueiro aberto"
    ]

    palavras_medias = [
        "buraco", "lampada queimada",
        "calcada quebrada"
    ]

    for palavra in palavras_altas:
        if palavra in descricao:
            return "Alta"

    for palavra in palavras_medias:
        if palavra in descricao:
            return "Media"

    return "Baixa"

def solicitar_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Este campo não pode ficar vazio!")

def selecionar_categoria():
    while True:
        print("\n--- CATEGORIAS ---")
        print("1 - Iluminação")
        print("2 - Acessibilidade")
        print("3 - Limpeza")
        print("4 - Conservação")

        opcao = input("Selecione a categoria: ")

        match opcao:
            case "1":
                return "Iluminacao"
            case "2":
                return "Acessibilidade"
            case "3":
                return "Limpeza"
            case "4":
                return "Conservacao"
            case _:
                print("Opção inválida! Escolha de 1 a 4.")

def cadastrar_ocorrencia():
    dados = carregar_dados()

    categoria = selecionar_categoria()
    descricao = solicitar_texto("Digite o que aconteceu: ")
    local = solicitar_texto("Digite o local: ")

    gravidade = identificar_gravidade(descricao)
    data = verificar_data()

    dados["ultimo_id"] += 1
    novo_id = str(dados["ultimo_id"]).zfill(3)

    nova_ocorrencia = {
        "id": novo_id,
        "categoria": categoria,
        "descricao": descricao,
        "local": local,
        "data": data,
        "gravidade": gravidade,
        "status": "aberta"
    }

    dados["ocorrencias"].append(nova_ocorrencia)
    registrar_evento(dados, novo_id, "", "aberta")

    salvar_dados(dados)

    print("\nOcorrência cadastrada com sucesso!")
    print(f"Gravidade identificada: {gravidade}")

