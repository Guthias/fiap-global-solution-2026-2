# Neighborhood Action Dashboard

## 1. Apresentação do projeto

O **Neighborhood Action Dashboard** é um sistema desenvolvido em Python como parte da **Global Solution da FIAP**. Seu objetivo é facilitar o registro, a organização, a consulta e o acompanhamento de ocorrências relacionadas a problemas urbanos.

A solução permite centralizar registros provenientes de diferentes localidades, sem limitar sua utilização a um único bairro. Cada ocorrência possui informações próprias, incluindo descrição, localização, categoria, gravidade e situação atual.

Com os dados organizados, o sistema busca facilitar a identificação de problemas recorrentes e fornecer informações que auxiliem na análise das demandas e na definição de prioridades.

---

## 2. Problema identificado e proposta de solução

Problemas relacionados à infraestrutura urbana podem comprometer a segurança, a mobilidade e a qualidade de vida da população. Entre eles estão falhas na iluminação pública, dificuldades de acessibilidade, problemas de limpeza e falta de conservação de espaços públicos.

Quando essas informações ficam dispersas ou não são organizadas adequadamente, torna-se mais difícil identificar quais problemas aparecem com maior frequência e acompanhar sua situação.

A proposta do projeto é oferecer um sistema que reúna essas ocorrências em uma estrutura organizada, permitindo seu registro, classificação, consulta e atualização.

### Público beneficiado

- **Cidadãos:** podem registrar problemas identificados em suas localidades.
- **Responsáveis pelo acompanhamento:** podem consultar e organizar as ocorrências registradas.
- **Gestores e equipes de análise:** podem utilizar os dados organizados para identificar demandas recorrentes e compreender melhor os problemas apresentados.

---

## 3. Categorias e classificação das ocorrências

Para padronizar os registros, o sistema trabalha com quatro categorias principais:

| Categoria | Descrição |
| --- | --- |
| Iluminação | Problemas relacionados à iluminação pública. |
| Acessibilidade | Barreiras e dificuldades de acesso e mobilidade. |
| Limpeza | Problemas relacionados à limpeza e ao descarte de resíduos. |
| Conservação | Problemas de manutenção e conservação de espaços públicos. |

As ocorrências também são classificadas por nível de gravidade:

- Baixa;
- Média;
- Alta;
- Crítica.

Para acompanhar a situação de cada registro, são utilizados três status:

- Aberta;
- Em análise;
- Concluída.

Essa padronização permite organizar as informações e facilitar as consultas e análises realizadas pelo sistema.

---

## 4. Funcionamento do sistema

O funcionamento está organizado em etapas:

1. **Cadastro:** registro de uma nova ocorrência com descrição e localização.
2. **Classificação:** identificação da categoria e da gravidade do problema.
3. **Armazenamento:** persistência das informações nos arquivos de dados do projeto.
4. **Consulta:** busca e visualização dos registros disponíveis.
5. **Acompanhamento:** atualização do status e da gravidade de uma ocorrência.
6. **Análise:** organização dos dados para identificar quantidades, categorias e situações das demandas.

Entre as funcionalidades identificadas nos módulos compartilhados estão o cadastro, a classificação, a busca de ocorrências, a exibição paginada, a visualização de detalhes, a edição de informações e a análise dos dados.

---

## 5. Tecnologias e armazenamento

O projeto utiliza **Python** para desenvolver as funcionalidades e organizar as operações do sistema.

Os dados são armazenados em arquivos locais, com destaque para:

- `dados.csv`: arquivo utilizado pelo repositório CSV para armazenar e consultar registros.
- `ocorrencias.json`: arquivo também presente na estrutura de dados do projeto.

O repositório responsável pelo CSV centraliza operações de leitura, cadastro e atualização das ocorrências. Essa organização permite separar as operações de armazenamento das demais funcionalidades do sistema.

### Campos dos registros

Os campos identificados na estrutura CSV são:

| Campo | Finalidade |
| --- | --- |
| `id` | Identificar individualmente cada ocorrência. |
| `categoria` | Armazenar a classificação do problema. |
| `descricao` | Apresentar os detalhes da ocorrência. |
| `local` | Informar onde o problema foi identificado. |
| `data` | Registrar a data da ocorrência. |
| `gravidade` | Indicar o nível de gravidade. |
| `status` | Representar a situação atual do registro. |

---

## 6. Organização e estrutura do projeto

O projeto está dividido em três pastas principais e dois arquivos externos. Dentro de `src`, as responsabilidades estão separadas em quatro subpastas e um arquivo principal.

