from tkinter import *


root = Tk()
root.configure(bg="#293C4A", bd=10)
root.title("Nerd Calculator")


#--1st row--
# Transform number to percentage
percentage = Button(root, button_params, text='%',
               command=percent).grid(row=5, column=3, sticky="nsew")

#--3rd row--
mul = Button(root, button_params_main, text='*',
             command=lambda:button_click('*')).grid(row=7, column=3, sticky="nsew")
div = Button(root, button_params_main, text='/',
             command=lambda:button_click('/')).grid(row=7, column=4, sticky="nsew")

#--4th row--
add = Button(root, button_params_main, text='+',
             command=lambda:button_click('+')).grid(row=8, column=3, sticky="nsew")
sub = Button(root, button_params_main, text='-',
             command=lambda:button_click('-')).grid(row=8, column=4, sticky="nsew")

#--5th row--
equal = Button(root, button_params_main, text='=',
               command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")


root.mainloop()