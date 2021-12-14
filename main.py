import turtle
import pandas as pd

from state import State

screen = turtle.Screen()
screen.title("Indian State Game")

image = "india-blank-map.gif"
screen.addshape(image)

turtle.shape(image)
turtle.resizemode("user")

data = pd.read_csv('state.csv')
for _ in len(data['state']):
    print(turtle.textinput("What's another state name?", "prompt"))
# placing all state names at their respective positions

state_ob = State()
for index, row in data.iterrows():
    state_ob.write_state(row['state'], row['X'], row['Y'])
    #print(row['state'], row['X'], row['Y'])

turtle.mainloop()