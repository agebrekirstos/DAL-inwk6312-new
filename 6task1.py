import math

class Point(object):
    """Represents a point in 2-D space"""
p1 = Point()
p2 = Point()
#p2 = Point()
p1.x = 0
p1.y = 0
p2.x = 3
p2.y = 4
def distance(p1,p2):
    """calculates the distance between two points"""
    distance = math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)
    return distance
print(distance(p1,p2))
    
        
       
        
        
