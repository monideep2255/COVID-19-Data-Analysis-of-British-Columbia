from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)

Bootstrap(app)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/britishcolumbia')
def britishcolumbia():
    return render_template('index.html')

@app.route('/canada')
def canada():
    return render_template('index.html')

@app.route('/world')
def world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)