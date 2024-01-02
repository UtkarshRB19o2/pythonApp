from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/addition', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return render_template('addition_result.html', result=result)
    return render_template('addition.html')

@app.route('/eligibility', methods=['GET', 'POST'])
def eligibility():
    if request.method == 'POST':
        age = int(request.form['age'])
        result = check_eligibility_logic(age)
        return render_template('eligibility_result.html', result=result)
    return render_template('eligibility.html')

def check_eligibility_logic(age):
    if age < 18:
        return 'Not eligible for driving. Must be 18 or above.'
    else:
        return 'Eligible for driving. Congratulations!'

if __name__ == '__main__':
    app.run(debug=True)
