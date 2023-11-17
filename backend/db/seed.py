from db import db, User
from ..app import app

with app.app_context():
    db.create_all()
    
user = User(
    username = "Sean", 
    email = "poopman@poo.pwop"
)

db.session.add(user)
db.session.commit()

