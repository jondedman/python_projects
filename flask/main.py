from flask import Flask

app = Flask(__name__)

def add_bold_decorator(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def add_italic_decorator(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper

def add_underline_decorator(func):
    def wrapper():
        return '<u>' + func() + '</u>'
    return wrapper

@app.route('/')
@add_bold_decorator
@add_italic_decorator
@add_underline_decorator
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
