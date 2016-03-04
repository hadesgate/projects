from Tkinter import *
from subprocess import Popen

#create root window
root = Tk()

# modify root window with a title
root.title("Servers login GUI")
root.geometry("236x100")

# create a frame in the root window
app = Frame(root)
app.grid(row=0)
bapp = Frame(root)
bapp.grid(row=1)
    
# create some buttons
button = Button(bapp, text = 'shellserver', width=12)
button.grid(row=0, column=0, sticky=W)

button2 = Button(bapp, text = 'dnsserver', width=12)
button2.grid(row=1, column=0, sticky=W)

button3 = Button(bapp, text = 'mainserver', width=12)
button3.grid(row=1, column=1, sticky=W)

# create entries with labels

entry1 = Entry(app)
entry2 = Entry(app)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

elabel = Label(app, text='Name:')
elabel2 = Label(app, text='Password:')
elabel.grid(row=0, column = 0, sticky=E)
elabel2.grid(row=1, column = 0)




# kick off main eventloop
# mainly neccessary for Windows users!
root.mainloop()


