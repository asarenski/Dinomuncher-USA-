__author__ = 'adam'

'''
Dinomuncher USA!
'''

from Tkinter import * # tkinter is a GUI writing module that can also be used to write games
from PIL import Image
import sys

class DinoFrame(Frame):
    def __init__(self, master=None, rows=8, columns=8, size=96, color1='old lace', color2="pale turquoise"):
        # size is the size of a square in pixels

        # initialize variables
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {} # a dictionary for any pieces on the game board
        self.numbers = {} # a dictionary for the generated numbers

        canv_width = columns * size # sets the width of the board default is 8*96
        canv_height = rows * size

        Frame.__init__(self, master) # initializes the frame

        # Canvas is a widget in Tkinter, in which you can draw
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canv_width, height=canv_height, background="white")

        # pack method from Tkinter automatically stakes care of coordinate information
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # binds self.refresh to the configure event
        self.canvas.bind("<Configure>", self.refresh)

        # initialize widgets
        self.createWidgets()

    # function for pushbutton widgets
    def createWidgets(self):

        # quit button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"  # foreground
        self.QUIT["bg"]   = "blue" # background
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        # print coordinates button
        self.hi_there = Button(self)
        self.hi_there["text"] = "Print_Coord",
        self.hi_there["command"] = self.print_coord
        self.hi_there.pack({"side": "left"})

        # function print_coord widget command
    def print_coord(self):
        print self.pieces['player1']

    # function to put the image of the piece on the board
    def piece(self, name, image, row=0, column=0):
    # Also calls placepiece, which puts it in the pieces dictionary.
        self.image = PhotoImage(file=image) # takes the string of the .gif
        self.canvas.create_image(0,0, image = self.image, tags=(name, "piece"), anchor="c") # c for center
        self.placepiece(name, row, column) # calls the placepiece function, which places it in coordinates

    # function to track coordinates for piece in dictionary 'pieces'
    def placepiece(self, name, row, column):
        self.pieces[name] = [row, column] #create a row, column list.. in previous code this was tuple
        # technically x0 should be using column. instead just imagine for the coordinate system
        # that the row just means x_i . This is so that it plays nicely with refresh event for board
        x0 = (row * self.size) + int(self.size/2)
        y0 = (column * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    # function to draw the numbers on the board
    def shownumber(self, act_number, row, column):
        self.numbers[act_number] = [row , column]
        text1 = act_number

        # loop draws the numbers
        for row in range(8):
            for col in range(8):
                x1 = (col * self.size) + int(self.size/2)-3
                y1 = (row * self.size) + int(self.size/2)-3
                self.canvas.create_text(x1,y1, font =("Times", "24", "bold"), text=text1)


    '''
    # function for future use. to resize 'player1' when window resized
    def resize_piece(self):
        # somehow have to capture the original size and compare it to the new sizing event
        scale_w = self.size/old_width
        scale_h = self.size/old_height
        PhotoImage.zoom(scale_w, scale_h)

        old_width = self.size
        old_height = self.size
    '''

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

        # need to do the same thing with the numbers that we put on the board
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
            # places the piece back where it was on the canvas after the redraw

            self.canvas.tag_raise("piece") # tag raise makes "piece" the top layer
            self.canvas.tag_lower("square")

        # redraw the numbers
        for act_number in self.numbers:
            self.shownumber(act_number,0,0)

    #controls
    # these events will move the player 96 pixels by default
    def leftkey(self,event):
        if self.pieces['player1'][0]== 0: # goes into the pieces dictionary and pulls the coord list to check
            print "cannot move past border"
        else:
            self.canvas.move('player1', -1*self.size, 0) # moves the player 1 space over, which is 96 pixels
            self.pieces['player1'][0] = self.pieces['player1'][0]-1 # changes the coordinate system

    def rightkey(self,event):
        if self.pieces['player1'][0]== 7:
            print "cannot move past border"
        else:
            self.canvas.move('player1', self.size, 0)
            self.pieces['player1'][0] = self.pieces['player1'][0]+1

    def upkey(self,event):
        if self.pieces['player1'][1]== 0:
            print "cannot move past border"
        else:
            self.canvas.move('player1', 0, -1*self.size)
            self.pieces['player1'][1] = self.pieces['player1'][1]-1

    def downkey(self,event):
        if self.pieces['player1'][1]== 7:
            print "cannot move past border"
        else:
            self.canvas.move('player1', 0, 1*self.size)
            self.pieces['player1'][1] = self.pieces['player1'][1]+1

    def spacebar(self,event):
        print "best"

# end of DinoFrame

def main():
    root = Tk() #creates the tk
    root.title("Dinomuncher USA!")
    app = DinoFrame(master=root) # initialize the application
    # app.master.maxsize(736,768) # sets the max size of the frame
    app.pack(side="top", fill="both", expand="true", padx=4, pady=4) # pad gives window a little extra room

    # calling the piece method and initializes player1
    player1 = "rex_skull2.gif" # sets the variable to a string
    app.piece("player1",player1,0,0) # calls the piece method arguments are (name, image, row, column)

    #call numbers
    app.shownumber(36,0,0)

    # key bindings
    root.bind('<Escape>', lambda e: root.quit()) # lambda allows you to write user input functions
    root.bind('<Left>',app.leftkey) # these call the keys. one could also write this with %s and a dictionary
    root.bind('<Right>',app.rightkey)
    root.bind('<Up>',app.upkey)
    root.bind('<Down>',app.downkey)
    root.bind('<space>',app.spacebar)

    root.mainloop() # begins the application
    root.destroy()
main()