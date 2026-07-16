# alugaFloripa — Previsão de Aluguel Residencial em Florianópolis

Projeto de ciência de dados desenvolvido para o módulo **Desenvolvimento de IA para Análise Preditiva**, com foco na construção de um pipeline completo de regressão para estimar o valor mensal de aluguel residencial em Florianópolis.

**Problema preditivo:** prever o valor mensal de aluguel de imóveis residenciais em Florianópolis.  
**Dataset:** Florianópolis Rent Pricing Dataset — Kaggle.  
**Tipo de problema:** Regressão.  
**Variável-alvo:** `valor`.  
**Modelo entregue:** Regressão Linear — versão `v1`.  
**R² no teste:** 0.7489.  
**MAE no teste:** R$ 2.403,63.  
**RMSE no teste:** R$ 4.469,95.

---

## Sobre o Projeto

O projeto **alugaFloripa** tem como objetivo estimar o valor mensal de aluguel residencial em Florianópolis a partir de características dos imóveis, como tipo, bairro, condomínio, área, quantidade de quartos, banheiros e vagas.

A proposta é simular uma aplicação prática de análise preditiva no mercado imobiliário, utilizando técnicas de preparação de dados, análise exploratória, engenharia de atributos, modelagem supervisionada e avaliação de desempenho.

O modelo pode ser utilizado como uma estimativa inicial para apoiar análises de preço, comparação entre anúncios e identificação de imóveis com valores acima ou abaixo do padrão esperado.

---

## Problema Preditivo

O problema central é responder à seguinte pergunta:

> Com base nas características de um imóvel residencial em Florianópolis, é possível estimar seu valor mensal de aluguel?

A variável que o modelo tenta prever é:

```text
valor
```

Essa variável representa o preço mensal anunciado para aluguel do imóvel.

A previsão desse valor é relevante porque pode auxiliar:

- imobiliárias na análise de preço de anúncios;
- proprietários na definição inicial de aluguel;
- inquilinos na comparação entre imóveis semelhantes;
- analistas na identificação de padrões de mercado;
- sistemas de recomendação ou precificação imobiliária.

---

## Dataset Utilizado

O dataset utilizado foi o **Florianópolis Rent Pricing Dataset**, disponível publicamente no Kaggle.

A base original contém anúncios de imóveis em Florianópolis, com informações como:

- tipo do imóvel;
- bairro;
- valor do aluguel;
- valor de condomínio;
- área;
- quantidade de quartos;
- quantidade de banheiros;
- quantidade de vagas;
- endereço;
- descrição;
- origem do anúncio;
- periodicidade do aluguel.

Para este projeto, foi aplicado um recorte específico:

```text
categoria == "Residencial"
periodicidade == "Mês"
```

Também foram mantidos apenas tipos residenciais, como apartamentos, casas, kitnets, lofts e flats.

---

## Pipeline do Projeto

| Fase | Etapa | Descrição | Principais Resultados |
|------|-------|-----------|----------------------|
| **1** | EDA | Análise exploratória dos dados, dimensões da base, tipos das variáveis, estatísticas descritivas e gráficos analíticos. | Identificação da assimetria do aluguel, relação entre área e valor, correlações numéricas e possíveis variáveis com vazamento de dados. |
| **2** | Data Prep | Limpeza da base, remoção de duplicatas, tratamento de nulos e análise de outliers. | Base reduzida para imóveis residenciais mensais válidos, com 4.454 registros após limpeza. |
| **3** | Feature Engineering | Criação de variáveis derivadas a partir das colunas existentes. | Criação de `area_por_quarto` e `tem_vaga`. |
| **4** | Preparação para Modelagem | Seleção de variáveis, split treino/teste, encoding, análise de multicolinearidade e escalonamento. | Aplicação de One-Hot Encoding em `tipo` e `bairro`, remoção de `area_por_quarto` por alta correlação com `area`, uso de `StandardScaler`. |
| **5** | Modelagem | Treinamento do modelo base de Regressão Linear e comparação entre treino e teste. | Modelo com R² de 0.7770 no treino e 0.7489 no teste, sem evidência forte de overfitting. |
| **6** | Avaliação e Versionamento | Avaliação final, gráficos de real x previsto e resíduos, veredito de negócio e salvamento do modelo v1. | Modelo salvo em `models/v1/modelo_regressao_v1.pkl` e métricas em `models/v1/metricas_v1.json`. |

