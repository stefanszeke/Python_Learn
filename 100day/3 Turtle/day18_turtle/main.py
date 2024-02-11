from turtle import Turtle, Screen

t = Turtle()

# t.color("pink")
# t.forward(100)

# t.color("red")
# t.left(90)
# t.forward(100)

# t.color("green")
# t.left(90)
# t.forward(100)

# t.color("blue")
# t.left(90)
# t.forward(100)

colors = ['red', 'green', 'blue', 'purple', 'pink', 'orange', 'yellow']

def incr(num, max) -> int:
    if num == max-1:
        return 0
    else:
        return num+1

t.speed(0)

length = 100
inset = 5
fill_index = 0
for step in range(10):
    
    # t.fillcolor("blue")
    
    print(colors[fill_index])
    
    # fill_index = incr(fill_index, len(colors))

    # t.begin_fill()
    for step in range(4):
        t.color(colors[step])
        t.forward(length)
        t.left(90)
    # t.end_fill()
    
    
    t.left(90)
    t.penup()
    t.forward(inset)
    t.right(90)
    t.forward(inset)
    t.pendown()
    length -= inset*2
    



# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         t.color(c)
#         t.forward(steps*2)
#         t.right(20)

screen = Screen()
screen.listen()
screen.exitonclick()