import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA

def filtro_colaborativo(filmes, ratings):
    df = filmes.merge(ratings, on='movieId')
    tabela_filmes = pd.pivot_table(df, index='title', columns='userId', values='rating').fillna(0)
    
    # Redução de dimensionalidade com PCA
    pca = PCA(n_components=100)
    tabela_reduzida = pca.fit_transform(tabela_filmes)
    
    # Calcula similaridade de cosseno
    rec = cosine_similarity(tabela_reduzida)
    rec_df = pd.DataFrame(rec, columns=tabela_filmes.index, index=tabela_filmes.index)
    return rec_df