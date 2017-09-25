class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

class Point(object):
    """Represents a point in 2-D space"""
R1 = Rectangle()
R1.corner = Point()
R1.width = 3
R1.height = 4
R1.corner.x = 0
R1.corner.y = 0

def find_center(R1):
    """rturns the coordinates of the center point of recangle"""
    pt = Point()
    pt.x = R1.corner.x + R1.width/2.0
    pt.y = R1.corner.y + R1.height/2.0
    return pt

def print_pt(pxy):
    """prints in (x,y) notation"""
    print('(%g, %g)' % (pxy.x, pxy.y))

def move_rectangle(R1,dx,dy):
    """moves the corner of the rectangle by dx and dy amounts"""
    p = Point()
    R1.corner.x+=dx
    R1.corner.y+=dy
    p.x = R1.corner.x
    p.y = R1.corner.y
    return p
    
#print_pt(find_center(R1))
print_pt(move_rectangle(R1,5,6))

