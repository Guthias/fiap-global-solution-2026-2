from utils.exibir_card import exibir_card
from services.visualizar_ocorrencia import visualizar_ocorrencia

def exibir_ocorrencias_paginadas(ocorrencias, mensagem,  titulo="Resultado da Pesquisa"):
    if not ocorrencias:
        exibir_card(titulo, "", [])
        return

    total_paginas = (len(ocorrencias) + 4) // 5
    pagina = 0

    while True:
        ocorrencias_da_pagina = ocorrencias[pagina * 5:(pagina + 1) * 5]
        texto_ocorrencias = [mensagem, ""]

        for index, ocorrencia in enumerate(ocorrencias_da_pagina):
            texto_ocorrencias.append(f"{index+1}. Descrição: {ocorrencia.descricao}")
            texto_ocorrencias.append(f"    Local: {ocorrencia.local}")
            texto_ocorrencias.append(f"    Status: {ocorrencia.status.value}")
            texto_ocorrencias.append("")

        texto_ocorrencias.append("Navegação:")
        if total_paginas > 1:
            if pagina < total_paginas - 1:
                texto_ocorrencias.append("N - Próxima página")
            if pagina > 0:
                texto_ocorrencias.append("P - Página anterior")
        
        texto_ocorrencias.append("B - Voltar ao Menu de Pesquisa")

        exibir_card(titulo, 
                    f"Exibindo {len(ocorrencias_da_pagina)} de {len(ocorrencias)} (Página {pagina + 1}/{total_paginas})",
                    texto_ocorrencias)

        opcao = input("Digite a opção desejada: ")

        match opcao.upper():
            case "1" | "2" | "3" | "4" | "5":
                index = int(opcao) - 1
                if index < len(ocorrencias_da_pagina):
                    visualizar_ocorrencia(ocorrencias_da_pagina[index])

            case "N":
                if pagina < total_paginas - 1:
                    pagina += 1

            case "P":
                if pagina > 0:
                    pagina -= 1

            case "B":
                break

            case _:
                pass
