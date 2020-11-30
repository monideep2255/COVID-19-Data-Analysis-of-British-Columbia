from flask import Flask, render_template, jsonify
from flask_bootstrap4 import Bootstrap

app = Flask(__name__)

Bootstrap(app)

@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)