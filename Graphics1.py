__author__ = 'adam'

from Tkinter import *

class DinoFrame(Frame):
    def __init__(self, master=None, rows=8, columns=8, size=96, color1='old lace', color2="pale turquoise"):
        #size is the size of a square in pixels

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {} # a dictionary for any pieces on the game board
        self.numbers = {} # a dictionary for the generated numbers

        canv_width = columns * size
        canv_height = rows * size

        Frame.__init__(self, master)

        # Canvas is a widget in Tkinter where you can draw stuff
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canv_width, height=canv_height, background="white")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # binds self.refresh to teh configure event
        self.canvas.bind("<Configure>", self.refresh)

        # initialize widgets
        self.createWidgets()

    # say_hi widget command
    def say_hi(self):
        print "hi there, everyone!"

    # initialize widgets
    def createWidgets(self):

        # quit button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"  # foreground
        self.QUIT["bg"]   = "blue" # background
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        # hi there button
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    # Redraws the board, such as when the window is resized
    def refresh(self, event):
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns): # this part does the actual resizing
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2

        # use this when you start to put characters on the board
        # need to do the same thing with the numbers that we put on the board
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

        # put code here for numbers

def start_app():
    root = Tk() #creates the tk
    root.title("Dinomuncher USA!")
    app = DinoFrame(master=root)
    app.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
    root.destroy()

start_app()