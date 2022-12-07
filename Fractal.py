#imports
import turtle as trtl
#Settings

#setup
wn=trtl.Screen()
wn.setup(width=1.0, height=1.0)
#trutles

fractalMaker=trtl.Turtle()
  
  
fractalMaker.speed(0)
  
# turning the turtle to face upwards
fractalMaker.rt(-90)
  
# the acute angle between
# the base and branch of the Y
angle = 30
  
# function to plot a Y
def y(sz, level):   
  
    if level > 0:

        trtl.colormode(255)
        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        fractalMaker.pencolor(0, 255//level, 0)
          
        # drawing the base
        fractalMaker.fd(sz)
  
        fractalMaker.rt(angle)
  
        # recursive call for
        # the right subtree
        y(0.8 * sz, level-1)
          
        fractalMaker.pencolor(0, 255//level, 0)
          
        fractalMaker.lt( 2 * angle )
  
        # recursive call for
        # the left subtree
        y(0.8 * sz, level-1)
          
        fractalMaker.pencolor(0, 255//level, 0)
          
        fractalMaker.rt(angle)
        fractalMaker.fd(-sz)
           
          
# tree of size 80 and level 7
y(80, 7)

#functions

#events
wn.mainloop()