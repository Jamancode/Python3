import turtle


def bar_graph(var1, value):
    var1.begin_fill()
    var1.left(90)
    var1.forward(value)
    var1.write(" " + str(value))

    var1.right(90)
    var1.forward(40)
    var1.right(90)
    var1.forward(value)
    var1.left(90)
    var1.end_fill()
    var1.forward(10)

turtle.title("Balken und so")
a = turtle.Screen()
a.bgcolor("#FFEFD5")
var1 = turtle.Turtle()
var1.color("green", "chartreuse")
var1.pensize(3)
measureheight = [48, 177, 200, 240, 160, 220]
for i in measureheight:
    bar_graph(var1, i)

a.mainloop()