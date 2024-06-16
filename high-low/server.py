from flask import Flask
import math
import random

app = Flask(__name__)

@app.route('/<int:guess>')
def hello_world(guess):
    answer = math.floor(9 * random.random())
    if guess == answer:
        return '<h1 style="text-align: center;"> You found me! </h1> <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExanpwajBnOXozajBqM3R4NWt6dHV3amtycWNjZWFianhiczdoZTFzMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nGEO47ShV3Us0/giphy.gif">'
    elif guess < answer:
        return '<h1 style="text-align: center;"> Too low! </h1> <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDhxNXJ1eXdhODhpeDQzMDcwbm1jYmV4eHgydDR6NnA2Mzl1dm52bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9rifpVQI2cTQWfeK9m/giphy.gif">'
    elif guess > answer:
        return '<h1 style="text-align: center;"> Too high! </h1> <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjU0N2dqYTIxYmpiand2Nm84N3pqeGN3YXZsaG14cHI1N3c3aDFsaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qW76IdtQdCJPi/giphy.gif">'
    else:
        return '<h1 style="text-align: center;"> Guess a number between 0 and 9 </h1><img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExanpwajBnOXozajBqM3R4NWt6dHV3amtycWNjZWFianhiczdoZTFzMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nGEO47ShV3Us0/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
