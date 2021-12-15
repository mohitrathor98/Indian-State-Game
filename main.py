import turtle
import pandas as pd

from state import State

screen = turtle.Screen()
screen.title("Indian State Game")

image = "india-blank-map.gif"
screen.addshape(image)

turtle.shape(image)
turtle.resizemode("user")
state_ob = State()

data = pd.read_csv('state.csv')
data_dict = {'state': [state.lower() for state in data['state'].tolist()], 'x': data['X'].tolist(), 'Y': data['Y'].tolist()}

for _ in range(len(data['state'])):
    state_name = turtle.textinput("What's another state name?", "prompt")
    
    if state_name.lower() in data_dict['state']:
        index = data_dict['state'].index(state_name.lower())
        state_ob.write_state(state_name.title(), data_dict['x'][index], data_dict['Y'][index])

turtle.mainloop()