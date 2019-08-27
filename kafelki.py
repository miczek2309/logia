import turtle
t = turtle.Pen()
t.speed(0)
t.up()
t.setx(-200)
t.sety(-200)
t.down()
        
def kwadracik(kratka, kolor):
    t.color("black", kolor)
    t.begin_fill()
    for i in range(4):
        t.forward(kratka)
        t.left(90)
    t.end_fill()
    t.setheading(0)
    t.forward(kratka)

def kafelek(n_kratek, ilosc):
    m = [
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0]
    ]
    for i in range(ilosc):
        for rzad in m:
            for k in range(ilosc):
                for kol in rzad:
                        if kol == 0:
                            kwadracik(400 / n_kratek, "white")
                        else:
                            kwadracik(400 / n_kratek, "green")
            t.left(90)
            t.forward(400 / n_kratek)
            t.left(90)
            t.setx(-200)
            t.setheading(0)
def kafelki(n):
    n_kratka = 15
    n_kratka = n_kratka * n
    kafelek(n_kratka, n)

kafelki(2)
