from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
# from ..app import app

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///avg-joe"
db.init_app()


from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
with app.app_context():
    db.create_all()
    
user = User(
    username = "Sean", 
    email = "poopman@poo.pwop"
)

db.session.add(user)
db.session.commit()