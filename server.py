from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return ''

@app.route("/calculator/add", methods=['POST'])
def add():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 + num2
    return render_template('calc.html', result=result, operation='add', num1=num1, num2=num2)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 - num2
    return render_template('calc.html', result=result, operation='subtract', num1=num1, num2=num2)

@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    result = None
    num1 = None
    num2 = None
    operation = None

    if request.method == 'POST':
        operation = request.form.get('operation')
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2

    return render_template('calc.html', result=result, operation=operation, num1=num1, num2=num2)

if __name__ == '__main__':
    app.run(port=8080, host='localhost')
