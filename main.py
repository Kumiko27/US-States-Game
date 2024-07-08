import turtle
import pandas
from stateboard import StateGame

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_label = StateGame()

# Get coordinated of the image for state and save in the csv file
# def get_mouse_click_coor(x,y)
#   print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

correct_guesses = []
states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        state_row = states_data[states_data.state == answer_state]
        correct_guesses.append(answer_state)
        state_label.update_state_game(answer_state, state_row.x.iloc[0], state_row.y.iloc[0])


incorrect_guesses = [state for state in all_states if state not in correct_guesses]
print(incorrect_guesses)
new_file = pandas.DataFrame(incorrect_guesses)

new_file.to_csv("states to learn.csv")

