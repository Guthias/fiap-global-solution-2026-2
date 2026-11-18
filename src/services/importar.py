import csv
from pathlib import Path
from repository.CsvRepository import CsvRepository
from services.validacao import validar_linha, valor
from utils.exibir_card import exibir_card

PASTA = Path(__file__).resolve().parents[2] / "data"
ARQUIVO_IMPORTACAO = PASTA / "importacao.csv"
ARQUIVO_REJEITADOS = PASTA / "rejeitados.csv"
CAMPOS = ["id", "categoria", "descricao", "local", "data", "gravidade", "status"]


def ler_linhas(arquivo):
    if not arquivo.exists():
        return []
    with arquivo.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def importar_e_validar():
    csv_repo = CsvRepository()
    novas = ler_linhas(ARQUIVO_IMPORTACAO)

    # ids que ja existem (lista) para detectar duplicidade
    ids_existentes = []
    for ocorrencia in csv_repo.listar_todos():
        ids_existentes.append(ocorrencia.id)

    aceitos = 0
    recusados = []
    for linha in novas:
        erros = validar_linha(linha, ids_existentes)
        if len(erros) == 0:
            csv_repo.adicionar_linha(linha)
            csv_repo.registrar_evento(valor(linha, "id"), "", valor(linha, "status"))
            ids_existentes.append(valor(linha, "id"))
            aceitos += 1
        else:
            motivo = ""
            for erro in erros:
                if motivo != "":
                    motivo = motivo + "; "
                motivo = motivo + erro
            recusados.append({"id": valor(linha, "id"), "descricao": valor(linha, "descricao"),
                              "motivo": motivo})

    if len(novas) > 0:
        # registra os recusados (acumula) e esvazia a fila de importacao
        antigos = ler_linhas(ARQUIVO_REJEITADOS)
        with ARQUIVO_REJEITADOS.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "descricao", "motivo"])
            writer.writeheader()
            for item in antigos:
                writer.writerow(item)
            for item in recusados:
                writer.writerow(item)
        with ARQUIVO_IMPORTACAO.open("w", newline="", encoding="utf-8") as file:
            csv.DictWriter(file, fieldnames=CAMPOS).writeheader()
        resumo = f"Importação: {aceitos} aceito(s) e {len(recusados)} recusado(s)."
    else:
        resumo = "Não há registros novos para importar."

    conteudo = [resumo, "", "--- REGISTROS RECUSADOS ---"]
    todos_recusados = ler_linhas(ARQUIVO_REJEITADOS)
    if len(todos_recusados) == 0:
        conteudo.append("Nenhum.")
    for item in todos_recusados:
        conteudo.append(f"ID {item['id'][:8] or '(vazio)'}: {item['descricao'][:30]}")
        conteudo.append(f"   {item['motivo'][:44]}")
    exibir_card("IMPORTAR E VALIDAR", "Registros inconsistentes são recusados", conteudo)