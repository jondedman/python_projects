from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    current_year = datetime.datetime.now().year
    random_number = random.randint(1, 100)
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
   age_response = requests.get(url=f"https://api.agify.io?name={name}")
   age_data = age_response.json()
   age = age_data['age']

   gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
   gender_data = gender_response.json()
   gender = gender_data['gender']
   return render_template('index.html', name=name, age=age, gender=gender)




if __name__ == '__main__':
    app.run(debug=True)
