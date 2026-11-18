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

Menu principal do sistema:

| Opção | Funcionalidade |
| --- | --- |
| 1 | Cadastrar nova ocorrência (com classificação automática) |
| 2 | Pesquisar ocorrências (todas ou por status, com paginação), ver detalhes e editar status, gravidade, categoria, descrição e local |
| 3 | Analisar ocorrências (indicadores) |
| 4 | Histórico de mudanças de situação |
| 5 | Importar e validar registros (recusa registros inconsistentes) |
| 6 | Matriz categoria × status, hierarquia de pendências e interpretação |
| B | Sair |

O fluxo de situação segue a ordem **Aberta → Em análise → Concluída**. Uma ocorrência concluída não volta atrás.

---

## 5. Tecnologias e armazenamento

O projeto utiliza **Python 3.10 ou superior** (usa `match/case`) para desenvolver as funcionalidades.

Os dados são armazenados em arquivos CSV na pasta `data/`:

| Arquivo | Conteúdo |
| --- | --- |
| `dados.csv` | Ocorrências cadastradas (14 registros válidos iniciais). |
| `historico.csv` | Eventos de mudança de situação (10 eventos iniciais). |
| `importacao.csv` | Registros brutos aguardando validação (7 registros: 2 válidos e 5 inconsistentes). |
| `rejeitados.csv` | Registros recusados pela validação, com o motivo. |

Os dados são **fictícios**. O repositório `CsvRepository` centraliza leitura, cadastro, atualização e registro de eventos.

**Uso de IA (opcional):** a classificação automática pode usar o Gemini (`google-genai`). Sem a biblioteca ou sem chave,
o sistema continua funcionando com a classificação por palavras-chave. Veja `docs/uso_ia.md`.

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

O projeto está dividido em três pastas principais. Dentro de `src`, as responsabilidades estão separadas em quatro subpastas e um arquivo principal.

```text
fiap-global-solution-2026-2/
│
├── data/
│   ├── dados.csv
│   ├── historico.csv
│   ├── importacao.csv
│   └── rejeitados.csv
│
├── docs/
│   ├── link_video.txt
│   ├── relatorio.pdf
│   └── uso_ia.md
│
├── src/
│   ├── models/
│   │   └── ocorrencia.py
│   ├── repository/
│   │   └── CsvRepository.py
│   ├── services/
│   │   ├── analisar_dados.py
│   │   ├── buscar_ocorrencias.py
│   │   ├── cadastrar.py
│   │   ├── classificacao.py
│   │   ├── exibir_ocorrencias_paginadas.py
│   │   ├── historico.py
│   │   ├── importar.py
│   │   ├── matriz.py
│   │   ├── validacao.py
│   │   └── visualizar_ocorrencia.py
│   ├── utils/
│   │   ├── converter_enum.py
│   │   ├── exibir_card.py
│   │   ├── google_genai.py
│   │   └── input_numero.py
│   ├── requirements.txt
│   └── sistema.py
│
├── .env.example
├── .gitignore
└── README.md
```

### Responsabilidade das pastas e módulos

#### `data/`

Armazena os arquivos CSV utilizados para guardar os dados do projeto (ocorrências, histórico, importação e rejeitados).

#### `docs/`

Reúne os materiais de documentação e entrega acadêmica: link do vídeo, relatório em PDF e documentação sobre o uso de inteligência artificial.

#### `src/models/`

Contém o arquivo `ocorrencia.py`, responsável pela representação dos dados de uma ocorrência. O modelo organiza atributos como identificador, descrição, localização, data, categoria, gravidade e status.

#### `src/repository/`

Contém `CsvRepository.py`, responsável pelas operações de acesso aos arquivos CSV: leitura, cadastro, atualização, inclusão de linhas importadas e registro/consulta do histórico.

#### `src/services/`

Reúne os módulos responsáveis pelas funcionalidades do sistema:

| Arquivo | Responsabilidade |
| --- | --- |
| `analisar_dados.py` | Indicadores: totais, taxa de conclusão e contagens por categoria, gravidade e status. |
| `buscar_ocorrencias.py` | Pesquisa de ocorrências (todas ou por status). |
| `cadastrar.py` | Cadastro de novos registros. |
| `classificacao.py` | Classificação de categoria e gravidade (IA opcional e plano B por palavras-chave). |
| `exibir_ocorrencias_paginadas.py` | Exibição dos registros de forma paginada. |
| `historico.py` | Tela do histórico, do evento mais recente para o mais antigo. |
| `importar.py` | Importação dos registros brutos, validando um a um. |
| `matriz.py` | Matriz categoria × status, hierarquia de pendências e interpretação. |
| `validacao.py` | Regras que recusam registros inconsistentes. |
| `visualizar_ocorrencia.py` | Detalhes de uma ocorrência, com edição de status, gravidade, categoria, descrição e local. |

#### `src/utils/`

Reúne funções auxiliares utilizadas pelo sistema:

