from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from Calculator import Calculator

app = Flask(__name__)
# Configure CORS to allow all origins
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})
calculator = Calculator()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST', 'OPTIONS'])
def calculate():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response

    try:
        data = request.get_json()
        operation = data.get('operation')
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        
        result = None
        if operation == 'add':
            result = calculator.add(a, b)
        elif operation == 'subtract':
            result = calculator.subtract(a, b)
        elif operation == 'multiply':
            result = calculator.multiply(a, b)
        elif operation == 'divide':
            result = calculator.divide(a, b)
        
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
