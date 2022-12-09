#imports
import turtle as trtl
#Settings
redColor=0
greenColor=0
blueColor=0
colorChoice=input("what color? (Red, Green or Blue):")
fractalChoice=input("What type of fractal would you like? (Tree, Spirograph,...")
if colorChoice=="red":
    redColor=255
elif colorChoice=="green":
    greenColor=255
else:
    blueColor=255
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
        fractalMaker.pencolor(redColor//level, greenColor//level, blueColor//level)
          
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
          
        fractalMaker.pencolor(redColor//level, greenColor//level, blueColor//level)

        fractalMaker.right(angle)
        fractalMaker.forward(-size)





#THE SNOWFLAKE

# Python code to draw snowflakes fractal.
import random
 
# setup the window with a background color
wn = turtle.Screen()
wn.bgcolor("cyan")
 
# assign a name to your turtle
elsa = turtle.Turtle()
elsa.speed(15)
 
# create a list of colours
sfcolor = ["white", "blue", "purple", "grey", "magenta"]
 
# create a function to create different size snowflakes
def snowflake(size):
 
    # move the pen into starting position
    elsa.penup()
    elsa.forward(10*size)
    elsa.left(45)
    elsa.pendown()
    elsa.color(random.choice(sfcolor))
 
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)  
        elsa.left(45)
     
 
# create one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            elsa.forward(10.0*size/3)
            elsa.backward(10.0*size/3)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(10.0*size/3)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(10.0*size)
 
# loop to create 20 different sized snowflakes
# with different starting co-ordinates
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(1, 4)
    elsa.penup()
    elsa.goto(x, y)
    elsa.pendown()
    snowflake(sf_size)
 
           
wn.tracer(False)          
# tree is size 80 and level 7
y(80, 10)



#THE SPIROGRAPH

color1 = "orange"
color2 = "purple"

wn = trtl.Screen()
width = 400
height = 300

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

answer = "y"
while (answer == "y"):
  wn.clearscreen()  
  painter.goto(0,0)
  space = 1

  angle = int(input("angle:"))
  seg = int(360/angle)
  while painter.ycor() < height:
    if painter.pencolor() == color2:
        painter.fillcolor(color1)
        painter.color(color1)
    else:
        painter.fillcolor(color2)
        painter.color(color2)
    painter.right(angle)
    painter.forward(2 * space + 10) # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space = space + 1
  answer = input("again?")





#functions

#events
wn.mainloop()
