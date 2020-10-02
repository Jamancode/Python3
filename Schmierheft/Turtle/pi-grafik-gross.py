import turtle as tu

with open("pi.txt", "r") as f:
    pi = f.read()

lines = 10_000

tu.mode('logo')
tu.tracer(False)
tu.screensize(3000,3000, 'green')
#tu.colormode(255)
tu.pencolor('yellow')

for n in range(lines):
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(10)


tu.done()