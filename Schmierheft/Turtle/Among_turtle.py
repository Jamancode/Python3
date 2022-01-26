#thanks to Ankur Gajurel https://copyassignment.com/author/ankur/

import turtle

# Seite um Farbennamen für Turtle zu finden: https://trinket.io/docs/colors
# Seite für Hex farb codes: https://www.color-hex.com/
color1 = '#b3dca0'
color2 = ''
color3 = 'lightcyan'
color4 = '#ccff00'

turtle.bgcolor("#fff2cd")
s = turtle.getscreen()
t = turtle.Turtle()


def Körper():
    t.pensize(20)

    t.fillcolor(color1)
    t.begin_fill()

    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    t.right(180)
    t.circle(100, -180)

    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    t.circle(40, -180)
    t.left(7)
    t.backward(50)

    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()

    t.right(240)
    t.circle(50, -70)

    t.end_fill()


def Brille():
    t.up()

    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)

    t.down()
    t.fillcolor(color3)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)

    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()


def Rucksack():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(color4)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)

    t.end_fill()


Körper()
Brille()
Rucksack()

turtle.done()