from models.ocorrencia import Categoria
from models.ocorrencia import Gravidade

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

    if any(palavra in descricao for palavra in palavras_altas):
        return Gravidade.ALTA

    if any(palavra in descricao for palavra in palavras_medias):
        return Gravidade.MEDIA

    return Gravidade.BAIXA

def identificar_categoria(descricao):
    descricao = descricao.lower()

    palavras_conservacao = [
        "buraco", "calcada quebrada",
        "bueiro aberto"
    ]

    palavras_iluminacao = [
        "lampada queimada", "poste apagado"
    ]

    palavras_limpeza = [
        "lixo", "entulho", "sujeira"
    ]

    palavras_acessibilidade = [
        "rampa", "cadeirante", "acesso"
    ]

    if any(palavra in descricao for palavra in palavras_conservacao):
        return Categoria.CONSERVACAO

    if any(palavra in descricao for palavra in palavras_iluminacao):
        return Categoria.ILUMINACAO

    if any(palavra in descricao for palavra in palavras_limpeza):
        return Categoria.LIMPEZA

    if any(palavra in descricao for palavra in palavras_acessibilidade):
        return Categoria.ACESSIBILIDADE

    return None

def classificar_ocorrencia(ocorrencia):
    ocorrencia.gravidade = identificar_gravidade(ocorrencia.descricao)
    ocorrencia.categoria = identificar_categoria(ocorrencia.descricao)