from Tkinter import *
from subprocess import Popen

#create root window
root = Tk()

# modify root window with a title
root.title("Servers login GUI")
root.geometry("236x100")

# create a frame in the root window
app = Frame(root)
app.grid()

    
# create some buttons
button = Button(root, text = 'shellserver', width=10)
button.grid(row=0, column=0)

button2 = Button(root, text = 'dnsserver', width=10)
button2.grid(row=1, column=0)

button3 = Button(root, text = 'mainserver', width=10)
button3.grid(row=1, column=1)

# kick off main eventloop
# mainly neccessary for Windows users!
root.mainloop()


