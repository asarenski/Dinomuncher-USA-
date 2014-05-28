from Tkinter import *

'''
master = Tk()

var = StringVar(master)
var.set("one") # initial value

option = OptionMenu(master, var, "one", "two", "three", "four")
option.pack()

#
# test stuff

def ok():
    print "value is", var.get()
    master.quit()

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()
'''

'''
_____________________________________________________-
'''

root = Tk()

def hello():
    print "hello!"

# create a toplevel menu
menubar = Menu(root)
menubar.add_command(label="Hello!", command=hello)
menubar.add_command(label="Quit!", command=root.quit)

# display the menu
root.config(menu=menubar)