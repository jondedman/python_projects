from flask import Flask, render_template
import requests


app = Flask(__name__)

r = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
DATA = r.json()

@app.route('/')
def home():
    return render_template("index.html", data=DATA)

@app.route('/posts<int:id>')
def get_post(id):
    for blog in DATA:
        if blog['id'] == id:
            return render_template("post.html", blog=blog)
        else:
            return render_template("index.html", data=DATA)





if __name__ == "__main__":
    app.run(debug=True)
