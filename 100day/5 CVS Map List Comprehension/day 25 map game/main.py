import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.tracer(0)


image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
    
score = []

def game_over(reason):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.write(f'Game over\n{reason}\nneed to learn {50-len(score)} states', align="center", font=("Arial", 24, "normal"))
    
data = pandas.read_csv("50_states.csv")
def get_mouse_click_coor(x, y):
    print(x, y)
    
screen.update()

def create_state(state):
    global score
    print("state: " + state.title() )
    sel = data[data.state == state.title()]
    print(sel)
    test = turtle.Turtle()
    test.penup()
    test.hideturtle()
    test.goto(sel.x.item(), sel.y.item())
    for i in range(10,1,-1):
        test.write(sel.state.item(), align="center", font=("Arial", i*6, "normal"))
        time.sleep(0.05)
        screen.update()
        test.clear()
    test.write(sel.state.item(), align="center", font=("Arial", 8, "normal"))
     
    score.append(state.lower())

        
input = screen.textinput(title=f'Score {len(score)} / 50', prompt="Guess a state?").title()
print(input)

game_is_on = True

while game_is_on:
    if input == None:
        break
    if input == "exit":
        break

    exists = input in data['state'].values
    already_guessed = input.lower() in score
    
    if exists and not already_guessed:
        create_state(input)
        input = screen.textinput(title=f'Score {len(score)} / 50', prompt="Guess another state?").title()
    elif already_guessed:
        input = screen.textinput(title=f'Score {len(score)} / 50', prompt=f'You already guessed {input}, try again').title()
    else:
        game_is_on = False
        game_over("You guessed wrong")
        break



    
turtle.onscreenclick(get_mouse_click_coor)

list_of_states = data["state"].to_list()
filtered_list = [state.lower() for state in list_of_states if state.lower() not in score]

new_data = pandas.DataFrame(filtered_list)
new_data.to_csv("states_to_learn.csv")



screen.mainloop()

