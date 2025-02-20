
def recomendar_por_conteudo(filme, sim_df):
    if filme not in sim_df.columns:
        raise KeyError(f"O filme '{filme}' não foi encontrado na base de dados.")
    
    # Remove o próprio filme das recomendações
    serie_similaridade = sim_df[filme].drop(filme, errors='ignore')
    
    
    if serie_similaridade.empty or serie_similaridade.isnull().all():
        raise ValueError(f"Nenhuma recomendação encontrada para o filme '{filme}'.")
    
    # Ordena os valores da série em ordem decrescente
    recomendacoes = serie_similaridade.sort_values(ascending=False).head(10)
    return recomendacoes

def recomendar_por_colaboracao(filme, rec_df):
    # Verifica se o filme existe na matriz de similaridade
    if filme not in rec_df.columns:
        raise KeyError(f"O filme '{filme}' não foi encontrado na base de dados.")
    
    # Ordena os valores da coluna 'filme' em ordem decrescente
    recomendacoes = rec_df[filme].drop(filme, errors='ignore').sort_values(ascending=False).head(10)
    return recomendacoes