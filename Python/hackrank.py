import turtle


def draw(t, sz):
    for i in ["red", "black", "gray"]:
        t.color(i)
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
ale = turtle.Turtle()
ale.pensize(3)

size = 30

for i in range(15):
    draw(ale, size)
    size = size + 10
    ale.forward(10)
    ale.right(18)

wn.mainloop()
