from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index ():
    return render_template ('index.html')

@app.route('/saludo/<nombre>/<int:edad>')
def saludo(nombre,edad):
    if(edad<18):
        return 'Hola ' + nombre + "eres mayor de edad"
    else:
        return 'Hola ' + nombre + "eres menor de edad"

if __name__ == '__main__':
    app.run(debug=True, port=80)
