from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-number')
def random_number():
    number = random.randint(1, 1000)
    return jsonify({'number': number})

if __name__ == '__main__':
    app.run(debug=True)

