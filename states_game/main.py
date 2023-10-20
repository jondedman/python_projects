import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# Get the coordinates of the mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
# But this is not needed as coordinates are already given in the csv file, but this is how you get the coordinates of the mouse click. could be useful in other projects

# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
  # This is a list of all the states in the csv file

guesses = []


while len(guesses) < 50:
    score = len(guesses)
    answer_state = screen.textinput(title=f"{len(guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        print(data[data.state == answer_state])
        x = data.x[data.state == answer_state]
        y = data.y[data.state == answer_state]

        # Write the name of the state at the coordinates
        answer = turtle.Turtle()
        answer.hideturtle()
        answer.penup()
        answer.goto(int(x), int(y))
        answer.write(answer_state , align="center", font=("Arial", 8, "normal"))
        guesses.append(answer_state)
        all_states.remove(answer_state)

unguessed_states = [state for state in all_states if state not in guesses]

df = pd.DataFrame(unguessed_states)
output_csv = "states_to_learn.csv"
df.to_csv(output_csv)
print(df)
