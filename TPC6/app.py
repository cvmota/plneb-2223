from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/engenharia')
def engenharia():
    return render_template('engenharia.html', title="Engenharia")


@app.route('/egua')
def egua():
    return render_template('egua.html', title="Égua")


@app.route('/elefante')
def elefante():
    return render_template('elefante.html', title="Elefante")


app.run(host="localhost", port=3001, debug=True)
