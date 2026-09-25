#!/usr/bin/python3
import turtle
turtle.shape("turtle")

a = 20
b = 10

for i in range(10):
    for _ in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.penup()
    turtle.backward(b/2)
    turtle.right(90)
    turtle.forward(b/2)
    turtle.left(90)
    turtle.pendown()

    a += b