```text
fiap-global-solution-2026-2/
│
├── data/
│   ├── dados.csv
│   └── ocorrencias.json
│
├── docs/
│   ├── link_video.txt
│   ├── relatorio.pdf
│   └── uso_ia.md
│
├── src/
│   │
│   ├── models/
│   │   └── ocorrencia.py
│   │
│   ├── repository/
│   │   └── CSVRepository.py
│   │
│   ├── services/
│   │   ├── buscar_ocorrencias.py
│   │   ├── cadastrar.py
│   │   ├── classificacao.py
│   │   ├── editar_ocorrencia.py
│   │   ├── exibir_ocorrencias_paginadas.py
│   │   └── visualizar_ocorrencia.py
│   │
│   ├── utils/
│   │   ├── registros/
│   │   │   ├── analisar_dados.py
│   │   │   ├── arquivos.py
│   │   │   ├── atualizar.py
│   │   │   ├── importar.py
│   │   │   └── mostrar.py
│   │   │
│   │   ├── converter_enum.py
│   │   ├── exibir_card.py
│   │   └── input_numero.py
│   │
│   └── sistema.py
│
├── .gitignore
└── README.md
```

### Responsabilidade das pastas e módulos

#### `data/`

Armazena os arquivos utilizados para guardar os dados do projeto. Contém a base CSV e o arquivo JSON.

#### `docs/`

Reúne os materiais de documentação e entrega acadêmica: link do vídeo, relatório em PDF e documentação sobre o uso de inteligência artificial.

#### `src/models/`

Contém o arquivo `ocorrencia.py`, responsável pela representação dos dados de uma ocorrência. O modelo organiza atributos como identificador, descrição, localização, data, categoria, gravidade e status.

#### `src/repository/`

Contém `CSVRepository.py`, responsável pelas operações de acesso aos registros armazenados no CSV, incluindo leitura, cadastro e atualização.

#### `src/services/`

Reúne os módulos responsáveis pelas funcionalidades do sistema:

| Arquivo | Responsabilidade identificada |
| --- | --- |
| `buscar_ocorrencias.py` | Busca e consulta de ocorrências. |
| `cadastrar.py` | Cadastro de novos registros. |
| `classificacao.py` | Classificação das ocorrências. |
| `editar_ocorrencia.py` | Edição de informações, incluindo status e gravidade. |
| `exibir_ocorrencias_paginadas.py` | Exibição dos registros de forma paginada. |
| `visualizar_ocorrencia.py` | Visualização dos detalhes de uma ocorrência. |

#### `src/utils/`

Reúne funções auxiliares utilizadas pelo sistema:

| Arquivo | Responsabilidade identificada |
| --- | --- |
| `converter_enum.py` | Apoio à conversão e utilização de enumerações. |
| `exibir_card.py` | Organização e apresentação de informações em formato de card. |
| `input_numero.py` | Apoio à entrada e validação de valores numéricos. |

#### `src/utils/registros/`

Contém módulos auxiliares relacionados ao tratamento e à apresentação dos registros:

| Arquivo | Responsabilidade a confirmar |
| --- | --- |
| `analisar_dados.py` | Análise e organização dos dados das ocorrências. |
| `arquivos.py` | Operações auxiliares relacionadas aos arquivos. |
| `atualizar.py` | Rotinas auxiliares de atualização. |
| `importar.py` | Rotinas de importação de dados. |
| `mostrar.py` | Apresentação de informações dos registros. |

#### `src/sistema.py`

Arquivo localizado diretamente na pasta `src`, fora das quatro subpastas. É o arquivo indicado para a execução e integração do sistema, devendo ser confirmado como ponto de entrada da aplicação.

---

## 7. Estruturas de dados e lógica de programação

O projeto utiliza recursos de Python para organizar as informações e implementar as funcionalidades.

Entre os elementos identificados estão:

- **Enum:** utilizado para padronizar categorias, gravidades e status.
- **Dataclass:** utilizada no modelo `Ocorrencia` para organizar os atributos de cada registro.
- **CSV:** utilizado para persistência e consulta dos dados.
- **Funções e módulos:** organizam as operações de cadastro, classificação, consulta, edição e análise.
- **Estruturas auxiliares:** utilizadas no processamento e na apresentação das informações.

A separação entre modelo, repositório, serviços e utilitários contribui para a modularização do código, facilitando a manutenção e a evolução do sistema.

> ⚠️ **Pendente de validação pela equipe:** apresentar exemplos concretos de utilização das estruturas obrigatórias da atividade, incluindo listas, filas, pilhas, dicionários, hierarquia de dados e matriz ou lista de listas. Também devem ser identificadas as condições lógicas com AND, OR e NOT utilizadas na implementação.

---

## 8. Regras de negócio e validações

As regras do sistema buscam manter os registros organizados e padronizados.

Entre as regras identificadas estão:

- Cada ocorrência deve possuir um identificador para permitir sua localização.
- As categorias devem seguir as opções padronizadas pelo sistema.
- A gravidade deve representar o nível do problema registrado.
- O status deve indicar a situação atual da ocorrência.
- As alterações realizadas devem ser persistidas no arquivo de dados.
- As consultas devem permitir localizar e visualizar os registros disponíveis.

O sistema também possui módulos auxiliares para entrada numérica, classificação e manipulação dos dados.

> ⚠️ **Pendente de complementação:** documentar as validações efetivamente implementadas para campos obrigatórios, entradas inválidas e informações ausentes ou inconsistentes. A equipe também deve apresentar exemplos reais de expressões booleanas e condições utilizadas no código.

