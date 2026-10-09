import turtle as t

length = int(input("Enter the length of polygon\'s side: "))
n = int(input("Enter the number of sides: "))
angle = 360 / n

for i in range(n):
    t.forward(length)
    t.left(angle)

t.exitonclick()