from dataclasses import dataclass
from datetime import date
from enum import Enum
from uuid import uuid4

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
    descricao: str
    local: str
    
    id: str = str(uuid4())
    data: date = date.today()
    categoria: Categoria | None = None
    gravidade: Gravidade | None = None
    status: Status = Status.ABERTA
