from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form['un']
        pw = request.form['pw']
        return 'hello ' + name + ' your password is ' + pw
    else:
        return render_template('simple_form.html')
