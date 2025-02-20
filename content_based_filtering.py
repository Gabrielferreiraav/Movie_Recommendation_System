import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def filtro_baseado_conteudo(filmes, tags, preferencias=None):
    filmes['movieId'] = filmes['movieId'].astype(str)
    df2 = filmes.merge(tags, on='movieId', how='left')
    
    # Combina informações relevantes
    df2['Infos'] = df2['genres'].fillna("") + " " + df2['tag'].fillna("")
    
    if preferencias:
        df2 = df2[df2['genres'].str.contains(preferencias, case=False)]
    
    # Processamento TF-IDF
    vec = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=5000)
    tfidf = vec.fit_transform(df2['Infos'])
    
    # Calcula similaridade de cosseno
    sim = cosine_similarity(tfidf)
    sim_df = pd.DataFrame(sim, columns=df2['title'], index=df2['title'])
    
    return sim_df