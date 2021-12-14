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
data_dict = data.to_dict()

for _ in range(len(data['state'])):
    state_name = turtle.textinput("What's another state name?", "prompt")
    if state_name.lower

for index, row in data.iterrows():
    state_ob.write_state(row['state'], row['X'], row['Y'])
    #print(row['state'], row['X'], row['Y'])

turtle.mainloop()