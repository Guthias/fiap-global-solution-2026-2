from repository.CsvRepository import CsvRepository
from utils.exibir_card import exibir_card

NOMES_CATEGORIAS = ["Iluminação", "Acessibilidade", "Limpeza", "Conservação"]
NOMES_STATUS = ["Aberta", "Em análise", "Concluída"]


def montar_hierarquia(ocorrencias):
    # Hierarquia (dicionário dentro de dicionário): categoria -> status -> lista de ids
    hierarquia = {}
    for categoria in NOMES_CATEGORIAS:
        hierarquia[categoria] = {}
        for status in NOMES_STATUS:
            hierarquia[categoria][status] = []

    sem_categoria = []
    for ocorrencia in ocorrencias:
        if ocorrencia.categoria is None:
            sem_categoria.append(ocorrencia.id)
        else:
            hierarquia[ocorrencia.categoria.value][ocorrencia.status.value].append(ocorrencia.id)

    return hierarquia, sem_categoria


def montar_matriz(hierarquia):
    # Matriz (lista de listas): linhas = categorias, colunas = status
    matriz = []
    for categoria in NOMES_CATEGORIAS:
        linha = []
        for status in NOMES_STATUS:
            linha.append(len(hierarquia[categoria][status]))
        matriz.append(linha)
    return matriz


def montar_interpretacao(ocorrencias, matriz, sem_categoria):
    total = len(ocorrencias)
    concluidas = 0
    graves_pendentes = 0
    for ocorrencia in ocorrencias:
        if ocorrencia.status.value == "Concluída":
            concluidas += 1
        elif ocorrencia.gravidade is not None and (
            ocorrencia.gravidade.value == "Alta" or ocorrencia.gravidade.value == "Crítica"
        ):
            graves_pendentes += 1

    pendentes = total - concluidas
    frases = []

    if total > 0 and concluidas * 2 < total:
        frases.append(f"Só {concluidas} de {total} foram concluídas.")
        frases.append("Há acúmulo de demandas sem solução.")
    else:
        frases.append(f"{concluidas} de {total} já foram concluídas.")

    # categoria com mais pendências (soma das colunas Aberta + Em análise)
    maior = -1
    lideres = []
    for i in range(len(NOMES_CATEGORIAS)):
        pend_categoria = matriz[i][0] + matriz[i][1]
        if pend_categoria > maior:
            maior = pend_categoria
            lideres = [NOMES_CATEGORIAS[i]]
        elif pend_categoria == maior:
            lideres.append(NOMES_CATEGORIAS[i])
    if maior > 0:
        frases.append(f"Mais pendências: {', '.join(lideres)} ({maior}).")

    if graves_pendentes > 0:
        frases.append(f"{graves_pendentes} pendência(s) de gravidade alta/crítica.")
    if len(sem_categoria) > 0:
        frases.append(f"{len(sem_categoria)} registro(s) sem categoria.")
        frases.append("Revise a classificação deles.")
    if pendentes == 0:
        frases.append("Não há pendências.")
    return frases


def exibir_matriz():
    ocorrencias = CsvRepository().listar_todos()

    if not ocorrencias:
        exibir_card("MATRIZ E HIERARQUIA", "RESUMO", ["Nenhuma ocorrência cadastrada."])
        return

    hierarquia, sem_categoria = montar_hierarquia(ocorrencias)
    matriz = montar_matriz(hierarquia)

    conteudo = ["--- MATRIZ CATEGORIA x STATUS ---",
                "Categoria".ljust(16) + "Aberta  Em análise  Concluída"]
    for i in range(len(NOMES_CATEGORIAS)):
        conteudo.append(
            NOMES_CATEGORIAS[i].ljust(16) + str(matriz[i][0]).ljust(8)
            + str(matriz[i][1]).ljust(12) + str(matriz[i][2])
        )
    if len(sem_categoria) > 0:
        conteudo.append(f"Sem categoria: {len(sem_categoria)}")

    conteudo.append("")
    conteudo.append("--- HIERARQUIA: PENDENTES (CÓDIGOS) ---")
    for categoria in NOMES_CATEGORIAS:
        ids = hierarquia[categoria]["Aberta"] + hierarquia[categoria]["Em análise"]
        if len(ids) == 0:
            conteudo.append(f"{categoria}: nenhuma")
        else:
            curtos = []
            for codigo in ids:
                curtos.append(codigo[:4])
            conteudo.append(f"{categoria}: {' '.join(curtos)}")

    conteudo.append("")
    conteudo.append("--- INTERPRETAÇÃO ---")
    for frase in montar_interpretacao(ocorrencias, matriz, sem_categoria):
        conteudo.append(frase)

    exibir_card("MATRIZ E HIERARQUIA", "Categoria x status e pendências", conteudo)