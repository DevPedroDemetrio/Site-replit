from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [
    {
        'id': 1,
        'titulo': 'Desenvolvedor Web',
        'localidade': 'RJ, Brasil',
        'salario': 'R$ 2.500 '
    },
    {
        'id': 2,
        'titulo': 'Desenvolvedor de Bots',
        'localidade': 'ES, Brasil',
        'salario': 'R$ 2.300 '
    },
    {
        'id': 3,
        'titulo': 'Desenvolvedor de IA',
        'localidade': 'PA, Brasil',
        'salario': 'R$ 7.100 '
    },
    {
        'id': 4,
        'titulo': 'Desenvolvedor Flutter',
        'localidade': 'RS, Brasil',
        'salario': 'R$ 3.500 '
    },
    {
        'id': 5,
        'titulo': 'Desenvolvedor Frontend',
        'localidade': 'PR, Brasil',
        'salario': 'R$ 1.500 '
    },
    {
        'id': 6,
        'titulo': 'Ciêntista de Dados',
        'localidade': 'SC, Brasil',
        'salario': 'R$ 5.500 '
    },
    {
        'id': 7,
        'titulo': 'Desenvolvedor Backend',
        'localidade': 'SP, Brasil',
        'salario': 'R$ 3.500 '
    },
]


@app.route("/")
def index():
  return render_template("index.html", vagas=VAGAS)

@app.route("/vagas")
def lista_vagas():
  return jsonify(VAGAS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
