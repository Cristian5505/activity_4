from flask import Flask

app = Flask (__name__)

@app.route('/')
def greeting():
	return "Hello there!"

@app.route('/add/<num1>/<num2>')
def addnums(num1,num2):
	return f'<h1>{num1}+{num2} = {str(int(num1)+int(num2))}</h1>'

@app.route('/mult/<num1>/<num2>')
def multnums(num1,num2):
	return f'<h1>{num1}*{num2} = {str(int(num1)*int(num2))}</h1>'

@app.route('/div/<num1>/<num2>')
def divnums(num1,num2):
	return f'<h1>{num1}/{num2} = {str(int(num1)/int(num2))}</h1>'
