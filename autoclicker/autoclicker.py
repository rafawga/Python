import tkinter as tk

class Main():

    def __init__(self, root):
        self.root = root
        self.count = 0

        frame = tk.Frame(self.root)
        frame.pack()

        btn = tk.Button(frame, text ='click me')
        btn.pack()
        btn.bind('<Button-1>', self.click)

        self.lbl = tk.Label(frame, text = 'Count is 0')
        self.lbl.pack()

    def click(self, event):
        self.count += 1
        self.lbl.config(text=f'count {self.count}')
        if self.count == 20:
            self.count == 0


if __name__=="__main__":
    root = tk.Tk()
    Main(root)
    root.mainloop()