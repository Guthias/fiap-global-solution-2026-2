from datetime import date
from models.ocorrencia import Categoria, Gravidade, Status


def valores_do_enum(enum_class):
    valores = []
    for item in enum_class:
        valores.append(item.value)
    return valores


def valor(linha, campo):
    # Texto do campo sem espacos; se nao existir, devolve texto vazio
    if campo in linha and linha[campo] is not None:
        return linha[campo].strip()
    return ""


def data_valida(texto):
    # Data real no formato AAAA-MM-DD e que nao esteja no futuro
    try:
        data = date.fromisoformat(texto)
    except ValueError:
        return False
    return data <= date.today()


def validar_linha(linha, ids_existentes):
    # Confere uma linha (tudo texto) e devolve a lista de motivos de recusa.
    # Lista vazia = linha valida.
    erros = []

    # 1) campos obrigatorios (categoria e gravidade podem ficar em branco)
    for campo in ["id", "descricao", "local", "data", "status"]:
        if valor(linha, campo) == "":
            erros.append(f"campo obrigatório ausente: {campo}")

    # 2) valores padronizados (so confere se foram preenchidos)
    if valor(linha, "categoria") != "" and valor(linha, "categoria") not in valores_do_enum(Categoria):
        erros.append(f"categoria desconhecida: '{valor(linha, 'categoria')}'")
    if valor(linha, "gravidade") != "" and valor(linha, "gravidade") not in valores_do_enum(Gravidade):
        erros.append(f"gravidade desconhecida: '{valor(linha, 'gravidade')}'")
    if valor(linha, "status") != "" and valor(linha, "status") not in valores_do_enum(Status):
        erros.append(f"status desconhecido: '{valor(linha, 'status')}'")

    # 3) id sem repeticao
    if valor(linha, "id") != "" and valor(linha, "id") in ids_existentes:
        erros.append(f"id duplicado: {valor(linha, 'id')}")

    # 4) data real e nao futura
    if valor(linha, "data") != "" and not data_valida(valor(linha, "data")):
        erros.append(f"data inválida: '{valor(linha, 'data')}' (use AAAA-MM-DD, real e não futura)")

    # 5) descricao com tamanho minimo e sem e-mail (privacidade)
    if valor(linha, "descricao") != "" and len(valor(linha, "descricao")) < 5:
        erros.append("descrição curta demais (mínimo de 5 caracteres)")
    if "@" in valor(linha, "descricao") or "@" in valor(linha, "local"):
        erros.append("possível dado pessoal (e-mail) na descrição ou no local")

    return erros