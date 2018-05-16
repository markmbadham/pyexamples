'''
Created on 16 May 2018

@author: mark
'''
import Tkinter as tk

win = tk.Tk()

text = tk.Text()
text.grid(row=2, column=1, columnspan=2)
def button_press():
    text.insert(0.0, "Button pressed")
def button_push():
    print text.get(0.0, tk.END)
button = tk.Button(text='press', command=button_press)
button.grid(row=1, column=1)
button2 = tk.Button(text='push', command=button_push)
button2.grid(row=1, column=2)
#button['command'] = button_press
win.mainloop()