| Arquivo | Responsabilidade |
| --- | --- |
| `converter_enum.py` | Conversão de texto para as enumerações. |
| `exibir_card.py` | Apresentação de informações em formato de card. |
| `google_genai.py` | Chamada ao Gemini (usada só se a IA estiver disponível). |
| `input_numero.py` | Apoio à entrada e validação de valores numéricos. |

#### `src/sistema.py`

Ponto de entrada da aplicação (`python src/sistema.py`). Mostra o menu principal e chama os módulos de `services`.

---

## 7. Estruturas de dados e lógica de programação

O projeto utiliza recursos de Python para organizar as informações e implementar as funcionalidades.

Elementos de modelagem: **Enum** (categorias, gravidades e status), **Dataclass** (`Ocorrencia`), **CSV** (persistência) e **funções e módulos** organizados em `models`, `repository`, `services` e `utils`.

Estruturas de dados da atividade, com exemplos reais do código:

| Estrutura | Onde aparece | Como é usada |
| --- | --- | --- |
| **Lista** | `CsvRepository.listar_todos()` | Devolve a lista de todas as ocorrências, percorrida com `for`. |
| **Dicionário** | `analisar_dados.py` | Contadores por categoria, gravidade e status (`categorias["Limpeza"] += 1`). |
| **Pilha (LIFO)** | `historico.py` | O histórico é lido do fim para o início: o evento mais recente fica no topo. |
| **Fila (FIFO)** | `importar.py` | Os registros de `importacao.csv` são processados na ordem de chegada e a fila é esvaziada ao final. |
| **Hierarquia** | `matriz.py` (`montar_hierarquia`) | Dicionário dentro de dicionário: categoria → status → lista de códigos. |
| **Matriz (lista de listas)** | `matriz.py` (`montar_matriz`) | Linhas = categorias, colunas = status, com a contagem em cada célula. |

Condições lógicas com **AND, OR e NOT** (`services/validacao.py`):

```python
# AND + NOT: só confere a categoria se ela foi preenchida
if valor(linha, "categoria") != "" and valor(linha, "categoria") not in valores_do_enum(Categoria):

# OR: possível e-mail na descrição ou no local
if "@" in valor(linha, "descricao") or "@" in valor(linha, "local"):

# NOT: data que não seja real e passada
if valor(linha, "data") != "" and not data_valida(valor(linha, "data")):
```

Também há busca (filtro por status), contagem e percentuais. As decisões de fluxo usam `if/elif/else` e `match/case`.

---

## 8. Regras de negócio e validações

- Cada ocorrência recebe um identificador único (UUID) gerado no cadastro.
- Categorias, gravidades e status seguem as opções padronizadas (Enum).
- O status só avança na ordem **Aberta → Em análise → Concluída**.
- Toda mudança de situação e toda abertura é registrada em `historico.csv`.
- As alterações são persistidas nos arquivos CSV.
- Descrição e local são obrigatórios no cadastro (o campo não pode ficar vazio).

### Validação de registros inconsistentes (opção 5)

`services/validacao.py` confere cada registro importado e devolve a lista de motivos de recusa:

| Regra | Exemplo recusado |
| --- | --- |
| Campos obrigatórios (`id`, `descricao`, `local`, `data`, `status`) | campo em branco |
| Categoria, gravidade e status devem existir nas opções | categoria `Lazer`; status `Resolvida` |
| `id` não pode se repetir | `id` já existente |
| Data real, no formato AAAA-MM-DD e não futura | `31/02/2026` |
| Descrição com no mínimo 5 caracteres | `ok` |
| Sem e-mail na descrição ou no local (privacidade) | texto com `@` |

Os registros recusados vão para `data/rejeitados.csv` com o motivo, e a opção 5 mostra a lista na tela.

---

## 9. Indicadores e análise dos dados

O módulo `analisar_dados.py` calcula os indicadores abaixo; `matriz.py` acrescenta a matriz e a interpretação.

| Indicador | Forma de cálculo |
| --- | --- |
| Total de ocorrências | Quantidade total de registros. |
| Ocorrências por categoria | Contagem de registros em cada categoria. |
| Ocorrências por gravidade | Contagem por nível de gravidade. |
| Ocorrências por status | Contagem por situação atual. |
| Taxa de conclusão | (Concluídas ÷ Total) × 100. |
| Demandas pendentes | Abertas + Em análise. |

**Resultados reais com os dados iniciais** (14 ocorrências):

| Indicador | Valor |
| --- | --- |
| Taxa de conclusão | 28,6% (4 de 14) |
| Pendentes | 10 (8 abertas e 2 em análise) |
| Por categoria | Iluminação 3, Acessibilidade 3, Conservação 3, Limpeza 2 (e 3 sem categoria) |
| Por gravidade | Baixa 5, Alta 4, Média 3, Crítica 1 (e 1 sem gravidade) |

