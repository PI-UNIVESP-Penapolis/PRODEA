from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField
import wtforms
from wtforms.validators import DataRequired


class CasdastroForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    cnpj = StringField("cnpj", validators=[DataRequired()])
    rua = StringField("rua", validators=[DataRequired()])
    bairro = StringField("bairro", validators=[DataRequired()])
    cidade = StringField("cidade", validators=[DataRequired()])
    cep = StringField("cep", validators=[DataRequired()])
    sobre = TextField("sobre", validators=[DataRequired()])

class Busca(FlaskForm):
    entidade = StringField("entidade", validators=[DataRequired()])