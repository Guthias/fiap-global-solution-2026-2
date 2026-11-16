from datetime import datetime
from utils.input_numero import input_numero
from utils.registros.arquivos import carregar_dados, salvar_dados


def transicao_permitida(atual, novo):
    # Fluxo permitido: aberta -> em analise -> concluida
    return (atual == "aberta" and novo == "em analise") or (atual == "em analise" and novo == "concluida")


def buscar_por_id(dados, codigo):
    # Busca linear na lista de ocorrencias
    for ocorrencia in dados["ocorrencias"]:
        if ocorrencia["id"] == codigo:
            return ocorrencia
    return None


def registrar_evento(dados, codigo, de, para):
    # Historico: cada mudanca de situacao vira um evento no fim da lista
    if "historico" not in dados:
        dados["historico"] = []
    dados["historico"].append({
        "id": codigo,
        "de": de,
        "para": para,
        "data": datetime.now().strftime("%d/%m/%Y")
    })


def atualizar_ocorrencia():
    dados = carregar_dados()

    codigo = input("Digite o ID da ocorrência (ex.: 005): ").strip()
    ocorrencia = buscar_por_id(dados, codigo)

    if ocorrencia is None:
        print(f"Nenhuma ocorrência com o ID {codigo}.")
        return

    atual = ocorrencia["status"]
    print(f"\nOcorrência {codigo}: {ocorrencia['descricao']}")
    print(f"Situação atual: {atual}")

    if atual == "concluida":
        print("Esta ocorrência está concluída e não pode ser alterada.")
        print("Se o problema voltou, cadastre uma nova ocorrência.")
        return

    print("\n--- NOVA SITUAÇÃO ---")
    print("1 - Em análise")
    print("2 - Concluída")
    opcao = input_numero("Escolha uma opção: ")

    match opcao:
        case 1:
            novo = "em analise"
        case 2:
            novo = "concluida"
        case _:
            print("Opção inválida!")
            return

    if not transicao_permitida(atual, novo):
        print(f"Mudança não permitida: de '{atual}' para '{novo}'.")
        print("O fluxo é: aberta -> em analise -> concluida.")
        return

    ocorrencia["status"] = novo
    registrar_evento(dados, codigo, atual, novo)
    salvar_dados(dados)

    print(f"\nOcorrência {codigo} atualizada: {atual} -> {novo}.")
    print("Alteração registrada no histórico.")