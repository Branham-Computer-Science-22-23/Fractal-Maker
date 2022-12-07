#imports
import turtle as trtl
#Settings
print("Welcome to the Fractal Maker! \n Here you can make different designs and customize them to your liking.")
#setup
wn=trtl.Screen()
wn.setup(width=1.0, height=1.0)
#trutles

#functions
#ask user for input
ColorChoice = input("What color would you like? ")
NumIterations = input(int("How many iterations would you like? "))
FranctalKind = input("What kind of Fractal? ")

#events
wn.mainloop()