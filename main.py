from tkinter import *

root = Tk()
root.configure(bg="#293C4A", bd=10)
root.title("Nerd Calculator")


button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}



button_7 = Button(root, button_params_main, text='7',
                  command=lambda:button_click('7')).grid(row=6, column=0, sticky="nsew")
button_8 = Button(root, button_params_main, text='8',
                  command=lambda:button_click('8')).grid(row=6, column=1, sticky="nsew")
button_9 = Button(root, button_params_main, text='9',
                  command=lambda:button_click('9')).grid(row=6, column=2, sticky="nsew")


button_4 = Button(root, button_params_main, text='4',
                  command=lambda:button_click('4')).grid(row=7, column=0, sticky="nsew")
button_5 = Button(root, button_params_main, text='5',
                  command=lambda:button_click('5')).grid(row=7, column=1, sticky="nsew")
button_6 = Button(root, button_params_main, text='6',
                  command=lambda:button_click('6')).grid(row=7, column=2, sticky="nsew")


button_1 = Button(root, button_params_main, text='1',
                  command=lambda:button_click('1')).grid(row=8, column=0, sticky="nsew")
button_2 = Button(root, button_params_main, text='2',
                  command=lambda:button_click('2')).grid(row=8, column=1, sticky="nsew")
button_3 = Button(root, button_params_main, text='3',
                  command=lambda:button_click('3')).grid(row=8, column=2, sticky="nsew")


button_0 = Button(root, button_params_main, text='0',
                  command=lambda:button_click('0')).grid(row=9, column=0, sticky="nsew")



root.mainloop()