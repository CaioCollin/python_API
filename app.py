from flask import Flask , jsonify , request 


app = Flask(__name__)


livros =  [
    {
        'id':1,
        'titulo':  'O senhor dos anéis - A sociedade do Anel',
        'autor' : 'J.R.R Tolkien '
    },
    {
        'id':2,
        'titulo':  'Kratos 2',
        'autor' : 'Caio mesquita collin '
    },
    {
        'id':3,
        'titulo':  'harry potter',
        'autor' : 'potter junior '
    },
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        

@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro  =  request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def remover_livro_por_id(id):
    for idice, livro in enumerate(livros):
        if livro.geet('id') == id:
            del livros[idice]

    return jsonify(livros)

app.run(port=5000, host='localhost',debug=True)

