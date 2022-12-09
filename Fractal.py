#imports
import turtle as trtl
#Settings
colorChoice=input("what color?:")
if colorChoice==
#setup
wn=trtl.Screen()
wn.setup(width=1.0, height=1.0)
#trutles



fractalMaker=trtl.Turtle()
  
fractalMaker.speed(0)
wn.tracer(True)  
# turning the turtle to face upwards
fractalMaker.right(-90)
  
# the acute angle between
# the base and branch of the Y
angle = 30
  
# function to plot a Y
def y(size, level):   
  
    if (level > 0):

        trtl.colormode(255)
        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        fractalMaker.pencolor(0, 255//level, 0)
          
        # drawing the base
        fractalMaker.fd(size)
  
        fractalMaker.rt(angle)
  
        # recursive call for
        # the right subtree
        y(0.8 * size, level-1)
          
        fractalMaker.pencolor(0, 255//level, 0)
          
        fractalMaker.left( 2 * angle )
  
        # recursive call for
        # the left subtree
        y(0.8 * size, level-1)
          
        fractalMaker.pencolor(0//level*redColor, 255//level*greenColor, 0//(level*blueColor)

        fractalMaker.right(angle)
        fractalMaker.forward(-size)
           
wn.tracer(False)          
# tree is size 80 and level 7
y(80, 10)

#functions

#events
wn.mainloop()