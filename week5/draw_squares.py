import turtle as t

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

def draw_flowers(n_leaves, size):
    for i in range(n_leaves):
        draw_square(size)
        t.left(360/n_leaves)


# Main program

t.speed(0)  # fastest speed

leaves = 20
size = 50
draw_flowers(leaves, size)

t.exitonclick()