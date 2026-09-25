#!/usr/bin/python3
import turtle
turtle.shape("turtle")
N = 12
for i in range(N):
    turtle.left(360/N)
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)

