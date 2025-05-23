from flask import Flask, jsonify, render_template

app = Flask(__name__)
counter = 0  # Global variable to store the counter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-number')
def random_number():
    global counter
    counter += 1
    return jsonify({'number': counter})

if __name__ == '__main__':
    app.run(debug=True)

