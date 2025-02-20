# -*- coding: utf-8 -*-
# main.py

from data_loader import carregar_dados
from collaborative_filtering import filtro_colaborativo
from content_based_filtering import filtro_baseado_conteudo

filmes, ratings, tags = carregar_dados()

rec_df = filtro_colaborativo(filmes, ratings)
sim_df = filtro_baseado_conteudo(filmes, tags)

if __name__ == "__main__":
    print("Dados carregados e modelos preparados!")