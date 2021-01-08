'''
My Turtle Interface 
'''
 
from tkinter import *
import turtlefigures
import turtle
 
#--------------------- make the 3 frame ie. main frame, canvas and control panel -------------------------

 
# make the root frame and give its geometry
root = Tk()
root.title("Turtle Figures")
root.geometry("900x750+100+100")
bgImage = PhotoImage (file = r"wave2.gif")
Label(root, image = bgImage).place(relwidth = 1, relheight = 1)


# make control frame
controlFrame = LabelFrame(root, pady=35, padx=35, bg="#9AD7D6")
controlFrame.pack(fill=BOTH)

# make the canvas
canvasFrame = LabelFrame(root, text = "TURTLE WILL DRAW YOUR SHAPE HERE")
canvasFrame.pack()
canvas = Canvas(canvasFrame, width = 600, height = 500, bg = "#9AD7D6")
canvas.pack()
 


 
# ---------------  functions to control the interface ---------


     #create info command

def onInfoF():
    myLabel = Label(controlFrame, text="Great Choice! You have chosen a "+figureStr.get(), bg="#1E9894")
    myLabel.grid(row=4, column=2)
    
#end InfoF

 
def onDrawF():
     # order and length type is an integer
     order = int(orderStr.get())
     length = int(lengthStr.get())
 
     # find the selected figure from the option menu
     turtleIndex = figureList.index(figureStr.get())
     
     if turtleIndex == 1:
     # draw binary tree
          turtlefigures.tree(order, length, pen)
 
 
     elif turtleIndex == 2:
     #draw quad tree
          turtlefigures.tree4(order, length, pen)


     elif turtleIndex == 3:
     #draw fern
        turtlefigures.fern(order, length, pen)

     elif turtleIndex == 4:
     #draw serpinsky gasket
        turtlefigures.s(order, length, pen)

     elif turtleIndex == 5:
     #draw koch snowflake
        turtlefigures.kochsnow(order, length, pen)

     elif turtleIndex == 6:
     #draw anti snowflake
        turtlefigures.anti(order, length, pen)

     elif turtleIndex == 7:
     #draw square gasket
        turtlefigures.gasket(order, length, pen)

     elif turtleIndex == 8:
     #draw circle 
        turtlefigures.circle(order, length, pen)

     elif turtleIndex == 9:
     #draw peoni
        turtlefigures.peoni(order, length, pen)

     elif turtleIndex == 10:
     #draw sunflower 
        turtlefigures.sunflower(order, length, pen)
 
# end DrawF
 
def onClearF():
     # define how clear events are handled
     orderStr.set("")
     lengthStr.set("")

 

     # clear the screen
     canvas.delete("all")
     global pen
     pen.up()
     pen = turtle.RawTurtle(canvas)
     pen.showturtle()
     pen.width(3)
     pen.speed(0)
     pen.up(); pen.setx(-200); pen.down()
     pen.shape("turtle")
     pen.color("#037587")

# end ClearF

 
 
 
# ---------------- make the interface ---------------

 
# top title
title = Label(root, text = "TURTLE GENERATOR", width=20, bg = "#1E9894", fg = "#FDFAF7")
title.pack()
title.config(font=("Courier", 25))
title.place(relx=0.5, rely=0.027, anchor=CENTER)


#list of turtle figures
figureList = ["                          Please choose:                          ",
              "  Binary Tree ",
              " Quadratic tree ",
              " Fern Tree",
              " Serpinsky Gasket",
              " Koch's Snowflake",
              " Anti-Snowflake",
              " Square Gasket ",
              " Circle",
              " Peoni",
              " Sunflower"]

figureStr = StringVar()
figureStr.set(figureList[0])
figureOptionMenu = OptionMenu(controlFrame, figureStr, *figureList)
figureOptionMenu.grid(row=2, column=2)




# order label and entry
orderLabel = Label(controlFrame, text=" ORDER: ", width=10, bg="#1E9894", activebackground="#ffffff")
orderLabel.grid(row = 2, column = 5)

orderStr = StringVar()
orderEntry = Entry(controlFrame, textvariable = orderStr, width=25)
orderEntry.grid(row = 2, column = 6)
orderEntry.insert(0, "Please enter:              ")

#length label and entry
lengthLabel = Label(controlFrame, text="LENGTH:", width=10, bg="#1E9894", activebackground="#ffffff")
lengthLabel.grid(row = 3, column = 5)

lengthStr = StringVar()
lengthEntry = Entry(controlFrame, textvariable = lengthStr, width=25)
lengthEntry.grid(row = 3, column = 6)
lengthEntry.insert(0, "Please enter:              ")


#creating draw, clear and info panel buttons

drawButton = Button(controlFrame, text="DRAW ", width=15, padx=15, pady=5, activebackground="#5bd4d0", command=onDrawF)
drawButton.grid(row = 2, column = 8)

clearButton = Button(controlFrame, text="CLEAR", width=15, padx=15, pady=5, activebackground="#5bd4d0", command=onClearF)
clearButton.grid(row = 3, column = 8)

infoButton = Button(controlFrame, text="Information Panel", padx=100, pady=2, activebackground="#5bd4d0", command=onInfoF)
infoButton.grid(row=3, column=2)

 
# --------------------- control the pen ------------------------------

pen = turtle.RawTurtle(canvas)
pen.color("#037587")
pen.shape("turtle")
pen.speed(0)
pen.width(3)
pen.up(); pen.setx(-200); pen.down()

 
 
 
 
