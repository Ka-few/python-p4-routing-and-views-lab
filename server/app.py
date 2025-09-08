#!/usr/bin/env python3

from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:number>')
def count_route(number):
    lines = [str(i) for i in range(number)]
    return '\n'.join(lines) + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math_route(num1, operation, num2):
    a = float(num1)
    b = float(num2)
    result = ''

    if operation == '+':
        result = str(int(a+b) if a + b == int(a+b) else a + b)
    elif operation == '-':
        result = str(int(a-b) if a - b == int(a-b) else a - b)
    elif operation == '*':
        result = str(int(a * b) if a * b == int(a * b) else a * b)
    elif operation == 'div':
        result = str(a / b)
    elif operation == '%':
        result = str(int(a % b))

    return result


if __name__ == '__main__':
    app.run(port=5555, debug=True)
