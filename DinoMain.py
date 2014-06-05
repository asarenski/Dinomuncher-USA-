'''
Dinomuncher USA!
DinoMain.py written by: Adam Sarenski
05/2014

The main file creates tkinter frames. It also initializes the program for play.
This file requires the input of MathFile.py to work.
'''

# tkinter is a GUI writing module that can also be used to write games
from Tkinter import *
from MathFile import math_main
import random
import pyaudio
import wave

class Select_Menu(Frame):
    def __init__(self, master, text, height, width, *args, **kwargs):

        """Initializes the selection menu for operation choice"""
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
        """Initializes the main frame with game-board."""

        # initialize variables
        # initially used for self.refresh, which is the checker board
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2

        # a dictionary for any pieces on the game board
        self.pieces = {}
        self.player1 = 0
        self.meteor1 = 0
        self.meteoron = 0

        # more piece variables
        self.metx0 = 0
        self.mety0 = 0

        # variables used initially by the callbacks and drawing the numbers
        # number marker for right or wrong answer
        self.number_marker = []
        # number list used to draw
        self.drawn_number = []
        # the comparative number
        self.op_number = 0
        # the type of comparison operation
        self.op_type = ''

        # string variable for label for operation
        self.v = StringVar()
        # string variable used for the score tracker
        self.v1 = StringVar()
        # string for the level counter
        self.v2 = StringVar()
        # int variable used to track points
        self.point_track = 0
        self.level_track = 1
        # used to increase the difficulty of the meteor
        self.mlevel_track = self.level_track
        # number of lives at the start
        self.life_track = 3

        # sets the width of the board default 6*96
        canv_width = columns * size
        canv_height = rows * size

        # initializes the frame
        Frame.__init__(self, master)

        # setting all the buttons for the select menu
        self.select1 = Select_Menu(self, '', height=100, width=300)
        # setting the button commands to the functions below
        self.select1.callback1 = self.callback1
        self.select1.callback2 = self.callback2
        self.select1.callback3 = self.callback3
        self.select1.callback4 = self.callback4
        self.select1.callback5 = self.callback5
        self.select1.place(x=0, y=50, relwidth=1, relheight=1)
        # sets the select menu as the top layer on Frame
        self.select1.lift

        operation_label = Label(master,justify="c", textvariable=self.v,
                                font=("TkHeadingFont", "16"), pady=10).pack({"side": "top"})
        self.v.set("Select an Operation")

        score_label = Label(self, justify='c', textvariable=self.v1).pack({'side':'top'})
        self.v1.set('Score: '+ str(self.point_track))

        level_label = Label(self, justify='c', textvariable=self.v2).pack({'side':'top'})
        self.v2.set('Level: '+str(self.level_track))

        # Canvas is a widget in Tkinter, in which you can draw
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                             width=canv_width, height=canv_height, background="white")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # initializes the checkered board with self.refresh
        self.refresh()

        # initialize widgets
        self.createWidgets()

        # starts the loop for the meteor enemy
        self.meteor()

        #jpark
        self.play_jpark_one()

    def play_jpark_one(self):
        self.wf = wave.open('jpark.wav', 'rb')
        self.p = pyaudio.PyAudio()
        def callback(in_data, frame_count, time_info, status):
            data = self.wf.readframes(frame_count)
            return (data, pyaudio.paContinue)
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels=self.wf.getnchannels(),
                        rate=self.wf.getframerate(),
                        output=True,
                        stream_callback=callback)

    def play_jpark_two(self):
        self.stream.start_stream()
        if self.stream.is_active == True:
            self.after(1,self.play_jpark_two)
        else:
            self.stream.stop_stream()
            self.stream.close()
            self.wf.close()
            self.p.terminate()

    def callback1(self):
        """ Definitions for the operation selection (callback functions)
        these unpack the num_dict and turn it into useful lists via for loop.
        xtuple is then used to create the drawn_number list and the number_marker_list
        the third value of xtuple is taken as a True or False for solving the operation requirement
        """
        self.op_type = "Multiples"
        self.lift()
        # pulls num_dict from math_main and sets as math_dict
        math_dict = math_main(self.op_type)

        for i in range (30):
            xtuple = ()
            xtuple = math_dict[i]
            self.drawn_number.append(xtuple[0])
            self.number_marker.append(xtuple[3])
        self.op_number = xtuple[2]
        # inputs num_list to show numbers on board
        self.shownumber(self.drawn_number)
        self.v.set(self.op_type + " of " + str(self.op_number))
        self.v1.set('Score: '+ str(self.point_track))
        self.v2.set('Level: '+str(self.level_track))
        self.rex_lives()

    def callback2(self):
        """ Definitions for the operation selection (callback functions) see docstring in callback1"""
        self.op_type = "Multiplication"
        self.lift()
        math_dict = math_main(self.op_type)
        for i in range (30):
            xtuple = ()
            xtuple = math_dict[i]
            self.drawn_number.append(str(xtuple[0])+'x'+str(xtuple[1]))
            self.number_marker.append(xtuple[3])
        self.op_number = xtuple[2]
        self.shownumber(self.drawn_number)
        self.v.set("Equals " + str(self.op_number))
        self.v1.set('Score: '+ str(self.point_track))
        self.v2.set('Level: '+str(self.level_track))
        self.rex_lives()

    def callback3(self):
        """ Definitions for the operation selection (callback functions) see docstring in callback1"""
        self.op_type = "Division"
        self.lift()
        math_dict = math_main(self.op_type)
        for i in range (30):
            xtuple = ()
            xtuple = math_dict[i]
            self.drawn_number.append(str(xtuple[0])+'/'+str(xtuple[1]))
            self.number_marker.append(xtuple[3])
        self.op_number = xtuple[2]
        self.shownumber(self.drawn_number)
        self.v.set("Equals " + str(self.op_number))
        self.v1.set('Score: '+ str(self.point_track))
        self.v2.set('Level: '+str(self.level_track))
        self.rex_lives()

    def callback4(self):
        """ Definitions for the operation selection (callback functions) see docstring in callback1"""
        self.op_type = "Addition"
        self.lift()
        math_dict = math_main(self.op_type)
        for i in range (30):
            xtuple = ()
            xtuple = math_dict[i]
            self.drawn_number.append(str(xtuple[0])+'+'+str(xtuple[1]))
            self.number_marker.append(xtuple[3])
        self.op_number = xtuple[2]
        self.shownumber(self.drawn_number)
        self.v.set("Equals " + str(self.op_number))
        self.v1.set('Score: '+ str(self.point_track))
        self.v2.set('Level: '+str(self.level_track))
        self.rex_lives()

    def callback5(self):
        """ Definitions for the operation selection (callback functions) see docstring in callback1"""
        self.op_type = "Subtraction"
        self.lift()
        math_dict = math_main(self.op_type)
        for i in range (30):
            xtuple = ()
            xtuple = math_dict[i]
            self.drawn_number.append(str(xtuple[0])+'-'+str(xtuple[1]))
            self.number_marker.append(xtuple[3])
        self.op_number = xtuple[2]
        self.shownumber(self.drawn_number)
        self.v.set("Equals " + str(self.op_number))
        self.v1.set('Score: '+ str(self.point_track))
        self.v2.set('Level: '+str(self.level_track))
        self.rex_lives()

    # function for pushbutton widgets
    def createWidgets(self):
        """Function for the pushbutton widgets"""

        # quit button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        # foreground
        self.QUIT["fg"]   = "red"
        # background
        self.QUIT["bg"]   = "blue"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        # print numbers button
        self.hi_there = Button(self)
        self.hi_there["text"] = "Print_Numbers",
        self.hi_there["command"] = self.print_numbers
        self.hi_there.pack({"side": "left"})

        # intial player lives
        self.LIVES = Label(self)
        imgstr = "rex_lives3.gif"
        self.lives_image = PhotoImage(file=imgstr)
        self.LIVES['image'] = self.lives_image
        self.LIVES.pack({'side':'right'})

        # restart button
        self.restart_button = Button(self)
        self.restart_button['text'] = "Restart"
        self.restart_button["command"] = self.restart_game
        self.restart_button.pack({"side": "left"})

    def rex_lives(self):
        """ Lives Tkinter label."""
        if self.life_track == 3:
            imgstr = "rex_lives3.gif"
        elif self.life_track == 2:
            imgstr = "rex_lives2.gif"
        elif self.life_track == 1:
            imgstr = "rex_lives1.gif"
        elif self.life_track <= 0:
            imgstr = "rex_lives0.gif"
            self.restart_game()
        self.lives_image = PhotoImage(file=imgstr)
        self.LIVES['image'] = self.lives_image

    def restart_game(self):
        """Function used if the player runs out of lives or clicks restart button.
        Brings the player back to the select menu.
        """
        self.canvas.delete("piece")
        self.canvas.delete("the_text")
        self.canvas.delete ("circle")

        # because self.meteor and self.flash8 have the longest timers, this tries prevents a bug
        # so far this bug fix does not work
        self.update_idletasks()
        self.after_cancel(self.meteor)
        self.after_cancel(self.flash)
        self.after_cancel(self.flash1)
        self.after_cancel(self.flash2)
        self.after_cancel(self.flash3)
        self.after_cancel(self.flash4)
        self.after_cancel(self.flash5)
        self.after_cancel(self.flash6)
        self.after_cancel(self.flash7)
        self.after_cancel(self.flash8)
        self.update_idletasks()

        self.player1 = PhotoImage(file='rex_skull2.gif')
        self.piece("player1",self.player1,0,0)
        self.select1.lift()

        self.v.set("Game Over , Your Score: " + str(self.point_track) + ", Max Level: " + str(self.level_track))

        del self.number_marker
        self.number_marker = []
        del self.drawn_number
        self.drawn_number = []
        # the comparative number
        self.op_number = 0
        # the type of comparison operation
        self.op_type = ''

        # int variable used to track points
        self.point_track = 0
        self.level_track = 1
        self.mlevel_track = self.level_track
        # number of lives at the start
        self.life_track = 3
        self.QUIT.lift
        self.hi_there.lift

    def half_restart_game(self):
        """Function used if the player beats the level.
        Restarts the game using the same initial operation selection.
        """
        self.canvas.delete("piece")
        self.canvas.delete("the_text")
        self.canvas.delete("circle")

        # because self.meteor and self.flash8 have the longest timers, this tries prevents a bug
        # so far this bug fix does not work
        self.update_idletasks()
        self.after_cancel(self.meteor)
        self.after_cancel(self.flash)
        self.after_cancel(self.flash1)
        self.after_cancel(self.flash2)
        self.after_cancel(self.flash3)
        self.after_cancel(self.flash4)
        self.after_cancel(self.flash5)
        self.after_cancel(self.flash6)
        self.after_cancel(self.flash7)
        self.after_cancel(self.flash8)
        self.update_idletasks()

        self.player1 = PhotoImage(file='rex_skull2.gif')
        self.piece("player1",self.player1,0,0)
        self.select1.lift
        self.level_track += 1
        self.mlevel_track = self.level_track*2 + self.point_track//20

        del self.number_marker
        self.number_marker = []
        del self.drawn_number
        self.drawn_number = []
        # the comparative number
        self.op_number = 0

        if self.op_type == "Multiples":
            self.callback1()
        if self.op_type == "Multiplication":
            self.callback2()
        if self.op_type == "Division":
            self.callback3()
        if self.op_type == "Addition":
            self.callback4()
        if self.op_type == "Subtraction":
            self.callback5()

    def print_numbers(self):
        """print_coord widgest command"""
        print self.drawn_number
        print self.number_marker
        print self.pieces

    def piece(self, name, image, row, column):
        """Puts the image of the piece on the board.
        Also calls placepiece, which puts it in the pieces dictionary.
        """
        self.canvas.create_image(row,column, image = image, tags=(name, "piece"))
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        """function to track coordinates for piece in dictionary 'pieces'
        Technically x0 should be using column. Instead just imagine for the coordinate system
        that the row just means x_i . This is so that it plays nicely with refresh event for board
        """
        self.pieces[name] = [row, column]
        # conversion of board coordinates to canvas coordinates
        x0 = (row * self.size) + int(self.size/2)
        y0 = (column * self.size) + int(self.size/2)
        # when coordinates given, those replace the coords shown here
        self.canvas.coords(name, x0, y0)

    def shownumber(self, drawn_number):
        """function to draw the numbers on the board"""
        self.drawn_number = drawn_number
        self.canvas.delete("the_text")

        # loop draws the drawn numbers
        for row in range(self.rows):
            for col in range(self.columns):
                x1 = (col * self.size) + int(self.size/2)-0
                y1 = (row * self.size) + int(self.size/2)-0
                text1 = drawn_number[col+row*self.columns]
                self.canvas.create_text(x1,y1, font =("Times", "24", "bold"), text=text1, tags="the_text")
        self.refresh()

    def refresh(self):
        """ Initializes the checkered board."""
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            # this part does the actual resizing
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            x0 = (self.pieces[name][0] * self.size) + int(self.size/2)
            y0 = (self.pieces[name][1] * self.size) + int(self.size/2)
            self.canvas.coords(name, x0, y0)
        # raise and lower are like lift and lower
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

    def leftkey(self,event):
        """Controls
        these events will move the player 96 pixels by default.
        leftkey moves the player left.
        """
        # goes into the pieces dictionary and pulls the coord list to check
        if self.pieces['player1'][0]== 0:
            print "cannot move past border"
        else:
            # moves the player 1 space over, which is 96 pixels
            self.canvas.move('player1', -1*self.size, 0)
            # changes the coordinate system
            self.pieces['player1'][0] = self.pieces['player1'][0]-1

    def rightkey(self,event):
        """Controls
        these events will move the player 96 pixels by default.
        leftkey moves the player right.
        """
        if self.pieces['player1'][0]== self.columns-1:
            print "cannot move past border"
        else:
            self.canvas.move('player1', self.size, 0)
            self.pieces['player1'][0] = self.pieces['player1'][0]+1

    def upkey(self,event):
        """Controls
        these events will move the player 96 pixels by default.
        leftkey moves the player up.
        """
        if self.pieces['player1'][1]== 0:
            print "cannot move past border"
        else:
            self.canvas.move('player1', 0, -1*self.size)
            self.pieces['player1'][1] = self.pieces['player1'][1]-1

    def downkey(self,event):
        """Controls
        these events will move the player 96 pixels by default.
        leftkey moves the player down.
        """
        if self.pieces['player1'][1]== self.rows-1:
            print "cannot move past border"
        else:
            self.canvas.move('player1', 0, 1*self.size)
            self.pieces['player1'][1] = self.pieces['player1'][1]+1

    def spacebar(self,event):
        """Spacebar is the main event control for the player. It will test the
        entry and regulates the delivery of feedback to the player.
        """
        # x-variable for the player's location
        x0 = self.pieces['player1'][0]
        # y-variable for the player's location
        y0 = self.pieces['player1'][1]

        # this is the translation to 0:29 for numbers dictionary
        numbers_entry = x0 + y0*self.columns
        print "space hit"

        #a reminder that numbers_entry is 0:29 (space location on board)
        #drawn_numbers is the list of the numbers that are being drawn on the board
        if self.drawn_number[numbers_entry] == '':
            # do nothing
            print "no entry"
        # the drawn_number at the point satisfies the operation
        elif self.number_marker[numbers_entry] == 1:
            if self.life_track <= 0:
                # do nothing
                pass
            else:
                self.point_track += 10
                self.v1.set("Score: " +str(self.point_track))
                print "congrats" + "you now have " + str(self.point_track) + " points"
                # turns the entry into a blank string
                self.drawn_number[numbers_entry] = ''
                self.number_marker[numbers_entry] = 0
                if 1 in self.number_marker:
                    self.shownumber(self.drawn_number)
                else:
                    print "you win"
                    # calls the half_restart_game method
                    self.half_restart_game()
        else:
            print "wrong"
            # subtract a life from the life counter
            self.life_track -= 1
            # re-do the image for lives and check for game-over
            self.rex_lives()
            if self.life_track > 0:
                # turns the entry into a blank string
                self.drawn_number[numbers_entry] = ''
                # make the numbers_marker 0
                self.number_marker[numbers_entry] = 0
                # runs the shownumber method with new list
                self.shownumber(self.drawn_number)
            else:
                pass

    #currently a test area for implementing a meteor
    def subtract_life(self):
        print "death"
        # subtract a life from the life counter
        self.life_track -= 1
        # re-do the image for lives and check for game-over
        self.rex_lives()
        self.placepiece('player1',0,0)

    def meteor(self):
        ''' Creates the flashing circles indicating a meteor is coming.
        It then lowers the circles so they can't be seen.
        After this is done it calls the flash method.
        '''
        self.canvas.delete('circle')
        self.canvas.delete('meteor1')
        def circle(self,name,x,y,r,fill,state):
            self.canvas.create_oval(x-r,y-r,x+r,y+r, fill=fill,state=state, tags=(name,"circle"))
        #canvas coords
        self.metx0 = self.size/2 + self.size * random.randrange(self.columns)
        self.mety0 = self.size/2 + self.size * random.randrange(self.rows)
        meteor_one = circle(self,"one", self.metx0,self.mety0,40,"red","hidden")
        meteor_two = circle(self,"two", self.metx0,self.mety0,30,"red","hidden")
        meteor_three = circle(self,"three", self.metx0,self.mety0,20,"red","hidden")
        self.canvas.lower('one')
        self.canvas.lower('two')
        self.canvas.lower('three')
        self.after(3000/self.level_track,self.flash)

    def flash(self):
        '''Calls the Flash class'''
        flash = Flash(self.canvas,'one')
        self.after(500/self.mlevel_track, self.flash1)
    def flash1(self):
        flash = Flash(self.canvas,'one')
        self.after(500/self.mlevel_track, self.flash2)
    def flash2(self):
        flash = Flash(self.canvas,'two')
        self.after(500/self.mlevel_track, self.flash3)
    def flash3(self):
        flash = Flash(self.canvas,'two')
        self.after(500/self.mlevel_track, self.flash4)
    def flash4(self):
        flash = Flash(self.canvas,'three')
        self.after(500/self.mlevel_track, self.flash5)
    def flash5(self):
        flash = Flash(self.canvas,'three')
        self.after(500/self.mlevel_track, self.flash6)
    def flash6(self):
        """This is where you call the meteor onto the board"""
        # for some reason this needs to stay global
        self.meteor1 = PhotoImage(file='Meteor1.gif')
        # calls piece method and converts the canvas pixel coords into row/col coords
        self.piece('meteor1',self.meteor1,self.metx0/self.size,self.mety0/self.size)
        self.refresh()
        self.after(5, self.flash7)
    def flash7(self):
            player_pos = self.pieces['player1']
            meteor_pos = self.pieces['meteor1']
            if player_pos == meteor_pos:
                self.subtract_life()
            else:
                pass
            self.after(200,self.flash8)
    def flash8(self):
        self.canvas.delete('meteor1')
        self.canvas.delete('circle')
        self.pieces.pop('meteor1')
        self.meteor()

