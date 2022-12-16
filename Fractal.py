#imports
import turtle as trtl
#Settings
redColor=0
greenColor=255
blueColor=0

#setup
wn=trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.tracer(False)
#trutles

fractalMaker=trtl.Turtle()
fractalMaker.speed(0)
  
 
# turning the turtle to face upwards
fractalMaker.setheading(90)
  
# the acute angle between
# the base and branch of the Y
branchAngle = 30
  
# function to plot a tree

def treeDrawer(size, level):   
  
    if (level > 0):

        trtl.colormode(255)
        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        fractalMaker.pencolor(redColor//level, greenColor//level, blueColor//level)
          
        # drawing the base
        fractalMaker.forward(size)
  
        fractalMaker.right(branchAngle)
  
        # recursive call for
        # the right subtree
        treeDrawer(0.8 * size, level-1)
          
        fractalMaker.pencolor(0, 255//level, 0)
          
        fractalMaker.left( 2 * branchAngle )
  
        # recursive call for
        # the left subtree
        treeDrawer(0.8 * size, level-1)
          
        fractalMaker.pencolor(redColor//level, greenColor//level, blueColor//level)

        fractalMaker.right(branchAngle)
        fractalMaker.forward(-size)
      
        
# tree is size 80 and level 5
treeDrawer(80, 5)


#draws spirograph
def spirographDrawer(angle,color1,color2):
    fractalMaker.goto(0,0)
    space = 1
    seg = int(360/angle)
    while fractalMaker.ycor() < 200:
        if fractalMaker.pencolor() == color2:
            fractalMaker.fillcolor(color1)
            fractalMaker.color(color1)
        else:
            fractalMaker.fillcolor(color2)
            fractalMaker.color(color2)
        fractalMaker.right(angle)
        fractalMaker.forward(2 * space + 10) # experiment
        fractalMaker.begin_fill()
        fractalMaker.circle(3)
        fractalMaker.end_fill()
        space = space + 1
    




#functions
treeIterations=5
spiroAngle=180
#adds more branches to tree
def iterateTree():
    global treeIterations
    if treeIterations<11:
        fractalMaker.setheading(90)
        fractalMaker.goto(0,0)
        fractalMaker.clear()
        treeIterations+=1
        treeDrawer(80,treeIterations)
#chenges tree to red
def redTree():
    global redColor, blueColor, greenColor
    fractalMaker.setheading(90)
    redColor=255
    blueColor=0
    greenColor=0
    fractalMaker.goto(0,0)
    fractalMaker.clear()
    treeDrawer(80,treeIterations)
#chenges tree to blue
def blueTree():
    global redColor, blueColor, greenColor
    fractalMaker.setheading(90)
    redColor=0
    blueColor=255
    greenColor=0
    fractalMaker.goto(0,0)
    fractalMaker.clear()
    treeDrawer(80,treeIterations)
#changes tree to green
def greenTree():
    global redColor, blueColor, greenColor
    fractalMaker.setheading(90)
    redColor=0
    blueColor=0
    greenColor=255
    fractalMaker.goto(0,0)
    fractalMaker.clear()
    treeDrawer(80,treeIterations)
#Rotates the spirograph
def iterateSpirograph():
    global spiroAngle
    fractalMaker.setheading(90)
    fractalMaker.goto(0,0)    
    fractalMaker.clear()
    spiroAngle+=-7
    spirographDrawer(spiroAngle,"green","cyan")


#events
trtl.onkeypress(redTree,"r")
trtl.onkeypress(greenTree,"g")
trtl.onkeypress(blueTree,"b")
trtl.onkeypress(iterateSpirograph,"s")
trtl.onkeypress(iterateTree,"t")
trtl.listen()

wn.mainloop()
