#!/usr/bin/python3
import turtle
turtle.shape("turtle")
def circle(direction="left"):
    N = 200
    for _ in range(N):
        turtle.forward(1)
        if direction == "left":
            turtle.left(360/N)
        elif direction == "right":
            turtle.right(360/N)
        else:
            print("ERROR")
            return

def eight():
    circle("left")
    circle("right")

N = 3 
for i in range(N):
    eight()
    turtle.left(180/N)

turtle.mainloop()
