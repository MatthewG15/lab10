##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#house base
rectangle = drawpad.create_rectangle(100,600,700,200)

#roof
roof1 = drawpad.create_line(400,50,0,250)
roof2 = drawpad.create_line(400,50,800,250)

#windows
window1 = drawpad.create_rectangle(150,500,250,425)
window2 = drawpad.create_rectangle(150,350,250,275)
window3 = drawpad.create_rectangle(550,350,650,275)
window4 = drawpad.create_rectangle(550,500,650,425)

#door
door = drawpad.create_rectangle(300,600,400,400)

#door handle
handle = drawpad.create_oval(310,510,320,525)

#chimney
chimney1 = drawpad.create_line(500,100,500,50)
chimney2 = drawpad.create_line(500,50,550,50)
chimney3 = drawpad.create_line(550,50,550,125)

root.mainloop()
