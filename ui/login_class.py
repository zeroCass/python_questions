from tkinter import *
from numpy import sign

from pyparsing import col


class Login(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry('300x100')
        self.title('Login screen')
        self.resizable(False, False)

        self.login_label = Label(self, text='Login')
        self.login_label.grid(column=0, row=0, sticky='w', padx=10)
        self.login_entry = Entry(self, width=30)
        self.login_entry.grid(column=1, row=0)
        self.pass_label = Label(self, text='password')
        self.pass_label.grid(column=0, row=1)
        self.pass_entry = Entry(self, width=30)
        self.pass_entry.grid(column=1, row=1)
        self.login_btn = Button(self, text='Sign in', command=self.sign_in)
        self.login_btn.grid(row=2, columnspan=2)
    
    def sign_in(self):
        if self.login_entry.get() != '' and self.pass_entry.get() != '':
            print(self.login_entry.get(), self.pass_entry.get())
        else:
            print('Preencha os campos adequadamente!')



        


