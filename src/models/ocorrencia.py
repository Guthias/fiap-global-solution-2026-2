from dataclasses import dataclass
from datetime import date
from enum import Enum

class Categoria(Enum):
    CONSERVACAO = "Conservação"
    ILUMINACAO = "Iluminação"
    LIMPEZA = "Limpeza"
    ACESSIBILIDADE = "Acessibilidade"

class Gravidade(Enum):
    BAIXA = "Baixa"
    MEDIA = "Média"
    ALTA = "Alta"
    CRITICA = "Crítica"

class Status(Enum):
    ABERTA = "Aberta"
    EM_ANALISE = "Em análise"
    CONCLUIDA = "Concluída"

@dataclass
class Ocorrencia:
    id: str
    descricao: str
    local: str
    data: date
    categoria: Categoria | None = None
    gravidade: Gravidade | None = None
    status: Status = Status.ABERTA
