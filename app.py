import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from recommendations import recomendar_por_colaboracao, recomendar_por_conteudo
from main import rec_df, sim_df  


filmes = pd.read_csv('ml-latest-small/movies.csv')
lista_de_filmes = filmes['title'].unique()  

app = dash.Dash(__name__)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    style={
        'font-family': 'Arial, sans-serif',
        'background-color': '#f9f9f9',
        'padding': '20px',
        'border-radius': '10px',
        'max-width': '800px',
        'margin': 'auto',
        'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
    },
    children=[
        
        html.H1(
            "🎬 Sistema de Recomendação de Filmes",
            style={
                'text-align': 'center',
                'color': '#333',
                'margin-bottom': '20px',
            }
        ),
        
        
        html.P(
            "Digite ou selecione um filme e receba recomendações personalizadas!",
            style={
                'text-align': 'center',
                'color': '#555',
                'margin-bottom': '30px',
            }
        ),
        
        dcc.Dropdown(
            id='filme-dropdown',
            options=[{'label': filme, 'value': filme} for filme in lista_de_filmes],
            placeholder="🔍 Digite ou selecione um filme...",
            style={
                'width': '100%',
                'padding': '10px',
                'font-size': '16px',
                'border-radius': '5px',
                'border': '1px solid #ccc',
                'margin-bottom': '20px',
            }
        ),
        
        
        dcc.RadioItems(
            id='tipo-recomendacao',
            options=[
                {'label': '👥 Colaborativo', 'value': 'colaborativo'},
                {'label': '📚 Baseado em Conteúdo', 'value': 'conteudo'}
            ],
            value='colaborativo',
            labelStyle={'display': 'inline-block', 'margin-right': '20px'},
            style={'text-align': 'center', 'margin-bottom': '20px'}
        ),
        
        
        html.Button(
            "✨ Gerar Recomendações",
            id='botao-recomendar',
            n_clicks=0,
            style={
                'background-color': '#007bff',
                'color': 'white',
                'border': 'none',
                'padding': '10px 20px',
                'font-size': '16px',
                'border-radius': '5px',
                'cursor': 'pointer',
                'display': 'block',
                'margin': 'auto',
            }
        ),
        
        
        html.Div(
            id='resultado',
            style={
                'margin-top': '30px',
                'text-align': 'center',
            }
        )
    ]
)

@app.callback(
    Output('resultado', 'children'),
    [Input('botao-recomendar', 'n_clicks')],
    [dash.dependencies.State('filme-dropdown', 'value'),
     dash.dependencies.State('tipo-recomendacao', 'value')]
)
def atualizar_recomendacoes(n_clicks, filme, tipo):
    if n_clicks == 0 or not filme:
        return html.Div("Por favor, selecione um filme e clique em 'Gerar Recomendações'.", style={'color': '#999'})
    
    try:
        
        if tipo == 'colaborativo':
            recomendacoes = recomendar_por_colaboracao(filme, rec_df)
        else:
            recomendacoes = recomendar_por_conteudo(filme, sim_df)
        
        return html.Ul(
            [
                html.Li(
                    f"🎥 {titulo} ({score:.2f})",
                    style={'font-size': '18px', 'margin': '10px 0', 'color': '#333'}
                )
                for titulo, score in recomendacoes.items()
            ],
            style={'list-style-type': 'none', 'padding': '0'}
        )
    except KeyError:
        return html.Div(f"Erro: O filme '{filme}' não foi encontrado na base de dados.", style={'color': 'red'})

if __name__ == "__main__":
    app.run_server(debug=True)