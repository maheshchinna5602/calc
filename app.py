from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    if not operation or num1 is None or num2 is None:
        return jsonify({'error': 'Invalid input'}), 400
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid numbers'}), 400

    result = None
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
