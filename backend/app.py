from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/welcome')
def index():
    return "Welcome to the __Dome__"

if __name__ == "__main__":
    app.run(port=9009, debug=True)