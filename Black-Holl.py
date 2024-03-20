import turtle as tur
import random

colors = ['blue', 'black']  

colorIndex = 'orange'

colorIndex = random.randint(0, 2)
tur.speed('fastest')

for i in range(570):
    colorI = random.randint(0, 1)
    tur.pencolor(colors[colorI])
    tur.forward(i)
    tur.left(91)
tur.done()
