import pandas as pd

def recomendar_por_conteudo(filme, sim_df, top_n=5):
    recomendacoes = sim_df[filme].drop(filme, errors='ignore').sort_values(ascending=False).head(10)
    return recomendacoes

def recomendar_por_colaboracao(filme, rec_df):

    if filme not in rec_df.columns:
        raise KeyError(f"O filme '{filme}' não foi encontrado na base de dados.")
    
    
    recomendacoes = rec_df[filme].drop(filme, errors='ignore').sort_values(ascending=False).head(10)
    return recomendacoes