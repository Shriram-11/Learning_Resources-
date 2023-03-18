import turtle
import time
screen=turtle.Screen()
screen.title('Pong')
screen.bgcolor('#f0f0f0')

def lef():
    lpad=turtle.Turtle()
    lpad.color('black')
    lpad.pensize(2)
    lpad.shape('circle')
    lpad.penup()
    print('Left Pad:')
    for a in range(0,20):
        lpad.forward(4)
        time.sleep(0.01)
        print(lpad.xcor())
lef()
i=input()
