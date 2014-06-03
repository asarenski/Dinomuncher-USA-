from Tkinter import *

def practice_one():
    root = Tk()

    canvas_one = Canvas(master=root, width=200, height=100)
    canvas_one.pack()

    canvas_one.create_line(0, 0, 200, 100)
    #canvas_one.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

    #canvas_one.create_rectangle(50, 25, 150, 75, fill="blue")

    root.bind("<Escape>", lambda e: root.quit())
    root.mainloop()

def flashing_circle():
    root = Tk()

    canvas_one = Canvas(master=root, width=400, height=200)
    canvas_one.pack()
    light_up=False


    def circle(name,x,y,r,fill):
        canvas_one.create_oval(x-r,y-r,x+r,y+r, fill=fill, tags=(name,"circle"))


    def circle_one():
        current_color = canvas_one.itemcget('one','fill')

        if current_color == "red":
            new_color = "blue"
            canvas_one.itemconfigure('one', fill=new_color)
        else:
            canvas_one.itemconfigure('one', fill="red")
        current_color = canvas_one.itemcget('one','fill')
        print current_color
        root.after(1000, circle_one)

    circle_canv = circle("one", 200,100,50,"blue")
    circle_one()

    root.bind("<Escape>", lambda e: root.quit())
    root.mainloop()
flashing_circle()
