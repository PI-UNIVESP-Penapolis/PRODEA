from app import db

class entity(db.Model):
    __tablename__ = "entity"

    nome = db.Column(db.String, primary_key = True, unique = True)
    cnpj = db.Column(db.String, unique = True)
    rua = db.Column(db.String)
    bairro = db.Column(db.String)
    cidade = db.Column(db.String)
    cep = db.Column(db.String)
    sobre = db.Column(db.String)

    def __init__(self, nome, cnpj, rua, bairro, cidade, cep, sobre):
        self.nome = nome
        self.cnpj = cnpj
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.sobre = sobre
    
    def __repr__(self):
        return "<Entidade %r" %self.nome
