import turtle as Tur

Tur.speed('fastest')
Tur.width(2)
for j in range(12):
    for i in range(8):
        Tur.forward(70)
        Tur.right(45)
    Tur.rt(30)
Tur.color('red')
Tur.penup()
Tur.goto(-300,-300)
Tur.pendown()
Tur.write('Milad Soleymani')
Tur.done()