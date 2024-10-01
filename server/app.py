#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print (parameter)
    return parameter

@app.route('/count/<int:count_value>')
def count(count_value):
    count_str = '\n'.join(str(i) for i in range(count_value)) + '\n'
    return count_str

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation =='+':
        result = num1 + num2
    elif operation =='-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation', 400  # Bad request if operation is invalid

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
