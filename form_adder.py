'''
Created on 17 May 2018

@author: mark
'''
from form import Form
import Tkinter as tk
class FormAdder(Form):
    def btn_command(self):
        self.entries['result'].insert(tk.END,
            float(self.entries['A'].get()) +
            float(self.entries['B'].get())
            )
            
    def setup(self):
        self.add_rows('A', 'B', 'result')
        self.add_button = tk.Button(text='Add',command=self.btn_command)
        self.add_button.grid(row=self.rows+1, column=1, columnspan=2)
        
if __name__=='__main__':
    FormAdder()    
