from flask import template_rendered
from flask.templating import render_template
from app import app

@app.route("/")
def route():
    return "teste"

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/entidades')
def entidades():
    return render_template('entidades')