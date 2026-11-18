from repository.CsvRepository import CsvRepository
from utils.exibir_card import exibir_card


def exibir_historico():
    # Pilha (LIFO): o evento mais recente fica no topo, por isso lemos do fim para o inicio
    eventos = CsvRepository().listar_historico()
    linhas = [f"Total de eventos: {len(eventos)}", "", "Mais recentes primeiro (até 12):"]

    i = len(eventos) - 1
    mostrados = 0
    while i >= 0 and mostrados < 12:
        evento = eventos[i]
        if evento["de"] == "":
            mudanca = f"abertura ({evento['para']})"
        else:
            mudanca = f"{evento['de']} -> {evento['para']}"
        linhas.append(f"{evento['data']} | {evento['id'][:8]} | {mudanca}")
        i = i - 1
        mostrados = mostrados + 1

    exibir_card("HISTÓRICO", "Mudanças de situação das ocorrências", linhas)