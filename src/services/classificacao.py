import json

from models.ocorrencia import Categoria
from models.ocorrencia import Gravidade
from utils.google_genai import gerar_resposta_json

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

def analise_assistida_por_ia(descricao):
    prompt = f"""
        Você é um assistente que classifica ocorrências urbanas.
        Analise a descrição abaixo e retorne somente um JSON válido, sem Markdown,
        com as chaves "gravidade" e "categoria".

        Para "gravidade", use exatamente um destes valores:
        BAIXA, MEDIA, ALTA, CRITICA.

        Para "categoria", use exatamente um destes valores:
        CONSERVACAO, ILUMINACAO, LIMPEZA, ACESSIBILIDADE.
        Se não for possível identificar uma categoria, use null.

        Descrição: {descricao}
    """

    resultado = json.loads(gerar_resposta_json(prompt))

    gravidade = Gravidade[resultado["gravidade"]]
    categoria_nome = resultado["categoria"]
    categoria = Categoria[categoria_nome] if categoria_nome is not None else None

    return {"gravidade": gravidade, "categoria": categoria}


def classificar_ocorrencia(ocorrencia):
    try:

        print("\nIniciando Analise Assistida por IA")
        classificacao = analise_assistida_por_ia(ocorrencia.descricao)
        print("Analise concluida com Sucesso!!")
        ocorrencia.gravidade = classificacao["gravidade"]
        ocorrencia.categoria = classificacao["categoria"]

    except Exception:
        print("\nErro na chamada a API, usando o Fallback deterministico")
        ocorrencia.gravidade = identificar_gravidade(ocorrencia.descricao)
        ocorrencia.categoria = identificar_categoria(ocorrencia.descricao)