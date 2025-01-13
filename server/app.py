#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>/', strict_slashes=False)
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>/', strict_slashes=False)
def count(parameter):
    count = ''
    for i in range(parameter):
        count += str(i) + '\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>/', strict_slashes=False)


def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div" or operation == "/":  
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == "%":  
        result = num1 % num2
    else:
        return "Error: Invalid operation"
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
