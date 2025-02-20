import pandas as pd

def carregar_dados():
    try:
        
        filmes = pd.read_csv('ml-latest-small/movies.csv', dtype={'movieId': str})
        tags = pd.read_csv('ml-latest-small/tags.csv', dtype={'movieId': str})
        ratings = pd.read_csv('ml-latest-small/ratings.csv', dtype={'movieId': str})
        return filmes, ratings, tags
    except FileNotFoundError as e:
        print("Erro ao carregar arquivo: {}".format(e))
        return None, None, None