# aula 10 20/11/2019
#
#  web calculadora

nome_pagina = 'calculadora'
from flask import Flask, render_template, request
from aula9 import *

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html',titulo= nome_pagina)
@app.route('/calcular')
def calcular():
    n1 = int(request.args['numero1'])
    n2 = int(request.args['numero2'])
    soma = Soma(n1,n2)
    subtracao = Subtraçao(n1,n2)
    multiplicacao = Multiplicacao(n1,n2)
    divisao_inteira = Divisao(n1,n2)
    divisao_fracionada = Div_frac(n1,n2)
    resto = Resto(n1,n2)
    raiz = Raiz(n1,n2)
    resultado = {'soma':soma,'subtracao':subtracao,'multiplicacao':multiplicacao,'divisao_inteira':divisao_inteira,'divisao_fracionada':divisao_fracionada,'resto':resto,'raiz':raiz}
    
    return render_template(
        'resultado.html'
        ,resultado=resultado
      
        ,soma= soma
       ,subtracao = subtracao
       ,multiplicacao = multiplicacao
       ,divisao_inteira = divisao_inteira
       ,divisao_fracionada = divisao_fracionada
       ,resto = resto
       ,raiz = raiz)

app.run()