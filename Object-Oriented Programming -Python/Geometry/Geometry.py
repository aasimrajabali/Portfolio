#  File: Geometry.py

#  Description: This program defines Point, Line, and Circle classes, and uses functions of those classes to determine geometric tests.

#  Student Name: Aasim Rajabali

#  Student UT EID: afr447

#  Partner Name: Shawn Hu

#  Partner UT EID: sh42578

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: February 14, 2015

#  Date Last Modified: February 15, 2015

import math

class Point (object):
    
    # constructor with default values
    def __init__ (self, x = 0, y = 0):
      self.x = x
      self.y = y
      
    # get distance to another Point object
    def dist (self, other):
      return math.hypot(self.x - other.x, self.y - other.y)

    # create a string representation of a Point (x, y)
    def __str__ (self):
      return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # test for equality between two points
    def __eq__ (self, other):
      tol= 1.0e-18
      return (abs(self.x - other.x) < tol and abs(self.y - other.y) < tol)

class Line (object):

    # constructor assign default values if user defined points are the same
    def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
      tol= 1.0e-18
      if (abs(p1_x - p2_x) < tol and abs(p1_y - p2_y) < tol):
          self.p1 = Point(0,0)
          self.p2 = Point(1,1)
      else:
          self.p1 = Point(p1_x, p1_y)
          self.p2 = Point(p2_x, p2_y)
          
    # determine if line is parallel to x axis
    def is_parallel_x (self):
      tol= 1.0e-18
      return (abs(self.p1.y-self.p2.y) < tol)

    # determine if line is parallel to y axis
    def is_parallel_y (self):
      tol= 1.0e-18
      return (abs(self.p1.x-self.p2.x) < tol)

    # determine slope for the line
    # return float ('inf') if line is parallel to the y-axis
    def slope (self):
      tol= 1.0e-18
      if (abs(self.p1.x - self.p2.x) < tol):
          return float('inf')
      else:
          return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
        
    # determine the y-intercept of the line
    def y_intercept (self):
      return (self.p1.y - (self.slope() * self.p1.x))

    # determine the x-intercept of the line
    def x_intercept (self):
      return (-1.0 * self.y_intercept()) / (self.slope())

    # determine if two lines are parallel
    def is_parallel (self, other):
      tol= 1.0e-18
      return (abs(self.slope() - other.slope()) < tol)

    # determine if two lines are perpendicular to each other
    def is_perpendicular (self, other):
      tol= 1.0e-18
      return self.slope() * other.slope() == -1

    # determine if a point is on the line or on an extension of it
    def is_on_line (self, p):
      tol= 1.0e-18
      return ((p.y - (self.slope() * p.x) - p.y_intercept()) < tol)

    # determine the perpendicular distance of a point to the line
    def perp_dist (self, p):
      if self.is_parallel_y:
          return abs(self.p1.x - p.x)
      if self.is_parallel_x:
          return abs(self.p1.y - p.y)
      perpline = Line(p.x, p.y, p.x + 1, p.y + self.slope)
      return p.dist(p, intersection_point(self, perpline))

    # determine the intersection point of two lines if not parallel
    def intersection_point (self, other):
      intx = (other.slope() - self.slope()) / self.y_intercept() - other.y_intercept()
      return Point(intx, self.slope() * intx + self.y_intercept())
    
    # determine if two points are on the same side of the line
    # return False if one or both points are on the line
    def on_same_side (self, p1, p2):
        if self.is_parallel_y:
            #checking for the equality of a boolean statement is really just saying "if not xor", which is what we want
            if (p1.x < self.p1.x) == (p2.x < self.p2.x):
                return True
        if self.is_parallel_x:
            if (p1.y < self.p1.y) == (p2.y < self.p2.y):
                return True
        if (p1.y > self.slope() * p1.x + self.y_intercept()) == (p2.y > self.slope() * p2.x + self.y_intercept()):
                return True
        return False        

    # string representation of the line - one of three cases
    # y = c
    # x = c
    # y = m * x + b
    def __str__ (self):
        if self.is_parallel_y():
            return ('x = ' + str(self.p1.x))
        if self.is_parallel_x():
            return ('y = ' + str(self.p1.y))
        return ('y = ' + str(self.slope()) + ' * x '+ str(self.y_intercept()))

class Circle (object):
    # constructor with default values
    def __init__ (self, radius = 1, x = 0, y = 0):
        tol = 1.0e-18
        if radius > tol:
            self.radius = radius
            self.center = Point(x, y)
        else:
            self.radius = 1
            self.center = Point(0, 0)
            
    # compute circumference
    def circumference (self):
        return self.radius * 2 * math.pi
    
    # compute area
    def area (self):
        return (self.radius) ** 2 * math.pi
    
    # determine if a point is inside the circle
    def is_inside_point (self, p):
        return (self.radius > p.dist(p, Circle.center))
    
    # determine if the other circle is strictly inside self
    def is_inside_circle (self, other):
        return (other.radius + other.center.dist(other.center) < self.radius)
    
    # determine if the other circle intersects self
    def does_intersect_circle (self, other):
        a = (other.radius + other.center.dist(other.center) < self.radius)
        b = (other.radius - other.center.dist(other.center) < self.radius)
        return (a and b)
        
    # determine if the line intersects circle
    def does_intersect_line (self, line):
        return (Line.perp_dist(line,self.center) < self.radius)

    # determine if the line is tangent to the circle
    def is_tangent (self, line):
        tol = 1.0e-16
        return (abs(Line.perp_dist(line, self.center) - self.radius) < tol)

    # string representation of a circle
    # Radius: radius, Center: (x, y)
    def __str__ (self):
        return ('Radius: ' + str(self.radius) + ', Center: (' + str(self.center.x) + ', ' + str(self.center.y) + ')')

