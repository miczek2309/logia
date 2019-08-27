import turtle
t = turtle.Pen()

bok = 100
czy = True

def kwadrat_bialy():
    for k in range(4):
        t.forward(bok)
        t.left(90)

def kwadrat_czarny():
    t.color(0, 0, 0)
    t.begin_fill()
    for c in range(4):
        t.forward(bok)
        t.left(90)
    t.end_fill()

def rzad(ilosc):
    global czy
    if ilosc % 2 == 0:
        czy = not czy
    for r in range(ilosc):
        if czy:
            kwadrat_bialy()
        else:
            kwadrat_czarny()
        t.forward(bok)
        czy = not czy

def szachownica(rozmiar):
    t.up()
    t.setx(-1 * rozmiar * bok * 0.5)
    t.sety(1 * (rozmiar * 0.5 - 1) * bok)
    t.down()
    for h in range(rozmiar):
        rzad(rozmiar)
        t.up()
        t.right(90)
        t.forward(bok)
        t.right(90)
        t.forward(bok * rozmiar)
        t.setheading(0)
        t.down()
        
szachownica(5)    
