__author__ = 'adam'
'''making a new'''
'''
Dinomuncher USA!
'''

from Tkinter import * # tkinter is a GUI writing module that can also be used to write games
from MathFile import math_main


class Select_Menu(Frame):
    def __init__(self, master, text, height, width, *args, **kwargs):
        self.height = height
        self.width = width

        Frame.__init__(self, *args, borderwidth=20, **kwargs)
        self.height = height
        self.width = width
        button1 = Button(self, text="Multiples", font=('Comic Sans MS', 20),command=lambda: self.callback1())
        button1.pack(side="top", pady = 20)

        button2 = Button(self, text="Multiplication", font=('Comic Sans MS', 20),command=lambda: self.callback2())
        button2.pack(side="top", pady = 20)

        button3 = Button(self, text="Division", font=('Comic Sans MS', 20),command=lambda: self.callback3())
        button3.pack(side="top", pady = 20)

        button4 = Button(self, text="Addition", font=('Comic Sans MS', 20),command=lambda: self.callback4())
        button4.pack(side="top", pady = 20)

        button5 = Button(self, text="Subtraction", font=('Comic Sans MS', 20),command=lambda: self.callback5())
        button5.pack(side="top", pady = 20)


class DinoFrame(Frame):
    def __init__(self, master=None, rows=5, columns=6, size=96, color1='old lace', color2="pale turquoise"):
        # size is the size of a square in pixels

        # initialize variables
        # initially used for self.refresh, which is the checker board
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2

        self.pieces = {} # a dictionary for any pieces on the game board

        # variables used intially by the callbacks and drawing the numbers
        self.number_marker = [] # number marker for right or wrong answer
        self.drawn_number = [] # number list used to draw
        self.op_number = 0 # the comparative number
        self.op_type = '' # the type of comparison operation

        self.v = StringVar() # string variable for label for operation
        self.v1 = StringVar() # string variable used for the score tracker
        self.point_track = 0 # int variable used to track points
        self.life_track = 3 # number of lives at the start

        canv_width = columns * size # sets the width of the board default 6*96
        canv_height = rows * size

        Frame.__init__(self, master) # initializes the frame

        # setting all the buttons for the select menu
        select1 = Select_Menu(self, '', height=100, width=300)
        # setting the button commands to the functions below
        select1.callback1 = self.callback1
        select1.callback2 = self.callback2
        select1.callback3 = self.callback3
        select1.callback4 = self.callback4
        select1.callback5 = self.callback5
        select1.place(x=0, y=50, relwidth=1, relheight=1)
        select1.lift # sets the select menu as the top layer on Frame

        # Canvas is a widget in Tkinter, in which you can draw
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canv_width, height=canv_height, background="white")

        # creates the label first so it is at the top
        label1 = Label(master,justify="c", textvariable=self.v,
                       font=("TkHeadingFont", "16"), pady=10).pack({"side": "top"})
        self.v.set("Select an Operation")

        label2 = Label(master, justify='c', textvariable=self.v1).pack({'side':'top'})
        self.v1.set('Score: 0')

        # pack method from Tkinter automatically stakes care of coordinate information
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # binds self.refresh to the configure event
        self.canvas.bind("<Configure>", self.refresh)

        # initialize widgets
        self.createWidgets()

        # initialize the life counter
        self.rex_lives()

    # Definitions for the operation selection (callback functions)
    # these unpack the num_dict and turn it into useful lists
    def callback1(self):
        self.op_type = "Multiples"
        self.lift()
        math_dict = math_main(self.op_type) # pulls num_dict from math_main and sets as math_dict

        # unpacks the num_dict into xtuple
        # xtuple is then used to create the drawn_number list and the number_marker_list
        # the third value of xtuple is taken as a True or False for solving the operation requirement
        for i in range (30):
            xtuple = ()
            xtuple = math_dict[i]
            self.drawn_number.append(xtuple[0])
            self.number_marker.append(xtuple[3])
        self.op_number = xtuple[2]
        self.shownumber(self.drawn_number) # inputs num_list to show numbers on board
        self.v.set(self.op_type + " of " + str(self.op_number))

    def callback2(self):
        self.op_type = "Multiplication"
        self.lift()
        math_dict = math_main(self.op_type) # pulls num_dict from math_main and sets as math_dict
        for i in range (30):
            xtuple = ()
            xtuple = math_dict[i]
            self.drawn_number.append(str(xtuple[0])+'x'+str(xtuple[1]))
            self.number_marker.append(xtuple[3])
        self.op_number = xtuple[2]
        self.shownumber(self.drawn_number)
        self.v.set("Equals " + str(self.op_number))

    def callback3(self):
        self.op_type = "Division"
        self.lift()
        math_dict = math_main(self.op_type) # pulls num_dict from math_main and sets as math_dict
        for i in range (30):
            xtuple = ()
            xtuple = math_dict[i]
            self.drawn_number.append(str(xtuple[0])+'/'+str(xtuple[1]))
            self.number_marker.append(xtuple[3])
        self.op_number = xtuple[2]
        self.shownumber(self.drawn_number)
        self.v.set("Equals " + str(self.op_number))

    def callback4(self):
        self.op_type = "Addition"
        self.lift()
        math_dict = math_main(self.op_type) # pulls num_dict from math_main and sets as math_dict
        for i in range (30):
            xtuple = ()
            xtuple = math_dict[i]
            self.drawn_number.append(str(xtuple[0])+'+'+str(xtuple[1]))
            self.number_marker.append(xtuple[3])
        self.op_number = xtuple[2]
        self.shownumber(self.drawn_number)
        self.v.set("Equals " + str(self.op_number))

    def callback5(self):
        self.op_type = "Subtraction"
        self.lift()
        math_dict = math_main(self.op_type) # pulls num_dict from math_main and sets as math_dict
        for i in range (30):
            xtuple = ()
            xtuple = math_dict[i]
            self.drawn_number.append(str(xtuple[0])+'-'+str(xtuple[1]))
            self.number_marker.append(xtuple[3])
        self.op_number = xtuple[2]
        self.shownumber(self.drawn_number)
        self.v.set("Equals " + str(self.op_number))

    # function for pushbutton widgets
    def createWidgets(self):

        # quit button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"  # foreground
        self.QUIT["bg"]   = "blue" # background
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        # print numbers button
        self.hi_there = Button(self)
        self.hi_there["text"] = "Print_Numbers",
        self.hi_there["command"] = self.print_numbers
        self.hi_there.pack({"side": "left"})

    def rex_lives(self):
        #lives label
        self.LIVES = Label(self)
        if self.life_track == 3:
            imgstr = "rex_lives3.gif"
        elif self.life_track == 2:
            imgstr = "rex_lives2.gif"
        elif self.life_track == 1:
            imgstr = "rex_lives1.gif"
        elif self.life_track <= 0:
            imgstr = "rex_lives0.gif"
            self.v1.set("Game Over , Your Score:" + str(self.point_track))
        self.lives_image = PhotoImage(file=imgstr)
        self.LIVES['image'] = self.lives_image
        self.LIVES.pack({'side':'right'})

        # function print_coord widget command
    def print_numbers(self):
        print self.drawn_number
        print self.number_marker

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
    def shownumber(self, drawn_number):
        self.drawn_number = drawn_number
        counter = -1
        self.canvas.delete("the_text")

        # loop draws the drawn numbers
        for row in range(self.rows):
            for col in range(self.columns):
                counter += 1
                x1 = (col * self.size) + int(self.size/2)-0
                y1 = (row * self.size) + int(self.size/2)-0
                text1 = drawn_number[counter]
                self.canvas.create_text(x1,y1, font =("Times", "24", "bold"), text=text1, tags="the_text")

    # draws the board
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

    #controls
    # these events will move the player 96 pixels by default
    def leftkey(self,event):
        if self.pieces['player1'][0]== 0: # goes into the pieces dictionary and pulls the coord list to check
            print "cannot move past border"
        else:
            self.canvas.move('player1', -1*self.size, 0) # moves the player 1 space over, which is 96 pixels
            self.pieces['player1'][0] = self.pieces['player1'][0]-1 # changes the coordinate system

    def rightkey(self,event): # remember self.columns was set at __init__
        if self.pieces['player1'][0]== self.columns-1:
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

    def downkey(self,event): #remember self.rows was set at __init__
        if self.pieces['player1'][1]== self.rows-1:
            print "cannot move past border"
        else:
            self.canvas.move('player1', 0, 1*self.size)
            self.pieces['player1'][1] = self.pieces['player1'][1]+1

    def spacebar(self,event):
        x0 = self.pieces['player1'][0] # x var of coords
        y0 = self.pieces['player1'][1] # y var of coords

        numbers_entry = x0 + y0*self.columns # this is the translation to 0:29 for numbers dictionary
        print "space hit"

        # a reminder that numbers_entry is 0:29 (space location on board)
        # drawn_numbers is the list of the numbers that are being drawn on the board
        if self.drawn_number[numbers_entry] == '': # the the drawn_number at that point is blank
            # do nothing
            print "no entry"
        elif self.number_marker[numbers_entry] == 1:
            if self.life_track <= 0:
                pass
            else:
                self.point_track += 10
                self.v1.set("Score: " +str(self.point_track))
                print "congrats" + "you now have " + str(self.point_track) + " points"
                self.drawn_number[numbers_entry] = '' # turns the entry into a blank string
                self.number_marker[numbers_entry] = 0
        else:
            print "wrong"
            self.drawn_number[numbers_entry] = '' # turns the entry into a blank string
            self.number_marker[numbers_entry] = 0
            self.life_track -= 1 # subtract a life from the life counter
            self.LIVES.destroy()
            self.rex_lives() # re-do the image for lives
        self.shownumber(self.drawn_number) # runs the shownumber method with new list

# end of DinoFrame

def main():
    root = Tk() #creates the tk
    root.resizable(0,0)
    root.title("Dinomuncher USA!")

    app = DinoFrame(master=root) # initialize the application

    app.pack(side="top", fill="both", expand="true", padx=4, pady=4) # pad gives window a little extra room

    # calling the piece method and initializes player1
    player1 = "rex_skull2.gif" # sets the variable to a string
    app.piece("player1",player1,0,0) # calls the piece method arguments are (name, image, row, column)

    #testing

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