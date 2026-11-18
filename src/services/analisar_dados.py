from repository.CsvRepository import CsvRepository
from utils.exibir_card import exibir_card

def analisar_dados():
    csv_repo = CsvRepository()
    ocorrencias = csv_repo.listar_todos()

    total = len(ocorrencias)

    if not total:
        exibir_card(
            "ANÁLISE DE DADOS",
            "RESUMO",
            ["Nenhuma ocorrência cadastrada."]
        )
        return

    # Ocorrências por categoria
    categorias = {
        "Iluminação": 0,
        "Acessibilidade": 0,
        "Limpeza": 0,
        "Conservação": 0,
    }

    total_categorizadas = 0

    for ocorrencia in ocorrencias:
        if ocorrencia.categoria is not None:
            categoria = ocorrencia.categoria.value
            if categoria in categorias:
                categorias[categoria] += 1
                total_categorizadas += 1

    conteudo_categorias = []

    for categoria, quantidade in categorias.items():
        percentual = quantidade / total_categorizadas * 100 if total_categorizadas else 0
        conteudo_categorias.append(
            f"{categoria}: {quantidade} ({percentual:.1f}%)"
        )

    # Ocorrências por gravidade
    gravidades = {
        "Alta": 0,
        "Média": 0,
        "Baixa": 0,
        "Crítica": 0
    }

    for ocorrencia in ocorrencias:
        if ocorrencia.gravidade is not None:
            gravidade = ocorrencia.gravidade.value
            if gravidade in gravidades:
                gravidades[gravidade] += 1

    conteudo_gravidades = []

    for gravidade, quantidade in gravidades.items():
        conteudo_gravidades.append(
            f"{gravidade}: {quantidade}"
        )

    # Ocorrências por status
    status = {
        "Aberta": 0,
        "Em análise": 0,
        "Concluída": 0
    }

    for ocorrencia in ocorrencias:
        situacao = ocorrencia.status.value
        if situacao in status:
            status[situacao] += 1

    conteudo_status = []

    for situacao, quantidade in status.items():
        percentual = quantidade / total * 100
        conteudo_status.append(
            f"{situacao}: {quantidade} ({percentual:.1f}%)"
        )

    # Indicadores
    percentual = status["Concluída"] / total * 100
    pendentes = status["Aberta"] + status["Em análise"]

    conteudo_resumo = [
        f"Total de ocorrências: {total}",
        f"Taxa de conclusão: {percentual:.1f}%",
        f"Ocorrências pendentes: {pendentes}"
    ]

    if total_categorizadas:
        categoria_principal = max(categorias, key=categorias.get)
        conteudo_resumo.append(
            f"Categoria principal: {categoria_principal}"
        )

    # Exibição dos cards
    conteudo_analise = (
    conteudo_resumo
    + [""]
    + ["--- OCORRÊNCIAS POR CATEGORIA ---"]
    + conteudo_categorias
    + [""]
    + ["--- OCORRÊNCIAS POR GRAVIDADE ---"]
    + conteudo_gravidades
    + [""]
    + ["--- OCORRÊNCIAS POR STATUS ---"]
    + conteudo_status
)
    
    exibir_card(
    "ANÁLISE DE DADOS",
    "RESUMO GERAL DAS OCORRÊNCIAS",
    conteudo_analise
    ),