**Interpretação (opção 6):** só 4 de 14 ocorrências foram concluídas, o que indica acúmulo de demandas sem solução.
Acessibilidade e Conservação têm o maior número de pendências (3 cada), e há 5 pendências de gravidade alta ou crítica.
Três registros estão sem categoria e precisam ser revisados. Há empate entre Iluminação, Acessibilidade e Conservação
(3 cada), por isso a "categoria principal" mostrada na opção 3 deve ser lida com cuidado.

---

## 10. Como executar o projeto

Requisito: Python 3.10 ou superior. Na pasta principal do repositório:

```bash
python src/sistema.py
```

Em ambientes nos quais o comando `python` não esteja configurado, use `python3 src/sistema.py`.

O sistema funciona **sem instalar nada**. Para ativar a classificação por IA (opcional):

```bash
pip install -r src/requirements.txt
```

e crie um arquivo `.env` (modelo em `.env.example`) com `GOOGLE_API_KEY=sua_chave`.

Observação: a opção 5 altera os arquivos de `data/` (importa os registros válidos e registra os recusados). Para repetir a demonstração, restaure os dados com `git checkout data/`.

---

## 11. Exemplos de utilização

Exemplos reais da execução (dados fictícios).

### Cadastro de ocorrência

```text
Digite o que aconteceu: Bueiro aberto perigoso na esquina
Digite o local: Rua das Palmeiras
Iniciando Analise Assistida por IA
Erro na chamada a API, usando o Fallback deterministico
Ocorrência cadastrada com sucesso!
```

Sem chave de IA, o plano B classifica por palavras-chave (neste exemplo, gravidade Alta).

### Atualização

Em Pesquisar → Aberta → escolher uma ocorrência → iniciar análise, o status passa de **Aberta** para **Em análise** e a mudança aparece em `historico.csv` e na opção 4.

### Importação e validação (opção 5)

```text
Importação: 2 aceito(s) e 5 recusado(s).

--- REGISTROS RECUSADOS ---
ID 65bed069: Quadra sem manutenção
   categoria desconhecida: 'Lazer'
ID 9bc7b146: Entulho na esquina
   data inválida: '31/02/2026'
ID 81b07a4c: Poste apagado na rua
   id duplicado
ID d506f4e4: Muro com rachaduras
   status desconhecido: 'Resolvida'
ID a14a6be1: ok
   descrição curta demais
```

### Histórico (opção 4)

```text
Total de eventos: 10
2026-11-17 | 17be1d05 | Em análise -> Concluída
2026-11-17 | 17be1d05 | Aberta -> Em análise
2026-11-16 | cdf37634 | Em análise -> Concluída
...
```

### Análise (opção 3)

```text
Total de ocorrências: 14
Taxa de conclusão: 28.6%
Ocorrências pendentes: 10
```

---

## 12. Acessibilidade, inclusão e privacidade

O projeto aborda problemas urbanos que afetam diferentes grupos, especialmente em acessibilidade, mobilidade e conservação dos espaços públicos. Há relação com os **ODS 10 (Redução das desigualdades)** e **11 (Cidades e comunidades sustentáveis)**: a categoria Acessibilidade (calçadas sem rampa, piso tátil danificado) permite dar visibilidade a barreiras enfrentadas por pessoas com mobilidade reduzida.

Sobre o uso do sistema: a interface é apenas de texto, com opções numeradas e mensagens objetivas. Não há modo específico para leitor de tela, o que fica como melhoria futura.

Em relação à privacidade, o sistema não pede nome nem contato, os dados do projeto são fictícios, e a validação recusa registros com e-mail na descrição ou no local. Recomenda-se usar apenas as informações necessárias para identificar e acompanhar cada ocorrência.

---

## 13. Conclusão e limitações

O Neighborhood Action Dashboard apresenta uma proposta de organização e acompanhamento de ocorrências urbanas por meio de uma aplicação desenvolvida em Python.

A solução reúne cadastro, classificação, consulta, edição, validação, histórico e análise de dados, com estrutura modular e arquivos CSV para armazenamento. O desenvolvimento permite aplicar listas, dicionários, pilha, fila, hierarquia, matriz, lógica booleana, organização em módulos e manipulação de arquivos.

**Limitações:**
- O funcionamento depende da qualidade das informações cadastradas.
- Os dados são fictícios e o projeto não se integra a órgãos públicos ou plataformas oficiais.
- A classificação por IA não foi testada com uma chave real durante a documentação; sem ela, o sistema usa palavras-chave, que não reconhecem todos os casos (3 dos 14 registros iniciais ficaram sem categoria).
- A busca na opção 2 é feita por listagem completa ou por status (não há busca por categoria nem por local).
- A opção 5 altera os arquivos de dados.

**Melhorias futuras:** reconhecer mais palavras na classificação, permitir busca por categoria e local, calcular prioridade por reincidência, criar uma interface web e um banco de dados, sempre com validação humana das sugestões automáticas.

---

## 14. Equipe

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