import turtle
#from turtle import...with this you dont need to put forward
print("Hello")

sides = int(input("enter number of sides: "))
length = int(input("How long do you want your side to be?"))
angle=(360/sides)

for repeat in range(sides) :
    turtle.forward(length)
    turtle.right(angle)
