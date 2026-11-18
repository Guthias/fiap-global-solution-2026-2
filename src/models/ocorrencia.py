from dataclasses import dataclass, field
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

def gerar_id():
    return str(uuid4())

@dataclass
class Ocorrencia:
    descricao: str
    local: str
    
    id: str = field(default_factory=gerar_id)
    data: date = field(default_factory=date.today)
    categoria: Categoria | None = None
    gravidade: Gravidade | None = None
    status: Status = Status.ABERTA

    def atualizar_status(self, repositorio=None):
        anterior = self.status
        if self.status == Status.ABERTA:
            self.status = Status.EM_ANALISE

        elif self.status == Status.EM_ANALISE:
            self.status = Status.CONCLUIDA

        if repositorio:
            repositorio.atualizar_ocorrencia(self)
            if self.status != anterior:
                repositorio.registrar_evento(self.id, anterior.value, self.status.value)

    def atualizar_gravidade(self, nova_gravidade: Gravidade, repositorio=None):
        self.gravidade = nova_gravidade

        if repositorio:
            repositorio.atualizar_ocorrencia(self)

    def atualizar_categoria(self, nova_categoria: Categoria, repositorio=None):
        self.categoria = nova_categoria

        if repositorio:
            repositorio.atualizar_ocorrencia(self)

    def atualizar_descricao(self, nova_descricao: str, repositorio=None):
        self.descricao = nova_descricao

        if repositorio:
            repositorio.atualizar_ocorrencia(self)

    def atualizar_local(self, novo_local: str, repositorio=None):
        self.local = novo_local

        if repositorio:
            repositorio.atualizar_ocorrencia(self)
