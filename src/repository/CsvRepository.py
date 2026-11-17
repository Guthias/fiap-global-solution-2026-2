import csv
from datetime import date
from pathlib import Path
from utils.converter_enum import converter_enum

from models.ocorrencia import (
    Ocorrencia,
    Categoria,
    Gravidade,
    Status
)

class CsvRepository:
    campos = [
        "id",
        "categoria",
        "descricao",
        "local",
        "data",
        "gravidade",
        "status"
    ]

    def __init__(self):
        self.arquivo = Path(__file__).resolve().parents[2] / "data" / "dados.csv"
        self.arquivo.parent.mkdir(parents=True, exist_ok=True)

        if not self.arquivo.exists():
            self._criar_arquivo()

    def _criar_arquivo(self):

        with self.arquivo.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.campos)
            writer.writeheader()

    def adicionar_ocorrencia(self, ocorrencia: Ocorrencia):
        with self.arquivo.open("a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.campos)
            writer.writerow({
                "id": ocorrencia.id,
                "categoria": ocorrencia.categoria.value if ocorrencia.categoria else "",
                "descricao": ocorrencia.descricao,
                "local": ocorrencia.local,
                "data": ocorrencia.data.isoformat(),
                "gravidade": ocorrencia.gravidade.value if ocorrencia.gravidade else "",
                "status": ocorrencia.status.value
            })

    def atualizar_ocorrencia(self, ocorrencia: Ocorrencia):
        ocorrencias = self.listar_todos()
        for i, o in enumerate(ocorrencias):
            if o.id == ocorrencia.id:
                ocorrencias[i] = ocorrencia
                break

        with self.arquivo.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.campos)
            writer.writeheader()
            for o in ocorrencias:
                writer.writerow({
                    "id": o.id,
                    "categoria": o.categoria.value if o.categoria else "",
                    "descricao": o.descricao,
                    "local": o.local,
                    "data": o.data.isoformat(),
                    "gravidade": o.gravidade.value if o.gravidade else "",
                    "status": o.status.value
                })


    def listar_todos(self) -> list[Ocorrencia]:
        with self.arquivo.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [self._converter_para_objeto(row) for row in reader]

    def _converter_para_objeto(self, row: dict) -> Ocorrencia:
        return Ocorrencia(
            id=row["id"],
            categoria=converter_enum(Categoria, row["categoria"]),
            descricao=row["descricao"],
            local=row["local"],
            data=date.fromisoformat(row["data"]),
            gravidade=converter_enum(Gravidade, row["gravidade"]),
            status=converter_enum(Status, row["status"])
        )
