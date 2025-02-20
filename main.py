# -*- coding: utf-8 -*-
# main.py

from data_loader import carregar_dados
from collaborative_filtering import filtro_colaborativo
from content_based_filtering import filtro_baseado_conteudo

# Carrega os dados
filmes, ratings, tags = carregar_dados()

# Gera as matrizes de similaridade
rec_df = filtro_colaborativo(filmes, ratings)
sim_df = filtro_baseado_conteudo(filmes, tags)

if __name__ == "__main__":
    # Este bloco só será executado se o script for rodado diretamente
    print("Dados carregados e modelos preparados!")