import turtle
import math

t = turtle.Pen()
t.color(0, 0.5, 0)

def domek():
    t.begin_fill()
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(30)
    t.forward(40)
    t.left(120)
    t.forward(40)
    t.left(30)
    t.forward(20)
    t.setheading(0)
    t.end_fill()
    
def piramida(ile):
    if ile == 0:
        return
    for i in range(ile):
        domek()
        t.forward(40)
    t.up()
    t.left(90)
    t.forward(math.sqrt(3200))
    t.left(90)
    t.forward(40 * ile - 20)
    t.setheading(0)
    t.down()
    piramida(ile - 1)
    
piramida(7)


