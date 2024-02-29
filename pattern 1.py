from turtle import *

speed('slowest')
pencolor('red')
pensize(3)

for i in range(8):
    fd(80)
    lt(45)
    circle(100,180)
    for i in range(6):
        fd(50)
        lt(60)

hideturtle()
mainloop()

 