---

## Estrutura do Projeto

```text
alugaFloripa/
│
├── data/
│   ├── raw/
│   │   └── full_history.csv
│   │
│   ├── processed/
│   │   └── aluguel_floripa_processed.csv
│   │
│   └── final/
│       └── aluguel_floripa_final.csv
│
├── models/
│   └── v1/
│       ├── modelo_regressao_v1.pkl
│       └── metricas_v1.json
│
├── notebooks/
│   └── alugaFloripa_regressao.ipynb
│
├── outputs/
│   └── figures/
│       ├── 01_distribuicao_valor.png
│       ├── 02_scatter_area_valor.png
│       ├── 03_scatter_quartos_valor.png
│       ├── 04_correlation_heatmap.png
│       ├── 05_boxplots_outliers.png
│       ├── 06_real_vs_previsto.png
│       └── 07_residuos_previsto.png
│
├── src/
│   ├── __init__.py
│   ├── data_prep.py
│   ├── evaluation.py
│   ├── features.py
│   └── modeling.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- Joblib
- Jupyter Notebook
- Git
- GitHub
- VS Code

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Acessar a pasta do projeto

```bash
cd alugaFloripa
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Abrir o notebook

```bash
jupyter notebook notebooks/alugaFloripa_regressao.ipynb
```

### 5. Executar as células

Execute o notebook na ordem apresentada.

Durante a execução, o notebook irá:

- carregar o dataset bruto;
- realizar a análise exploratória;
- limpar e tratar os dados;
- criar variáveis derivadas;
- preparar os dados para modelagem;
- treinar e avaliar o modelo;
- gerar gráficos;
- salvar a base processada;
- salvar o modelo versionado;
- salvar as métricas da versão `v1`.

---

## Tratamento dos Dados

Durante a etapa de Data Prep, foram realizadas as seguintes ações:

- filtro da base para imóveis residenciais;
- filtro para anúncios com periodicidade mensal;
- manutenção apenas de tipos residenciais;
- remoção de registros duplicados;
- análise de valores ausentes;
- tratamento de colunas relevantes para o modelo;
- identificação de outliers por boxplot e método IQR;
- análise crítica sobre a permanência de imóveis de alto valor.

Após a limpeza, a base utilizada ficou com:

```text
4.454 imóveis
```

Os outliers de valor mais alto foram mantidos porque muitos representam imóveis reais de alto padrão em Florianópolis, especialmente em regiões valorizadas. A remoção automática desses registros poderia melhorar artificialmente as métricas, mas reduziria a representatividade do mercado imobiliário local.

---

## Variáveis Utilizadas

As variáveis explicativas consideradas no projeto foram:

- `tipo`
- `bairro`
- `condominio`
- `area`
- `qtd_banheiros`
- `qtd_quartos`
- `qtd_vagas`
- `area_por_quarto`
- `tem_vaga`

Durante a preparação para modelagem, a variável `area_por_quarto` foi removida antes do modelo final por apresentar alta correlação com `area`, reduzindo risco de multicolinearidade.

---

## Feature Engineering

Foram criadas duas variáveis derivadas:

### `area_por_quarto`

Representa a área média disponível por quarto:

```text
area_por_quarto = area / qtd_quartos
```

Essa variável foi útil para análise, mas foi removida da modelagem final por alta correlação com `area`.

### `tem_vaga`

Indica se o imóvel possui pelo menos uma vaga de garagem:

```text
tem_vaga = 1 se qtd_vagas > 0
tem_vaga = 0 se qtd_vagas == 0
```

Essa variável foi mantida na modelagem por representar uma característica relevante para o valor do aluguel.

---

## Variáveis Removidas por Vazamento de Dados

Algumas variáveis foram removidas da modelagem por representarem risco de vazamento de dados, ou seja, por carregarem informação direta ou derivada da variável-alvo `valor`.

As principais foram:

