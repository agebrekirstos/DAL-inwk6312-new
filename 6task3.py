from turtle import *


class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

class Point(object):
    """Represents a point in 2-D space"""
R1 = Rectangle()
R1.corner = Point()
R1.width = 100
R1.height = 50
R1.corner.x = 0
R1.corner.y = 0

b = Turtle()

def draw_rect(t,w,h):
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(w)
    t.lt(90)
    t.fd(h)
    
draw_rect(b,100,50)
turtle.mainloop()
canvas.exitonclick()
