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
    def __init__(self):
        self.arquivo = Path(__file__).resolve().parents[2] / "data" / "dados.csv"
        self.arquivo.parent.mkdir(parents=True, exist_ok=True)

        if not self.arquivo.exists():
            self._criar_arquivo()

    def _criar_arquivo(self):
        campos = [
            "id",
            "categoria",
            "descricao",
            "local",
            "data",
            "gravidade",
            "status"
        ]

        with self.arquivo.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()

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
