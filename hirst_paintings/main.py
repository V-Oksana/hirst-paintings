import turtle
import random

my_screen = turtle.Screen()
my_screen.colormode(255)
my_screen.setup(1000, 1000, 5)

my_colors = [(239, 221, 114), (18, 111, 193), (224, 59, 93), (235, 150, 74), (142, 88, 49),
             (115, 147, 211), (212, 127, 164), (34, 195, 118), (107, 106, 195), (137, 182, 20),
             (189, 17, 39), (232, 55, 45), (245, 147, 183), (112, 191, 149), (190, 47, 70),
             (19, 186, 208), (44, 52, 106), (145, 229, 168), (135, 220, 239), (202, 211, 7),
             (18, 154, 118), (239, 171, 152), (33, 43, 76), (111, 42, 40), (179, 174, 225), (250, 7, 37)]

pablo = turtle.Turtle()
pablo.speed("fastest")
pablo.shape("turtle")
pablo.pensize(20)
pablo.penup()
pablo.goto(-250, 250)


for hght in range(10):
    for len in range(10):
        pablo.color(random.choice(my_colors))
        pablo.pendown()
        pablo.forward(1)
        pablo.penup()
        pablo.forward(49)
    pablo.forward(-500)
    pablo.right(90)
    pablo.forward(49)
    pablo.left(90)

pablo.hideturtle()

my_screen.exitonclick()