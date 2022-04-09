import turtle
import pandas as pd

# Create U.S. States Game
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
list_of_states = data.state.tolist()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's Another State?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in list_of_states:
            if state not in guess_states:
                missing_states.append(state)
        print(f"You got {len(guess_states)}/50 states correct.\nThe missing states are: {missing_states}")
        new_data = pd.DataFrame({"State": missing_states})
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in list_of_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


