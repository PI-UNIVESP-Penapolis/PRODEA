from flask import template_rendered
from flask.templating import render_template
from app import app

@app.route("/")
def route():
    return "teste"