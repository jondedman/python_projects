from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Dynamic route for generic pages
@app.route('/generic/<page_name>')
def generic(page_name):
    # Assuming you have a generic.html template that can handle different content based on page_name
    return render_template('generic.html', page_name=page_name)

# Route for the elements page
@app.route('/elements')
def elements():
    return render_template('elements.html')

if __name__ == '__main__':
    app.run(debug=True)
