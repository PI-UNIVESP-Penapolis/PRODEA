DEBUG = True
import os.path

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(PROJECT_ROOT, 'app', 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'um-nome-bem-seguro'