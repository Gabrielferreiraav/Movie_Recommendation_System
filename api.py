from flask import Flask, request, jsonify
from main import rec_df, sim_df 
from recommendations import recomendar_por_colaboracao, recomendar_por_conteudo

app = Flask(__name__)

@app.route('/recomendar', methods=['POST'])

def recomendar():
    data = request.json
    filme = data.get('filme')
    tipo = data.get('tipo')  # 'colaborativo' ou 'conteudo'
    
    if tipo == 'colaborativo':
        recomendacoes = recomendar_por_colaboracao(filme, rec_df)
    elif tipo == 'conteudo':
        recomendacoes = recomendar_por_conteudo(filme, sim_df)
    else:
        return jsonify({"erro": "Tipo inválido"}), 400
    
    return jsonify(recomendacoes.to_dict())

@app.route('/')
def home():
    return "API de Recomendação de Filmes está funcionando!"


if __name__ == "__main__":
    print("Iniciando o servidor Flask...")
    app.run(debug=True)