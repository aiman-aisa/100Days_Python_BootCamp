import turtle
import pandas as pd

states_df = pd.read_csv(r"Day-25-Pandas-csv\us-states-game\50_states.csv")
states = states_df["state"].to_list()
# print(states_df.loc[states_df.state == "Tennessee", 'x'].iloc[0])
# print(states_df.loc[states_df.state == "Tennessee", 'y'].iloc[0])

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"Day-25-Pandas-csv\us-states-game\blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
# print(answer_state)
# print(states)

correct_state = []

while len(correct_state) < 50:
    answer_state = screen.textinput(title=f"{len(correct_state)}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in correct_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(r"Day-25-Pandas-csv\us-states-game\states_to_learn.csv")
        break
    
    if answer_state in states and answer_state not in correct_state:
        correct_state.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = states_df[states_df.state == answer_state]
        # x = states_df.loc[states_df.state == answer_state, 'x'].iloc[0]
        # y = states_df.loc[states_df.state == answer_state, 'y'].iloc[0]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=("Arial", 8, "normal"))
        
        

            
    

    

# def get_mouse_click_coor(x, y):
#     print(x, y)
    

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen.exitonclick()