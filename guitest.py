from Tkinter import *

#create root window
root = Tk()

# modify root window
root.title("guis test")
root.geometry("200x100")

# create a frame in the root window
app = Frame(root)
app.grid()

# create some buttons
button = Button(app text = "shellserver1")
button.grid()

# kick off main eventloop

root.mainloop()


