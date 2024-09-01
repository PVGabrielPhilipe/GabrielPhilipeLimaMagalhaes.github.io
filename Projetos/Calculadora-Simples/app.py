from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    numero1 = float(request.form['numero1'])
    numero2 = float(request.form['numero2'])
    operacao = request.form['operacao']

    if operacao == 'soma':
        resultado = numero1 + numero2
    elif operacao == 'subtracao':
        resultado = numero1 - numero2
    elif operacao == 'multiplicacao':
        resultado = numero1 * numero2
    elif operacao == 'divisao':
        resultado = numero1 / numero2
    else:
        resultado = 'Operação inválida'

    return redirect(url_for('resultado', resultado=resultado))

@app.route('/resultado')
def resultado():
    resultado = request.args.get('resultado')
    return render_template('result.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
