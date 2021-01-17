# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Pierwszy projekt")
# Set geometry (widthxheight)
root.geometry('500x500')
 
# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

icon = PhotoImage(file = '/home/michal/Desktop/gear.png')
 
# Setting icon of master window
root.iconphoto(False, icon)


newLabel = Label(root, text= "Try the button", bg='SlateGray3')
#pady and padx sets position of our newLabel
#newLabel.grid(pady=200, padx=200) 

newLabel.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)

# function to display text when
# button is clicked

def clicked():
    #newLabel.configure(text = "I just got clicked")

    res = "You wrote: " + txt.get()
    newLabel.configure(text = res)

# button widget with red color text
# inside
newButton = Button(root, text = "Click me", fg = "green", command=clicked)
# set Button grid
newButton.grid(column=2, row=0)    

# Execute Tkinter
root.mainloop()