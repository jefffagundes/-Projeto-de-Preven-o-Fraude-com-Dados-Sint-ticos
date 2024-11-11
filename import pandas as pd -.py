import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# Inicializar Faker
fake = Faker()

# Parâmetros
num_dias = 90  # Número de dias de dados
media_transacoes = 1000  # Média de transações por dia
fraude_rate = 0.02  # Taxa de fraude esperada (2%)
detecao_taxa = 0.9  # Taxa de detecção de fraudes

# Listas para armazenar os dados
datas = []
transacoes = []
fraudes_detectadas = []
fraudes_nao_detectadas = []
valor_fraude = []

# Gerar dados diários
for i in range(num_dias):
    # Verifica o progresso
    print(f"Gerando dados para o dia {i+1} de {num_dias}")
    data = datetime.now() - timedelta(days=i)
    num_transacoes = int(np.random.normal(media_transacoes, 200))

    # Fraudes diárias
    fraudes = int(num_transacoes * fraude_rate)
    fraudes_detectadas_dia = int(fraudes * detecao_taxa)
    fraudes_nao_detectadas_dia = fraudes - fraudes_detectadas_dia

    # Valores associados às fraudes
    valor_medio_fraude = 500  # Valor médio de cada fraude
    valor_total_fraude = fraudes * valor_medio_fraude

    # Armazenar os dados
    datas.append(data)
    transacoes.append(num_transacoes)
    fraudes_detectadas.append(fraudes_detectadas_dia)
    fraudes_nao_detectadas.append(fraudes_nao_detectadas_dia)
    valor_fraude.append(valor_total_fraude)

# Criar DataFrame
df = pd.DataFrame({
    'Data': datas,
    'Transacoes': transacoes,
    'Fraudes_Detectadas': fraudes_detectadas,
    'Fraudes_Nao_Detectadas': fraudes_nao_detectadas,
    'Valor_Fraude': valor_fraude
})

# Calcular KPIs
df['Taxa_Fraude'] = (df['Fraudes_Detectadas'] +
                     df['Fraudes_Nao_Detectadas']) / df['Transacoes']
df['Taxa_Detecao'] = df['Fraudes_Detectadas'] / \
    (df['Fraudes_Detectadas'] + df['Fraudes_Nao_Detectadas'])
df['Perda_por_Fraude'] = df['Valor_Fraude'] / df['Transacoes']

# Modificar o formato da data para o padrão brasileiro
df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')

# Formatação diretamente nas colunas existentes
df['Valor_Fraude'] = df['Valor_Fraude'].apply(
    lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
df['Taxa_Fraude'] = df['Taxa_Fraude'].apply(lambda x: f"{x:,.2%}")
df['Taxa_Detecao'] = df['Taxa_Detecao'].apply(lambda x: f"{x:,.2%}")
df['Perda_por_Fraude'] = df['Perda_por_Fraude'].apply(
    lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
df['Transacoes'] = df['Transacoes'].apply(
    lambda x: f"{x:,.0f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

# Salvar o arquivo CSV com as colunas formatadas
df.to_csv('caminho para salvar', index=False)

# Verificar o tamanho do DataFrame gerado
# Exibe o número de linhas e colunas
print(f"Tamanho do DataFrame: {df.shape[0]} linhas e {df.shape[1]} colunas")

# Exibir a base gerada
print(df.head())