class Flash():
    def __init__(self,canvas,name):
        '''Used for when the meteor will hit'''
        self.canvas = canvas
        self.name = name
        self.flash_main()

    def flash_main(self):
        '''Flashes where the meteor will hit'''
        self.canvas.lift(self.name)
        current_state = self.canvas.itemcget(self.name,'state')
        if current_state == "normal":
            new_state = "hidden"
            self.canvas.itemconfigure(self.name,state=new_state)
        else:
            self.canvas.itemconfigure(self.name,state='normal')

def main():
    """Initializes the root, creates the tk, and starts the game."""
    root = Tk()
    root.resizable(0,0)
    root.title("Dinomuncher USA!")

    # initialize the application
    app = DinoFrame(master=root)

    # pad gives window a little extra room
    app.pack(side="top", fill="both", expand="true", padx=4, pady=4)

    # calling the piece method and initializes player1
    # sets the variable to a string
    player1 = PhotoImage(file='rex_skull2.gif')
    # calls the piece method arguments are (name, image, row, column)
    app.piece("player1",player1,0,0)

    # key bindings
    # lambda allows you to write user input functions
    root.bind('<Escape>', lambda e: app.quit())
    root.bind('<Left>',app.leftkey)
    root.bind('<Right>',app.rightkey)
    root.bind('<Up>',app.upkey)
    root.bind('<Down>',app.downkey)
    root.bind('<space>',app.spacebar)

    # begins the event loop of the root
    root.mainloop()
main()