import turtle as Tur

Tur.speed('fastest') # change speed to fastest mode

Tur.width(2) # change thickness of pen

for j in range(12):
    for i in range(8):   # insert ocatagonal
        Tur.forward(70)  # shape side length
        Tur.right(45)    
    Tur.rt(30) # set rotate degree in every repeat 
Tur.color('red') # change color to red
Tur.penup()
Tur.goto(-300,-300) # Change Location of oen
Tur.pendown()
Tur.write('Milad Soleymani') # write namme
Tur.done() # for don't closing after completed codes