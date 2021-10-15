from flask import template_rendered
from flask.templating import render_template
from wtforms.fields.core import StringField
from app import app, db

from  app.models.forms import CasdastroForm
from app.models.tables import entity

@app.route("/")
@app.route('/home')
def home():
    return render_template('hometeste.html')

@app.route("/prodea")
def prodea():
    return render_template('prodea.html')

@app.route('/cadastre', methods=["POST", 'GET'])
def cadastre():
    form = CasdastroForm()
    if form.validate_on_submit():
        nome = form.nome.data
        cnpj = form.cnpj.data
        sobre = form.sobre.data
        rua = form.rua.data
        bairro = form.bairro.data
        cidade = form.cidade.data
        cep = form.cep.data
    
        entidade = entity(nome, cnpj, rua, bairro, cidade, cep, sobre)
        db.session.add(entidade)
        db.session.commit()
    return render_template('cadastro.html', form=form)

@app.route('/entidades', methods=["POST", "GET"])
def entidades():
    entidades = entity.query.order_by(entity.cidade).all()
    return render_template("lista.html", entidades=entidades)