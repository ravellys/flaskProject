from flask import Flask

app = Flask(__name__)


@app.route('/<string:metodo>/<string:var1>/<string:var2>')
def triangulo_retangulo(var1, var2, metodo):

    try:
        lados = [float(var1), float(var2)]
        aprox = 4
    except ValueError as ve:
        return {'statusCode': 400, 'message': f'The Parameter is Wrong {ve}'}

    if metodo == 'calcular_hipotenusa':
        hipotenusa = round((lados[0] ** 2 + lados[1] ** 2) ** 0.5, aprox)
        lados.append(hipotenusa)
        lados.sort(reverse=True)
        relacao = {'statusCode': 200,
                   "hipotenusa": lados[0],
                   "cateto_maior": lados[1],
                   "cateto_menor": lados[2]}
        return relacao

    elif metodo == 'calcular_cateto':
        if lados[0] != lados[1]:
            cateto = round((max(lados) ** 2 - min(lados) ** 2) ** 0.5, aprox)
            lados.append(cateto)
            lados.sort(reverse=True)
            relacao = {'statusCode': 200,
                       "hipotenusa": lados[0],
                       "cateto_maior": lados[1],
                       "cateto_menor": lados[2]}
            return relacao
        else:
            return {'statusCode': 400, 'message': 'Error: hipotenusa = cateto'}
    else:
        return {'statusCode': 400, 'message': "Error: método inválido"}


if __name__ == '__main__':
    app.run(debug=True)
