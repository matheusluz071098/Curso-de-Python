def CalculoInvestimento(valor,meses):
    resultado = valor
    for i in range(meses):
        lucro = resultado * 0.05
        resultado +=lucro   


    return resultado
