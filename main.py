from tkinter import *


root = Tk()
root.configure(bg="#293C4A", bd=10)
root.title("Nerd Calculator")


button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}


#--1st row--
# Add a left parentheses
left_par = Button(root, button_params, text='(',
                  command=lambda:button_click('(')).grid(row=5, column=0, sticky="nsew")
# Add a right parentheses
right_par = Button(root, button_params, text=')',
                   command=lambda:button_click(')')).grid(row=5, column=1, sticky="nsew")   
# Add a +/-
signs = Button(root, button_params, text='\u00B1',
                   command=sign_change).grid(row=5, column=2, sticky="nsew") 

#--2nd row--
delete_one = Button(root, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='DEL', command=button_delete, bg='#db701f').grid(row=6, column=3, sticky="nsew")
delete_all = Button(root, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='AC', command=button_clear_all, bg='#db701f').grid(row=6, column=4, sticky="nsew")

#--5th row--
point = Button(root, button_params_main, text='.',
               command=lambda:button_click('.')).grid(row=9, column=1, sticky="nsew")


root.mainloop()