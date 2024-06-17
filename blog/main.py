from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    r = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = r.json()
    print(data)


    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
