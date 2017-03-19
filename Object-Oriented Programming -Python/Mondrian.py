#  File: Mondrian.py

#  Description: This program recursively paints Mondrian Lines in the form of abstract art.

#  Student Name: Aasim Rajabali

#  Student UT EID: afr447   

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: March 7, 2015

#  Date Last Modified: March 7, 2015

import turtle,random

def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

def drawrectangle(ttl, x, y, width, height):
    color_list= ['blue','red','yellow','grey']
    ttl.fillcolor(color_list[random.randint(0,3)])
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.begin_fill()
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(height)
    ttl.right(90)
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(height)
    ttl.right(90)
    ttl.end_fill()
    

#draws a horizontal line from one side of the canvas to the other    
def drawLineX(ttl,rec_lvl):
    if rec_lvl == 0:
        return
    
    x_ran= random.randint(-400,400)
    y_ran= random.randint(-400,400)
    ttl.pensize(random.randint(3,10))
    drawLine(ttl,-400,y_ran,400,y_ran)
    ttl.goto(x_ran,y_ran)
    
    return drawLineY(ttl,rec_lvl-1,x_ran,y_ran)

#draws a vertical line recursively from one side of the canvas to the other
def drawLineY(ttl,rec_lvl,x_ran,y_ran):
    if rec_lvl == 0:
        return
    ttl.pensize(random.randint(3,10))
    if y_ran > 0:
        drawLine(ttl,x_ran,y_ran,x_ran,-400)
        y_ran2= random.randint(-400,y_ran)
    else:
        drawLine(ttl,x_ran,y_ran,x_ran,400)
        y_ran2= random.randint(y_ran,400)
    ttl.goto(x_ran,y_ran2)
    
    #draw random rectangles to go with each recursive line
    while rec_lvl < 6:
        ttl.goto(x_ran, y_ran2)
        drawrectangle(ttl,x_ran,y_ran2,random.randint(200,400),random.randint(0,200))
        return drawLineRec(ttl,rec_lvl-1,x_ran,y_ran2)
        
    
    return drawLineRec(ttl,rec_lvl-1,x_ran,y_ran2)
       

#draws a horizontal line recursively from one side of the canvas to the other
def drawLineRec(ttl,rec_lvl,x_ran,y_ran2):
    if rec_lvl == 0:
        return
    ttl.pensize(random.randint(3,10))
    if x_ran > 0:
        drawLine(ttl,x_ran,y_ran2,-400,y_ran2)
        x_ran2= random.randint(-400,x_ran)
    else:
        drawLine(ttl,x_ran,y_ran2,400,y_ran2)
        x_ran2= random.randint(x_ran,400)
    ttl.goto(x_ran2,y_ran2)
    
    #draw the random rectangles to go with each recursive line
    while rec_lvl < 6:
        ttl.goto(x_ran2, y_ran2)
        drawrectangle(ttl,x_ran2,y_ran2,random.randint(0,200),random.randint(200,400))
        return drawLineY(ttl,rec_lvl-1,x_ran2,y_ran2)
    
    return drawLineY(ttl,rec_lvl-1,x_ran2,y_ran2)

  
def main():
    print('Mondrian Composition')
    print()
    #prompt user to enter recursion level
    rec_lvl= eval(input('Enter a level of recursion between 1 and 6: '))
    if rec_lvl < 0 or rec_lvl > 6:
        return

    #put label at the top of the page
    turtle.title('Mondrian Lines')
    #setup screen size
    turtle.setup(800,800,0,0)
    
    #create turtle object
    ttl=turtle.Turtle()
    ttl.speed(3)
    drawLineX(ttl,rec_lvl)
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file = "Mondrian.eps")
    
    #persist drawing
    turtle.done()
               
main()
    
