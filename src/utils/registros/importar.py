import csv
import json
from pathlib import Path

CAMINHO_CSV = Path(__file__).resolve().parents[3] / "data" / "dados.csv"
CAMINHO_JSON = Path(__file__).resolve().parents[3] / "data" / "ocorrencias.json"


def importar_csv_para_json():
    with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    ids_existentes = {
        ocorrencia["id"] for ocorrencia in dados["ocorrencias"]
    }

    with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            if linha["id"] not in ids_existentes:
                nova_ocorrencia = {
                    "id": linha["id"],
                    "categoria": linha["categoria"],
                    "descricao": linha["descricao"],
                    "local": linha["local"],
                    "data": linha["data"],
                    "gravidade": linha["gravidade"],
                    "status": linha["status"]
                }

                dados["ocorrencias"].append(nova_ocorrencia)
                ids_existentes.add(linha["id"])

   
    dados["ultimo_id"] = max(
        int(ocorrencia["id"])
        for ocorrencia in dados["ocorrencias"]
    )

    
    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print("Importação concluída!")


if __name__ == "__main__":
    importar_csv_para_json()
