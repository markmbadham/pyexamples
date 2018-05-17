'''
Created on 17 May 2018

@author: mark
'''
import Tkinter as tk

class Form(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.rows = 0
        self.entries = {}
        self.setup()
        self.mainloop(0)
    
    def add_rows(self, *titles):
        for title in titles:
            self.rows += 1
            label = tk.Label(text=title)
            label.grid(row=self.rows, column=1)
            entry = tk.Entry()
            entry.grid(row=self.rows, column=2)
            self.entries[title] = entry
            
    def btn_command(self):
        for title, entry in self.entries.items():
            print title, entry.get()
            
    def setup(self):
        self.add_rows('name', 'surname', 'age')
        self.print_button = tk.Button(text='print',command=self.btn_command)
        self.print_button.grid(row=self.rows+1, column=1, columnspan=2)
        
if __name__=='__main__':
    Form()    
