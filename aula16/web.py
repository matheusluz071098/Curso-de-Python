from flask import flask, render_template
from faixa import 

app = flask(__name__)


@app.route('/lista')
def listar_faixas():
    return render_template("lista.html",nome = 'lista de faixa')


app.run()