- `valor_total`
- `valor_m2`
- `valor_condo_m2`

Essas colunas não foram utilizadas como preditoras porque poderiam fazer o modelo aprender a resposta de forma artificial, prejudicando sua capacidade real de generalização.

---

## Modelagem

O modelo base escolhido foi:

```text
Regressão Linear
```

A escolha da Regressão Linear foi adequada para esta primeira versão por ser um modelo interpretável, direto e compatível com o objetivo do módulo: construir, validar e interpretar um modelo de regressão.

O processo incluiu:

- separação entre treino e teste;
- One-Hot Encoding para variáveis categóricas;
- análise de multicolinearidade com correlação e VIF;
- escalonamento com `StandardScaler`;
- treinamento com `LinearRegression`;
- avaliação com métricas de erro;
- diagnóstico de overfitting;
- retreino final com 100% da base para salvamento do modelo versionado.

---

## Métricas do Modelo

### Desempenho no treino

| Métrica | Resultado |
|--------|-----------|
| MAE | R$ 2.198,12 |
| MSE | 15.293.280,25 |
| RMSE | R$ 3.910,66 |
| R² | 0.7770 |

### Desempenho no teste

| Métrica | Resultado |
|--------|-----------|
| MAE | R$ 2.403,63 |
| MSE | 19.980.462,43 |
| RMSE | R$ 4.469,95 |
| R² | 0.7489 |

---

## Diagnóstico de Overfitting

As métricas de treino e teste ficaram próximas:

```text
R² treino: 0.7770
R² teste: 0.7489
```

O MAE também apresentou diferença moderada:

```text
MAE treino: R$ 2.198,12
MAE teste: R$ 2.403,63
```

Essa proximidade indica que não há evidência forte de overfitting. O modelo apresenta pequena queda no conjunto de teste, mas ainda consegue generalizar para dados não vistos com desempenho semelhante ao observado no treino.

---

## Resultados Gráficos

O projeto gerou gráficos para apoiar a análise exploratória e a avaliação do modelo.

### Distribuição da variável-alvo

Arquivo:

```text
outputs/figures/01_distribuicao_valor.png
```

Esse gráfico mostra a distribuição dos valores de aluguel e evidencia a presença de assimetria, com concentração de imóveis em faixas mais baixas e alguns imóveis com valores muito superiores.

### Relação entre área e valor

Arquivo:

```text
outputs/figures/02_scatter_area_valor.png
```

Esse gráfico mostra que imóveis com maior área tendem a apresentar valores de aluguel mais altos, embora exista dispersão, principalmente em imóveis de maior padrão.

### Relação entre quartos e valor

Arquivo:

```text
outputs/figures/03_scatter_quartos_valor.png
```

Esse gráfico permite observar a relação entre quantidade de quartos e valor do aluguel, indicando que imóveis com mais quartos podem ter valores maiores, mas essa relação não é perfeitamente linear.

### Mapa de correlação

Arquivo:

```text
outputs/figures/04_correlation_heatmap.png
```

O heatmap foi utilizado para analisar correlações entre variáveis numéricas e identificar possíveis problemas de multicolinearidade.

### Boxplots de outliers

Arquivo:

```text
outputs/figures/05_boxplots_outliers.png
```

Os boxplots ajudaram a identificar valores extremos em variáveis como `valor`, `area`, `qtd_banheiros`, `qtd_quartos` e `qtd_vagas`.

### Real x Previsto

Arquivo:

```text
outputs/figures/06_real_vs_previsto.png
```

Esse gráfico compara os valores reais de aluguel com os valores previstos pelo modelo. Pontos próximos à linha ideal indicam previsões mais precisas.

### Resíduos x Previsto

Arquivo:

```text
outputs/figures/07_residuos_previsto.png
```

Esse gráfico analisa os erros do modelo. Foi observada maior dispersão dos resíduos em imóveis de valor mais alto, indicando que o modelo apresenta mais dificuldade para prever imóveis de alto padrão.

---

## Interpretação de Negócio

O modelo apresentou bom desempenho geral para uma primeira versão, com R² de 0.7489 no conjunto de teste. Isso indica que o modelo conseguiu explicar aproximadamente 74,89% da variação dos valores de aluguel no conjunto de teste.

