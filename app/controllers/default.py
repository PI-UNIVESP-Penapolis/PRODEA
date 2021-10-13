from flask import template_rendered
from flask.templating import render_template
from app import app

from  app.models.forms import CasdastroForm

@app.route("/")
@app.route('/home')
def home():
    return render_template('hometeste.html')

@app.route('/entidades')
def entidades():
    return render_template('entidades.html')

@app.route('/cadastre')
def cadastre():
    form = CasdastroForm()
    return render_template('cadastro.html', form=form)