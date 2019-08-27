import turtle
import math

t = turtle.Pen()
#t.speed(0)

def przekatna(bok):
      return math.sqrt(2 * bok * bok)/5 

def romb(ile_rombow, bok):
    t.color('black', 'yellow')
    for o in range(ile_rombow):
        t.down()
        t.begin_fill()
        t.left(45)
        t.forward(przekatna(bok))
        for r in range(3):
            t.right(90)
            t.forward(przekatna(bok))
        t.end_fill()
        t.up()
        t.setheading(0)
        t.forward(bok)
        
def kafelek(bok):
    t.color('black', 'brown')
    t.begin_fill()
    podstawa = (3/5) * bok
    t.up()
    t.forward(1/5 * bok)
    t.down()
    for e in range(4):
        t.forward(podstawa)
        t.left(45)
        t.forward(przekatna(bok))
        t.left(45)
    t.end_fill()
    t.up()
    t.forward(4/5 * bok)
    
def posadzka(ile):
    t.up()
    t.setx(-225)
    t.sety(-225)
    bok = 450 / ile
    for rzad in range(ile):      
        for kolumna in range(ile):
            kafelek(bok)
        t.left(90)
        t.forward(bok)
        t.left(90)
        t.forward(450)
        t.setheading(0)

    t.right(90)
    t.forward((ile - 1) * bok)
    t.setheading(0)
    t.forward((4/5) * bok)
    for r in range(ile - 1):
        romb(ile - 1, bok)
        t.up()
        t.backward(bok * (ile - 1))
        t.left(90)
        t.forward(bok)
        t.right(90)
    
posadzka(5)

