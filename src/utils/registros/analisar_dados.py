
from utils.registros.arquivos import carregar_dados


def analisar_dados():
    dados = carregar_dados()
    ocorrencias = dados["ocorrencias"]

    total = len(ocorrencias)

    if total == 0:
        print("Nenhuma ocorrência cadastrada.")
        return

    print(f"\nTotal de ocorrências: {total}")

    # Ocorrências por categoria
    categorias = {
        "Iluminacao": 0,
        "Acessibilidade": 0,
        "Limpeza": 0,
        "Conservacao": 0
    }

    for ocorrencia in ocorrencias:
        categoria = ocorrencia.get("categoria", "").capitalize()

        if categoria in categorias:
            categorias[categoria] += 1

    print("\n--- OCORRÊNCIAS POR CATEGORIA ---")

    for categoria, quantidade in categorias.items():
        percentual = (quantidade / total) * 100
        print(f"{categoria}: {quantidade} ({percentual:.1f}%)")

    # Ocorrências por gravidade
    gravidades = {
        "Alta": 0,
        "Media": 0,
        "Baixa": 0
    }

    for ocorrencia in ocorrencias:
        gravidade = ocorrencia["gravidade"].capitalize()

        if gravidade in gravidades:
            gravidades[gravidade] += 1

    print("\n--- OCORRÊNCIAS POR GRAVIDADE ---")

    for gravidade, quantidade in gravidades.items():
        print(f"{gravidade}: {quantidade}")

    # Ocorrências por status
    status = {
        "aberta": 0,
        "em analise": 0,
        "concluida": 0
    }

    for ocorrencia in ocorrencias:
        situacao = ocorrencia["status"].lower()

        if situacao in status:
            status[situacao] += 1

    print("\n--- OCORRÊNCIAS POR STATUS ---")

    for situacao, quantidade in status.items():
        percentual = (quantidade / total) * 100
        print(f"{situacao.capitalize()}: {quantidade} ({percentual:.1f}%)")

    # Indicador de conclusão
    percentual = (status["concluida"] / total) * 100

    print(f"\nTaxa de conclusão: {percentual:.1f}%")

    # Interpretação
    pendentes = status["aberta"] + status["em analise"]

    print("\n--- INTERPRETAÇÃO DOS DADOS ---")
    print(f"Existem {pendentes} ocorrências pendentes de conclusão.")

    categoria_principal = max(categorias, key=categorias.get)

    print(
        f"A categoria com mais registros é: "
        f"{categoria_principal} ({categorias[categoria_principal]} ocorrências)."
    )
