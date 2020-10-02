import turtle as tu

with open("pi.txt", "r") as f:
    pi = f.read()

lines = 100

tu.mode('logo')
for n in range(lines):
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(50)


tu.done()