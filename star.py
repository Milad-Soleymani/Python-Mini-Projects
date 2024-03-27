import turtle as tur
import random

tur.shape('triangle')
tur.shapesize(0.3)
tur.color('yellow')

tur.speed(10)

colors = ['pink', 'yellow', 'orange','blue'] 


for j in range (7):
    tur.color(colors[random.randint(0, 3)])
    tur.backward(100)
    for i in range (5):
        tur.forward(100)
        tur.rt(144)

tur.forward(1400)


for a in range (7):
    tur.color(colors[random.randint(0, 3)])
    tur.backward(100)
    for b in range (5):
        tur.forward(100)
        tur.rt(144)


tur.done()