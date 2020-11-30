from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from data import fetch_nutrition_score

app = Flask(__name__)

Bootstrap(app)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/anotherpage')
def another_page():
    return render_template('another_page.html')

@app.route('/data')
def nutrition_page():
    nutrition_grades = {}
    products = ['coke', 'chips', 'apple','banana','almonds', 'chicken']

    for item in products:
        grade = fetch_nutrition_score(item)
        nutrition_grades[item] = grade

    return jsonify(nutrition_grades)

if __name__ == '__main__':
    app.run(debug=True)