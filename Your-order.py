import turtle as Tur

print("if Do not answer the questions, You will get an error ")
side =  int(input( "be polygonal? "))
width =  int(input( "What is the length of the shape? "))
repeat =  int(input( "How many times to repeat? "))
rotate = int(input( "How many degrees does it rotate in each round? "))
color =  input("Do you want wich once color your shape ? ")

Tur.speed('fastest')

for j in range(repeat):
    Tur.color(color)
    Tur.width(2)
    for i in range(side):
        Tur.forward(width)
        Tur.right(360 / side)
    Tur.right(rotate)
