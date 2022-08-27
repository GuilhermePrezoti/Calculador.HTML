from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)#rferência ao objeto FLASK, criando uma váriavel APP que guarda os elementos do Flask


@app.route("/")#Pagina Index - Primeira pagina de qualquer site
def homepage():
    return render_template("index.html")

@app.route("/soma", methods=['Post', 'Get'])
def soma():
    if request.method == 'Post':
        num1 = request.form['num1']
        num2 = request.form['num2']

if __name__ == '__main__':
    app.run(debug=True)
