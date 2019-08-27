import turtle
import random
t = turtle.Pen()
t.speed(0)
t.up()
t.setx(-200)
t.sety(-200)
t.down()


def kratka(ile):
    krata = 11
    if ile == 2:
        krata = 11
    else:
        for i in range(ile - 2):
            krata = krata + 6
    return krata

def kwiatek(bok, jest_ostatni, pierwszy_rzad):
    kolor = random.randint(1, 3)
    print(kolor)
    if kolor == 1:
        t.color("black", "yellow")
    elif kolor == 2:
        t.color("black", "blue")
    else:
        t.color("black", "red")
    t.begin_fill()
    for kwiatek in range(4):     
        krata = kratka(2)
        t.forward(bok * 2)
        t.left(90)
        t.forward(bok)
        t.right(90)
        t.forward(bok)
        t.right(90)
        t.forward(bok)
        t.left(90)
        t.forward(bok * 2)
        t.left(90)
    t.end_fill()
    t.setheading(0)
    t.up()
    t.forward(bok * 5)
    t.color("black", "grey")
    t.left(90)
    t.forward(bok * 5)
    t.left(90)
    t.forward(bok * 2)
    t.begin_fill()
    t.down()
    if not pierwszy_rzad:
        for m in range(4):
            t.left(90)
            t.forward(bok)
            for g in range(2):
                t.right(90)
                t.forward(bok)
    t.end_fill()
    t.up()
    t.setheading(0)
    t.forward(bok * 2)
    t.right(90)
    t.forward(bok * 3)
    t.setheading(90)
    t.down()
    t.begin_fill()
    if not jest_ostatni:
        for y in range(4):
            t.left(90)
            t.forward(bok)
            for p in range(2):
                t.right(90)
                t.forward(bok)
    t.end_fill()
    t.up()
    t.setheading(270)
    t.forward(bok * 2)
    t.setheading(0)
    t.forward(bok)
    t.down()

def plecionka(ilosc):  
    krata = kratka(ilosc)
    bok = 400 / krata
    for rzad in range(ilosc):
        for kolumna in range(ilosc):
            jest_ostatni = kolumna == ilosc - 1
            pierwszy_rzad = rzad == ilosc - 1
            kwiatek(bok, jest_ostatni, pierwszy_rzad)
        t.up()
        t.left(90)
        t.forward(bok * 6)
        t.left(90)
        t.forward(400 + bok)
        t.setheading(0)
        t.down()
   
plecionka(10)