def main():
  # open file "geometry.txt" for reading
  infile= open("geometry.txt", 'r')

  # read the coordinates of the first Point P
  p1= infile.readline()
  p1= p1.strip()
  p1_x= float(p1[0:2])
  p1_y= float(p1[5:6])
  p1= Point(p1_x,p1_y)
  print('Coordinates of P:',p1)
  
  # read the coordinates of the second Point Q
  q2= infile.readline()
  q2= q2.strip()
  q2_x= float(q2[0:1])
  q2_y= float(q2[4:6])
  q2= Point(q2_x,q2_y)
  print('Coordinates of Q:',q2)
    
  # print distance between P and Q
  distance= p1.dist(q2)
  print('Distance between P and Q:', distance)
  
  # print the slope of the line PQ
  line1= Line(p1_x, p1_y, q2_x, q2_y)
  slope= line1.slope()
  print('Slope of PQ:', slope)
  
  # print the y-intercept of the line PQ
  y_int= line1.y_intercept()
  print('Y-Intercept of PQ:', y_int)
  
  # print the x-intercept of the line PQ
  x_int= line1.x_intercept()
  print('X-Intercept of PQ:', x_int)
  
  # read the coordinates of the third Point A
  a3= infile.readline()
  a3= a3.strip()
  a3_x= float(a3[0:1])
  a3_y= float(a3[4:5])  
  a3= Point(a3_x,a3_y)
  
  # read the coordinates of the fourth Point B
  b4= infile.readline()
  b4= b4.strip()
  b4_x= float(b4[0:2])
  b4_y= float(b4[5:7])
  b4= Point(b4_x,b4_y)

  # print the string representation of the line AB
  line2= Line(a3_x, a3_y, b4_x, b4_y)
  slope2= line2.slope()
  y_int2= line2.y_intercept()
  print('Line AB:' + line2.__str__())
  

  # print if the lines PQ and AB are parallel or not
  parallel_lines= Line.is_parallel(line1,line2)
  if parallel_lines:
      print('PQ is parallel to AB')
  else:
      print('PQ is not parallel to AB')
      
  # print if the lines PQ and AB (or extensions) are perpendicular or not
  perp_lines= Line.is_perpendicular(line1,line2)
  if perp_lines:
      print('PQ is perpendicular to AB')
  else:
      print('PQ is not perpendicular to AB')
      
  # print coordinates of the intersection point of PQ and AB if not parallel
  if parallel_lines==False:
      int_pt= Line.intersection_point(line1,line2)
      print('Intersection point of PQ and AB:', int_pt)

  # read the coordinates of the fifth Point G
  g5= infile.readline()
  g5= g5.strip()
  g5_x= float(g5[0:1])
  g5_y= float(g5[4:5])
  g5= Point(g5_x,g5_y)
  
  # read the coordinates of the sixth Point H
  h6= infile.readline()
  h6= h6.strip()
  h6_x= float(h6[0:2])
  h6_y= float(h6[5:7])
  h6= Point(h6_x,h6_y)
  
  # print if the the points G and H are on the same side of PQ
  same_side1= line1.on_same_side(g5,h6)
  if same_side1:
      print('G and H are on the same side of PQ')
  else:
      print('G and H are not on the same side of PQ')
      
  # print if the the points G and H are on the same side of AB
  same_side2= line2.on_same_side(g5,h6)
  if same_side2:
      print('G and H are on the same side of AB')
  else:
      print('G and H are not on the same side of AB')
      
  # read the radius of the circleA and the coordinates of its center
  circ1= infile.readline()
  circ1= circ1.strip()
  circ1_rad= float(circ1[0:1])
  circ1_x= float(circ1[4:5])
  circ1_y= float(circ1[8:9])
  circleA= Circle(circ1_rad,circ1_x,circ1_y)
  # print the string representation of circleA and circleB
  print('CircleA:', circleA)
  
  # read the radius of the circleB and the coordinates of its center
  cir2= infile.readline()
  cir2= cir2.strip()
  cir2_rad= float(cir2[0:4])
  cir2_x= float(cir2[4:8])
  cir2_y= float(cir2[8:12])
  circleB= Circle(cir2_rad,cir2_x,cir2_y)
  # print the string representation of circleA and circleB
  print('CircleB:', circleB)
  
  # determine if circleB is inside circleA
  inside_a= Circle.is_inside_circle(circleA,circleB)
  if inside_a:
      print('circleB is inside circleA')
  else:
      print('circleB is not inside circleA')
      
  # determine if circleA intersects circleB
  intersect= Circle.does_intersect_circle(circleA,circleB)
  if intersect:
      print('circleA does intersect circleB')
  else:
      print('circleA does not intersect circleB')
      
  # determine if line PQ (or extension) intersects circleA
  line_int= Circle.does_intersect_line(circleA,line1)
  if line_int:
      print('PQ does intersect circleA')
  else:
      print('PQ does not intersect circleA')
      
  # determine if line AB (or extension) is tangent to circleB
  line_tan= Circle.is_tangent(circleB, line2)
  if line_tan:
      print('AB is a tangent to circleB')
  else:
      print('AB is not a tangent to circleB')

  # close file "geometry.txt"
  infile.close()
  
main()
