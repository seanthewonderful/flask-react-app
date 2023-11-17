from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from config import Config

csrf = CSRFProtect()
db = SQLAlchemy()


def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    csrf.init_app(app)
    db.init_app(app)
    
    return app