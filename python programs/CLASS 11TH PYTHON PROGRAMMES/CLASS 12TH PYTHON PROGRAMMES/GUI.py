import turtle as t
m = t.Turtle()
m.screen.bgcolor('white')
m.left(90)
m.speed(100)
m.color('black')
m.pensize(5)
m.screen.title('GUI')


def f(blen):
    if blen < 10:
        return
    else:
        m.forward(blen)
        m.left(30)
        f(3*blen/4)
        m.right(60)
        f(3*blen/4)
        m.left(30)
        m.backward(blen)


f(100)
m = t.done()
'''
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(180):
    t.pencolor(colors[x % 5])
    t.width(x/100+1)
    t.forward(x)
    t.left(60)
'''
