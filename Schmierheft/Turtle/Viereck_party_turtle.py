import turtle as t

pen = t.Turtle()
pen.color("cyan")
pen.speed(0)
colors = ["green","black","orange","navy","green","black","orange","navy"]

def draw_square(color):
        for side in range(4):
                pen.forward(100)
                pen.right(90)
                for side in range(4):
                        pen.forward(50)
                        pen.right(90)

pen.penup()
pen.back(40)
pen.pendown()

for color in colors:
        pen.color(color)
        draw_square(color)
        pen.forward(50)
        pen.left(45)

pen.hideturtle()
t.done()