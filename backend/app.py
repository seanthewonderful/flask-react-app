from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///avg-joe'
db.init_app()

@app.route('/welcome')
def index():
    return "Welcome to the __Dome__"

if __name__ == "__main__":
    app.run(port=9009, debug=True)