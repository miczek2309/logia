import turtle
t = turtle.Pen()
t.color(0 ,0.75, 0)
t.speed(0)
t.left(90)

def galozka(A, w_lewo):
    if A == 0:
        if w_lewo:
            t.left(60)
        else:
            t.right(60)
        t.forward(20)
        t.backward(20)
        if w_lewo:
            t.right(60)
        else:
            t.left(60)
    else:
        if w_lewo:
            t.left(60)
        else:
            t.right(60)
        for z in range(A):
            t.forward(20)
            t.right(60)
            for i in range(2):
                t.forward(20)
                t.color("green")
                t.begin_fill()
                t.right(30)
                t.forward(15)
                for x in range(2):
                    t.left(120)
                    t.forward(15)
                t.end_fill()
                t.color(0 ,0.75, 0)
                t.right(30)
                t.forward(20)
                t.right(70)
            t.setheading(90)
            if w_lewo:
                t.left(60)
            else:
                t.right(60)
        t.forward(20)
        t.backward(20 * (A + 1))
    w_lewo = not w_lewo

def drzewo(N):
    w_lewo = True
    for i in range(N + 2):
        t.forward(40)
        galozka(N, w_lewo)
        w_lewo = not w_lewo
        t.setheading(90)
        if N > 0:
            N = N - 1
    t.forward(40)   

drzewo(3)


