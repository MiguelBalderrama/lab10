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
drawpad = Canvas(root, background='white')
drawpad.grid(row=0, column=1)
# create_oval(x,y,width,height,fill color)
#create_square(top left x,top left y, bottom right x, bottom right y, fill color)
square = drawpad.create_rectangle(120,90,130,50, fill='red')
square = drawpad.create_rectangle(50,200,150,100, fill='red')
square = drawpad.create_rectangle(110,110,140,140, fill='white')
square = drawpad.create_rectangle(60,110,90,140, fill='white')
square = drawpad.create_rectangle(80,160,110,200, fill='white')
oval = drawpad.create_oval(100, 170, 105, 180, fill='blue')
square = drawpad.create_rectangle(40,200,180,220, fill='green')
#create_line(top left x,top left y, bottom right x, bottom right y, fill color)
line = drawpad.create_line(150, 100, 100, 50)
line = drawpad.create_line(50, 100, 100, 50)

root.mainloop()