# Uso de Inteligência Artificial

Este documento declara onde a IA foi usada no projeto **Neighborhood Action Dashboard**, tanto
**dentro do sistema** quanto **no desenvolvimento**, e o que foi feito para conferir os resultados.

## 1. IA dentro do sistema (funcionalidade)

| Item | Descrição |
|---|---|
| Onde | `src/services/classificacao.py` (função `analise_assistida_por_ia`) e `src/utils/google_genai.py` |
| O que faz | Ao cadastrar uma ocorrência, envia a descrição para o modelo Gemini (biblioteca `google-genai`) para sugerir **categoria** e **gravidade** |
| Plano B | Se a IA não estiver disponível (sem biblioteca, sem chave `GOOGLE_API_KEY` ou erro de rede), o sistema usa uma **classificação por palavras-chave** (`identificar_categoria` e `identificar_gravidade`) e informa "usando o Fallback deterministico" |
| Dados enviados | Apenas o texto da descrição da ocorrência. Não há dados pessoais no sistema |
| Decisão final | A categoria e a gravidade podem ser **editadas depois pelo usuário** (menu de pesquisa → detalhes da ocorrência) |

**Limitação declarada:** nos testes feitos para esta documentação o programa foi executado **sem chave de API**,
portanto o resultado observado foi sempre o do plano B. A chamada real ao Gemini deve ser testada pela
equipe com uma chave válida (o nome do modelo configurado em `google_genai.py` precisa ser conferido).
O sistema foi ajustado para abrir e funcionar normalmente mesmo sem a biblioteca de IA instalada.

## 2. IA no desenvolvimento

| Ferramenta | Para que foi usada |
|---|---|
| Claude (Anthropic) | Análise do enunciado, apoio na organização do projeto, revisão do código do repositório, sugestão e redação de correções (identificação de bugs, validação de registros, histórico de mudanças, matriz categoria × status e interpretação), geração dos dados fictícios de teste e redação do README, deste documento e do relatório |
| [Equipe: preencher] | [Equipe: informar qualquer outra ferramenta usada por cada integrante, por exemplo para gerar código, tirar dúvidas ou revisar textos] |

### Trechos que tiveram apoio de IA
- `src/services/validacao.py`, `src/services/importar.py`, `src/services/historico.py` e `src/services/matriz.py` (arquivos novos).
- Correções em `models/ocorrencia.py` (id e data gerados por ocorrência), `services/classificacao.py` (importação da IA só quando usada) e `services/visualizar_ocorrencia.py` (categorias do menu de edição).
- Registros fictícios adicionados em `data/dados.csv`, `data/importacao.csv` e `data/historico.csv`.
- Textos de `README.md` e `docs/relatorio.pdf`.

## 3. Como o resultado foi conferido

- O programa foi **executado** em cópia do repositório, com entradas válidas e inválidas.
- Foram verificados: abertura do sistema sem a biblioteca de IA; cadastro de dois registros seguidos (identificadores diferentes);
  atualização de status com registro no histórico; edição de categoria; importação (2 registros aceitos e 5 recusados, cada um com o motivo);
  análise de dados; matriz e interpretação.
- Os números do relatório (14 ocorrências, 28,6% de conclusão, 10 pendentes, 10 eventos de histórico) foram copiados da saída real do programa.
- Os dados são **fictícios** e não representam ocorrências reais.

## 4. Responsabilidade da equipe

A IA foi tratada como apoio. A equipe é responsável por **ler, entender, testar e explicar** todo o código entregue,
e por conferir se o que está documentado corresponde ao que o programa faz.

> **Antes de entregar, a equipe deve revisar este documento** e completar os campos marcados com `[Equipe: ...]`,
> declarando com honestidade quem usou cada ferramenta e para quê.