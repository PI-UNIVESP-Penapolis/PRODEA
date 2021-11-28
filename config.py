import django_heroku

DEBUG = True
import os.path

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
ALLOWED_HOSTS = ["https://prodea.herokuapp.com/"]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(PROJECT_ROOT, 'app', 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'um-nome-bem-seguro'

django_heroku.settings(locals())