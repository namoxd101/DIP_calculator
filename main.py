import tkinter as tk
class MyCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("470x650")
        self.root.resizable(0, 0)
        self.root.title("Calculator Pro X +++")
        self.root.option_add("*Font", "ComicSansMS 25")
        self.root.title(self.title)


        self.label = tk.Label(self.root, text="Calculator Pro X +++", font=('Comic Sans MS', 30))
        self.label.grid(row=0, column=0, columnspan=4, sticky="NEWS", padx=20, pady=(20, 10), ipadx=20, ipady=10)
        self.label = tk.Label(self.root, text=" ", font=('Comic Sans MS', 30),bg="yellow")
        self.label.grid(row=1, columnspan=4, padx=20, pady=(0, 10), ipadx=20, ipady=10)
        

        self.button = tk.Button(self.root, text="CE", width=3, height=1)
        self.button.grid(row=2, column=0)
        self.button = tk.Button(self.root, text="()", width=3, height=1)
        self.button.grid(row=2, column=1)
        self.button = tk.Button(self.root, text="%", width=3, height=1)
        self.button.grid(row=2, column=2)
        self.button = tk.Button(self.root, text="/", width=3, height=1)
        self.button.grid(row=2, column=3)
        self.button = tk.Button(self.root, text="x", width=3, height=1)
        self.button.grid(row=3, column=3)
        self.button = tk.Button(self.root, text="-", width=3, height=1)
        self.button.grid(row=4, column=3)
        self.button = tk.Button(self.root, text="+", width=3, height=1)
        self.button.grid(row=5, column=3)
        self.button = tk.Button(self.root, text="7", width=3, height=1)
        self.button.grid(row=3, column=0)
        self.button = tk.Button(self.root, text="8", width=3, height=1)
        self.button.grid(row=3, column=1)
        self.button = tk.Button(self.root, text="9", width=3, height=1)
        self.button.grid(row=3, column=2)
        self.button = tk.Button(self.root, text="4", width=3, height=1)
        self.button.grid(row=4, column=0)
        self.button = tk.Button(self.root, text="5", width=3, height=1)
        self.button.grid(row=4, column=1)
        self.button = tk.Button(self.root, text="6", width=3, height=1)
        self.button.grid(row=4, column=2)
        self.button = tk.Button(self.root, text="1", width=3, height=1)
        self.button.grid(row=5, column=0)
        self.button = tk.Button(self.root, text="2", width=3, height=1)
        self.button.grid(row=5, column=1)
        self.button = tk.Button(self.root, text="3", width=3, height=1)
        self.button.grid(row=5, column=2)
        self.button = tk.Button(self.root, text="+/-", width=3, height=1)
        self.button.grid(row=6, column=0)
        self.button = tk.Button(self.root, text="0", width=3, height=1)
        self.button.grid(row=6, column=1)
        self.button = tk.Button(self.root, text=".", width=3, height=1)
        self.button.grid(row=6, column=2)
        self.button = tk.Button(self.root, text="=", width=3, height=1)
        self.button.grid(row=6, column=3)
      


        self.root.mainloop()


MyCalculator()