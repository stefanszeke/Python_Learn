# from turtle import Turtle, Screen

# jack = Turtle()
# jack.shape("turtle")
# jack.color("darkOrchid")

# jack.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)