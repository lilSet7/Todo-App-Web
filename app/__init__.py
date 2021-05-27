from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate



app = Flask(__name__)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = "login"
migrate = Migrate(app, db)

app.config["SECRET_KEY"] = "essa-é-uma-chave-secreta"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite/"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from app import routes, models