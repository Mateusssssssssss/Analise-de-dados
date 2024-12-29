import pandas as pd

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


df = ler('diabetes.csv')
df_limpo = limpa_dados(df)
df_ordenado = ordenar_por_idade(df_limpo)
df_remove = remover_coluna_outcome(df_ordenado)
salvar_csv(df_remove, 'diabetes.csv')
print(df_remove.head(10)) 

