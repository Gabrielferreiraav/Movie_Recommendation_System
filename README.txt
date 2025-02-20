
# Sistema de Recomendação de Filmes

Este projeto é um sistema de recomendação de filmes que utiliza técnicas de filtragem colaborativa e baseada em conteúdo para sugerir filmes aos usuários. O sistema foi desenvolvido como parte de um portfólio para demonstrar habilidades em ciência de dados, machine learning e desenvolvimento de aplicações web.

## Funcionalidades

- **Recomendação Colaborativa**: Utiliza a técnica de filtragem colaborativa para recomendar filmes com base nas avaliações de outros usuários.
- **Recomendação Baseada em Conteúdo**: Utiliza a técnica de filtragem baseada em conteúdo para recomendar filmes com base em características como gênero e tags.
- **Interface Web**: Uma interface web desenvolvida com Dash permite que os usuários selecionem um filme e recebam recomendações personalizadas.
- **API RESTful**: Uma API desenvolvida com Flask permite que outras aplicações consumam o sistema de recomendação.

## Tecnologias e Bibliotecas Utilizadas

- **Python**: Linguagem de programação principal.
- **Pandas**: Para manipulação e análise de dados.
- **Scikit-learn**: Para cálculo de similaridade e redução de dimensionalidade (PCA).
- **Flask**: Para desenvolvimento da API RESTful.
- **Dash**: Para desenvolvimento da interface web.
- **TfidfVectorizer**: Para processamento de texto e cálculo de similaridade baseada em conteúdo.

## Estrutura do Projeto

- **api.py**: Contém a implementação da API RESTful usando Flask.
- **app.py**: Contém a implementação da interface web usando Dash.
- **collaborative_filtering.py**: Implementa a filtragem colaborativa.
- **content_based_filtering.py**: Implementa a filtragem baseada em conteúdo.
- **data_loader.py**: Responsável por carregar os dados dos filmes, avaliações e tags.
- **main.py**: Script principal que carrega os dados e gera as matrizes de similaridade.

## Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Gabrielferreiraav/Movie_Recommendation_System
   cd sistema-recomendacao-filmes
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a API**:
   ```bash
   python api.py
   ```

4. **Execute a interface web**:
   ```bash
   python app.py
   ```

5. **Acesse a interface web**:
   Abra o navegador e acesse `http://127.0.0.1:8050/`.


# Caso queira testar a API pode executar um **curl** como :
curl -X POST http://127.0.0.1:5000/recomendar      -H 
"Content-Type: application/json"      -d '{"filme": "Stretch (2014)", "tipo": "colaborativo"}'
## Contato

Para mais informações, entre em contato através do email: gabriel.vianafr@gmail.com.

---

Este projeto foi desenvolvido como parte de um portfólio para demonstrar habilidades em ciência de dados e desenvolvimento de aplicações web. Sinta-se à vontade para explorar e utilizar o código!