O MAE de R$ 2.403,63 significa que, em média, o modelo erra a previsão do aluguel mensal em cerca de R$ 2,4 mil.

Esse erro deve ser interpretado com cautela, pois seu impacto muda conforme a faixa de preço do imóvel. Para um imóvel de aluguel alto, como R$ 20.000, esse erro pode ser proporcionalmente menor. Já para um imóvel de R$ 5.000, o mesmo erro representa uma diferença percentual muito mais relevante.

Por isso, o modelo não deve ser usado sozinho para definir o valor final de um aluguel. Ele é mais adequado como uma estimativa inicial ou ferramenta de apoio para comparar se um imóvel está anunciado acima ou abaixo do padrão esperado.

---

## Versionamento do Modelo

A versão entregue do modelo é:

```text
v1
```

Os arquivos da versão `v1` estão em:

```text
models/v1/
```

Arquivos salvos:

```text
models/v1/modelo_regressao_v1.pkl
models/v1/metricas_v1.json
```

O arquivo `.pkl` contém o artefato final do modelo, incluindo:

- modelo treinado;
- scaler final;
- colunas utilizadas na modelagem.

O arquivo `.json` contém:

- versão do modelo;
- data de treinamento;
- modelo utilizado;
- features utilizadas;
- métricas de treino;
- métricas de teste;
- observação sobre a avaliação honesta com split treino/teste.

---

## Melhorias Futuras

Algumas melhorias podem ser aplicadas em versões futuras do projeto:

- testar transformação logarítmica da variável `valor`;
- avaliar métricas percentuais, como MAPE;
- segmentar os imóveis por faixa de preço;
- criar modelos específicos para imóveis de alto padrão;
- comparar a Regressão Linear com modelos não lineares, como Random Forest, KNN Regressor ou Decision Tree Regressor;
- incluir novas variáveis de localização;
- enriquecer o dataset com dados externos, como proximidade da praia, região da cidade ou indicadores de infraestrutura;
- transformar o fluxo em um pipeline completo com `Pipeline` e `ColumnTransformer` do scikit-learn;
- criar uma interface simples para simular previsões de aluguel.

---

## Reprodutibilidade

As dependências principais do projeto estão registradas no arquivo:

```text
requirements.txt
```

Para instalar as dependências, utilize:

```bash
pip install -r requirements.txt
```

---

## Git e Versionamento

O projeto foi desenvolvido com controle de versão utilizando Git e GitHub.

A organização seguiu uma estratégia baseada em branches:

- `main`: branch principal do projeto;
- `develop`: branch de integração;
- `feature/*`: branches específicas para cada etapa do desenvolvimento.

As principais etapas foram desenvolvidas em branches separadas, como:

- estrutura inicial do projeto;
- adição do dataset;
- análise exploratória;
- tratamento dos dados;
- feature engineering;
- preparação para modelagem;
- modelagem e validação;
- avaliação e versionamento;
- documentação final.

Essa organização permitiu manter um histórico de commits mais claro e acompanhar a evolução lógica do projeto.

---

## Conclusão

O projeto **alugaFloripa** demonstrou a construção de um pipeline completo de análise preditiva aplicado ao mercado imobiliário de Florianópolis.

Foram realizadas etapas de análise exploratória, limpeza dos dados, tratamento de outliers, criação de variáveis derivadas, preparação para modelagem, treinamento, avaliação e versionamento do modelo.

A Regressão Linear apresentou desempenho adequado para uma primeira versão, com R² de 0.7489 no teste e MAE de R$ 2.403,63. O modelo conseguiu capturar parte relevante dos padrões de formação do aluguel, especialmente em imóveis de valor baixo e intermediário.

Apesar disso, a maior dispersão dos erros em imóveis de valor mais alto indica que versões futuras podem se beneficiar de transformações na variável-alvo, segmentação por faixa de preço ou uso de modelos não lineares.

---

## Autor

Cristina Freitas

Projeto desenvolvido para o curso **Desenvolvimento de IA para Análise Preditiva**, no programa SCTEC.
