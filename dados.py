import pandas as pd
import sqlite3 as sq
# Lendo o arquivo Excel
def ler(abrir):
   df = pd.read_csv(abrir)
   return df
    
# Remove as linhas com valores ausentes do DataFrame e retorna o DataFrame limpo.
def limpa_dados(df):
    df = df.dropna()
    return df


def ordenar_por_idade(df):
    df = df.sort_values(by='Age')  # Substitua 'idade' pelo nome correto da coluna de idade
    return df


def remover_coluna_outcome(df):
    if 'Outcome' in df.columns:  # Verifica se a coluna 'outcome' existe
        df = df.drop(columns=['Outcome'])  # Remove a coluna 'outcome'
    return df

def salvar_csv(df, arquivo):
    df.to_csv(arquivo, index=False)
    
# Função para criar banco de dados SQLite
def criar_banco_de_dados(df, nome_db):
    conn = sq.connect(nome_db)  # Conectar ao banco de dados SQLite (será criado se não existir)
    df.to_sql('diabetes', conn, if_exists='replace', index=False)  # Cria uma tabela 'diabetes' e insere os dados
    conn.commit()  # Salva as alterações
    conn.close()  # Fecha a conexão 
    
def visualizar_banco(nome_db):
    conn = sq.connect(nome_db)
    query = "SELECT * FROM diabetes WHERE Glucose > 100 LIMIT 100"  # Limita a 10 primeiros registros
    df = pd.read_sql(query, conn)
    print(df.head(100))  # Exibe as 10 primeiras linhas
    conn.close()


df = ler('diabetes.csv')
df_limpo = limpa_dados(df)
df_ordenado = ordenar_por_idade(df_limpo)
df_remove = remover_coluna_outcome(df_ordenado)
criar_banco_de_dados(df_remove, 'diabetes.db')
visualizar_banco('diabetes.db')



