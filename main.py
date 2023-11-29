import tkinter as tk
class MyCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x480")
        self.root.title("Calculator Pro X +++")

        self.label = tk.Label(self.root, text="Calculator Pro X +++", font=('Comic Sans MS', 40))
        self.label.pack()
        self.button = tk.Button(self.root, text="CE", font=('Comic Sans MS', 25))
        self.button.place(x=75, y=150)
        self.button = tk.Button(self.root, text="/", font=('Comic Sans MS', 25))
        self.button.place(x=190, y=150)
        self.button = tk.Button(self.root, text="x", font=('Comic Sans MS', 25))
        self.button.place(x=275, y=150)
        self.button = tk.Button(self.root, text="-", font=('Comic Sans MS', 25))
        self.button.place(x=360, y=150)
        self.button = tk.Button(self.root, text="+", font=('Comic Sans MS', 25))
        self.button.place(x=445, y=150)
        self.button = tk.Button(self.root, text="7", font=('Comic Sans MS', 25))
        self.button.place(x=85, y=240)
        self.button = tk.Button(self.root, text="8", font=('Comic Sans MS', 25))
        self.button.place(x=185, y=240)
        self.button = tk.Button(self.root, text="9", font=('Comic Sans MS', 25))
        self.button.place(x=285, y=240)
        self.button = tk.Button(self.root, text="4", font=('Comic Sans MS', 25))
        self.button.place(x=85, y=340)


        self.root.mainloop()


MyCalculator()