---

## 9. Indicadores e análise dos dados

O módulo `analisar_dados.py` está relacionado à análise das ocorrências armazenadas e à organização de indicadores.

Entre os indicadores identificados no desenvolvimento estão:

| Indicador | Forma de cálculo |
| --- | --- |
| Total de ocorrências | Quantidade total de registros. |
| Ocorrências por categoria | Contagem de registros em cada categoria. |
| Ocorrências por gravidade | Contagem por nível de gravidade. |
| Ocorrências por status | Contagem por situação atual. |
| Taxa de conclusão | (Concluídas ÷ Total) × 100. |
| Demandas pendentes | Abertas + Em análise. |

Essas informações permitem observar a distribuição das ocorrências, identificar categorias com maior concentração de registros e acompanhar a quantidade de demandas ainda não concluídas.

> ⚠️ **Pendente de complementação:** inserir os resultados reais produzidos pela versão final do sistema, demonstrar as fórmulas utilizadas no código e acrescentar a interpretação dos indicadores. Caso existam outros indicadores implementados, eles também devem ser documentados.

---

## 10. Como executar o projeto

Para executar o sistema, é necessário ter o Python instalado e acessar a pasta principal do repositório pelo terminal.

Comando previsto:

```bash
python src/sistema.py
```

Em ambientes nos quais o comando `python` não esteja configurado, pode ser necessário utilizar:

```bash
python3 src/sistema.py
```

> ⚠️ **Pendente de validação:** confirmar a execução na versão final e documentar eventuais dependências necessárias.

---

## 11. Exemplos de utilização

Os exemplos abaixo representam situações de uso compatíveis com a proposta do sistema. Os dados são fictícios e devem ser ajustados conforme as opções e as mensagens reais da aplicação.

### Cadastro de ocorrência

- **Categoria:** Iluminação
- **Descrição:** Poste com iluminação apagada
- **Local:** Rua das Flores, 120
- **Gravidade:** Alta
- **Status:** Aberta

### Consulta

O usuário pode consultar ocorrências cadastradas e visualizar os registros de acordo com os critérios disponíveis no sistema.

### Atualização

Uma ocorrência registrada como **Aberta** pode ter seu status alterado para **Em análise**, permitindo acompanhar a evolução da demanda.

### Análise

O módulo de análise organiza os registros e permite consultar quantidades por categoria, gravidade e status.

> ⚠️ **Pendente de complementação:** adicionar exemplos reais da execução no terminal, incluindo cadastro, consulta, atualização e apresentação dos indicadores.

---

## 12. Acessibilidade, inclusão e privacidade

O projeto aborda problemas urbanos que podem afetar diferentes grupos da população, especialmente em questões relacionadas à acessibilidade, mobilidade e conservação dos espaços públicos.

A organização das ocorrências permite reunir informações sobre problemas que impactam o cotidiano dos cidadãos.

Em relação à privacidade, recomenda-se utilizar apenas as informações necessárias para identificar e acompanhar cada ocorrência, evitando a exposição de dados pessoais desnecessários.

---

## 13. Conclusão e limitações

O Neighborhood Action Dashboard apresenta uma proposta de organização e acompanhamento de ocorrências urbanas por meio de uma aplicação desenvolvida em Python.

A solução reúne funcionalidades de cadastro, classificação, consulta, edição e análise de dados, utilizando uma estrutura modular e arquivos locais para armazenamento.

O desenvolvimento permite aplicar conceitos de programação, organização de dados, modularização, manipulação de arquivos e lógica computacional.

Como limitações, o funcionamento depende da qualidade das informações cadastradas e da atualização adequada dos registros. O projeto também possui escopo acadêmico e não representa uma integração direta com órgãos públicos ou plataformas oficiais de atendimento.

> ⚠️ **Pendente de complementação:** incluir os principais aprendizados da equipe, dificuldades encontradas durante o desenvolvimento e possíveis melhorias futuras.

---

## 14. Equipe

**Nome da equipe:** [PREENCHER]

| Integrante | RM |
| --- | --- |
| Gustavo Mathias | [RM: 575347] |
| Clara Mei | [RM: 575975] |
| Vinicius Ramos | [RM: 575185] |
| Daniel Turatti | [RM: 574215] |
| Evellyn Soares | [RM: 576111] |

---

## 15. Links e materiais

- **Repositório GitHub:** <https://github.com/Guthias/fiap-global-solution-2026-2>
- **Vídeo de apresentação:** [INSERIR LINK DO YOUTUBE]

---

### Observação para a equipe

Este README foi elaborado para documentar a proposta, a organização dos arquivos e as funcionalidades identificadas durante o desenvolvimento do projeto.

Os itens sinalizados como pendentes precisam ser revisados e complementados, considerando a implementação real e os requisitos da Global Solution. Antes da entrega, é importante conferir os exemplos, os indicadores, as estruturas de dados e os resultados apresentados para garantir que a documentação corresponda à versão final do sistema.
