import Tkinter as tk
class Page(tk.Frame):
    def __init__(self, master, text, height, width, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=20, **kwargs)
        self.height = height
        self.width = width
        button = tk.Button(self, text=text, font=('Comic Sans MS', 20),
                           command=lambda: self.callback())
        button.pack(side="top", fill="both", expand=True)
    def onlift(self):
        root.geometry('{}x{}'.format(self.width, self.height))
        self.lift()

class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        p1 = Page(self, 'This is page 1', height=200, width=300)
        p2 = Page(self, 'Next page is 2', height=400, width=300)
        p3 = Page(self, 'We love number 3', height=400, width=600)
        p1.callback = p2.onlift
        p2.callback = p3.onlift
        p3.callback = p1.onlift

        p1.place(x=0, y=0, relwidth=1, relheight=1)
        p2.place(x=0, y=0, relwidth=1, relheight=1)
        p3.place(x=0, y=0, relwidth=1, relheight=1)

        p1.onlift()

root = tk.Tk()
app = App(root)
root.mainloop()