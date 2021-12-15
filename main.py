import turtle
import pandas as pd

from state import State

screen = turtle.Screen()
screen.setup(width=1000, height=1000)

screen.title("Indian State Game")

image = "india-blank-map.gif"
screen.addshape(image)

turtle.shape(image)
turtle.resizemode("user")
state_ob = State()

data = pd.read_csv('state.csv')
data_dict = {'state': [state.lower() for state in data['state'].tolist()], 'x': data['X'].tolist(), 'Y': data['Y'].tolist()}

correctly_guessed = []
while len(correctly_guessed) < len(data_dict['state']):
    state_name = turtle.textinput(f"{len(correctly_guessed)}/{len(data_dict['state'])} states correct", "State Name:").lower()
    
    if (state_name in data_dict['state']) and (state_name not in correctly_guessed):
        correctly_guessed.append(state_name)
        index = data_dict['state'].index(state_name)
        state_ob.write_state(state_name.title(), data_dict['x'][index], data_dict['Y'][index])

turtle.mainloop()