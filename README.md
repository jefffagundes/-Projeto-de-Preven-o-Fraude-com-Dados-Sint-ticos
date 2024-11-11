# Projeto de Prevenção à Fraude com Dados Sintéticos

Este projeto gera uma base de dados sintética para simular transações diárias e calcular métricas de prevenção à fraude, como Taxa de Fraude, Taxa de Detecção e Perda por Fraude. Os dados são gerados com a biblioteca **Faker** e são configurados para ajudar no entendimento e análise de fraudes em um cenário fictício.

## 📋 Estrutura do Projeto

- **import pandas as pd**  
  Para manipulação de dados no formato tabular.
  
- **import numpy as np**  
  Utilizado para geração de valores aleatórios e cálculos matemáticos.

- **from faker import Faker**  
  Geração de dados sintéticos de forma realista.

- **from datetime import datetime, timedelta**  
  Manipulação de datas para criação de datas retroativas.

## 📊 Campos e KPIs Calculados

Abaixo estão os campos e cálculos realizados para gerar e interpretar a base de dados:

| **Campo**             | **Descrição**                                                                                                                                                             | **Cálculo/Formula**                                                                                                               |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Transações**         | Número total de transações processadas no dia.                                                                                                                              | Gerado aleatoriamente com uma distribuição normal em torno de uma média (média de 1000 transações/dia).                         |
| **Fraudes Detectadas** | Número de fraudes detectadas entre as transações realizadas no dia.                                                                                                        | Fraudes detectadas = Número de fraudes * Taxa de detecção (geralmente 90% ou outro valor predefinido).                           |
| **Fraudes Não Detectadas** | Fraudes que ocorreram mas não foram detectadas no dia.                                                                                                                  | Fraudes não detectadas = Fraudes totais - Fraudes detectadas.                                                                     |
| **Valor da Fraude**    | O valor total das fraudes que ocorreram no dia.                                                                                                                              | Valor da fraude = Número de fraudes * Valor médio de cada fraude (exemplo: R$ 500 por fraude).                                  |
| **Taxa de Fraude**     | A porcentagem de transações que resultaram em fraude.                                                                                                                      | Taxa de fraude = (Fraudes Detectadas + Fraudes Não Detectadas) / Total de Transações.                                            |
| **Taxa de Detecção**   | A porcentagem de fraudes que foram corretamente identificadas.                                                                                                            | Taxa de detecção = Fraudes Detectadas / (Fraudes Detectadas + Fraudes Não Detectadas).                                           |
| **Perda por Fraude**   | O valor médio perdido por transação, considerando as fraudes.                                                                                                              | Perda por fraude = Valor da fraude / Transações totais.                                                                            |

## 🛠️ Como Rodar o Projeto

### Pré-requisitos
- Python 3.6+
- Pacotes necessários:
  ```bash
  pip install pandas numpy faker
Execute o script principal: 
```bash
python nome_do_script.py
```
 O script gera um arquivo base_prevenção_fraude.csv na pasta especificada, contendo a base de dados simulada para análise de fraude.

 📈 Exemplo de Saída de Dados

 
        Data                    Transacoes  Fraudes_Detectadas  Fraudes_Nao_Detectadas  Valor_Fraude    Taxa_Fraude  Taxa_Detecao  Perda_por_Fraude
        2024-11-09 18:13:18       1309                23                       3            R$13.000        1.98%        86.95%         R$9.93


##  📚 Possíveis Expansões
Adicionar visualizações no Matplotlib ou Seaborn para melhor interpretação dos dados.
Testar diferentes valores de parâmetros, como taxa de fraude e taxa de detecção, para análise de sensibilidade.
Implementar modelos preditivos de machine learning para detectar padrões de fraude.

##  ✨ Contribuição
Se deseja contribuir, fique à vontade para abrir pull requests e issues. Feedbacks e sugestões são bem-vindos!
