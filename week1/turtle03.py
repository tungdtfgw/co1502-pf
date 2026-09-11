import turtle as t

# draw a base line
t.forward(200)
t.left(135)
# draw a side line
t.forward(200 / (2 ** 0.5))
t.left(90)
# draw another side line
t.forward(200 / (2 ** 0.5))
t.left(135)

# exit program when clicked
t.exitonclick()