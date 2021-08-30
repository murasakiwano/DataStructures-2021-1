import turtle
import random

# Árvore fractal desenhada por recursão
def tree(branchLen,t,width):
    if branchLen > 5:
        angulo = random.randint(15,45)
        t.pensize(width)
        t.forward(branchLen)
        t.right(angulo)
        tree(branchLen-random.randint(10,15),t, width-1)
        t.left(2*angulo)
        tree(branchLen-random.randint(10,15),t, width-1)
        t.right(angulo)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(90,t,7)
    myWin.exitonclick()

main()
