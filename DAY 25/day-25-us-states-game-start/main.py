import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S States")
image='blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)
isGameOn=True
data=pandas.read_csv('50_states.csv')
TOTAL=50
STATE=[]
while len(STATE)<50:
    answer_state = screen.textinput(title=f"Guess the State {len(STATE)}/{len(data)}",prompt="Whats another state name").title()
    state=data.state.tolist()


    missing_state=[s for s in state if s not in STATE]
    print(missing_state)
    new_data= pandas.DataFrame(missing_state)
    new_data.to_csv('to_learn.csv')



    if answer_state in STATE:
        pass


    if answer_state in state:
       STATE.append(answer_state)
       x_axis=data[data.state== answer_state]
       t=turtle.Turtle()
       t.hideturtle()
       t.penup()
       t.goto(int(x_axis.x),int(x_axis.y))
       t.write(answer_state,font=("'Ariel',8,'bold'"))



