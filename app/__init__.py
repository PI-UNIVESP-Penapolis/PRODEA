
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.controllers import default
from app.models import tables