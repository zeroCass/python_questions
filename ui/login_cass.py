from tkinter import *
from tkinter import messagebox


class Window(Toplevel):
    def __init__(self, parent:Tk, window_name:str, geometry:str, w, h):
        super().__init__(parent)
        self.title(window_name)
        self.resizable(False, False)
        self.parent = parent
        self.label = Label(self, text='Main Frame').pack()
        self.protocol('WM_DELETE_WINDOW', quit)

        print('scwidth: %s' % self.winfo_screenmmwidth())
        print('scheight: %s' % self.winfo_screenmmheight())

        



        
    def quit(self) -> None:
        self.parent.destroy()





class Login(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry('300x100')
        self.title('Login screen')
        self.resizable(False, False)

        self.login_label = Label(self, text='Login').place(x=10, y=10)
        self.login_entry = Entry(self, width=30)
        self.login_entry.place(x=70, y=10)
        self.pass_label = Label(self, text='password').place(x=10, y=35)
        self.pass_entry = Entry(self, width=30)
        self.pass_entry.place(x=70, y=35)
        self.login_btn = Button(self, text='Sign in', command=self.sign_in).place(x=130, y=65)
        
    
    def sign_in(self):
        if self.login_entry.get() != '' and self.pass_entry.get() != '':
            self.withdraw()
            new_window = Window(self, 'Main', '500x500')
            
        else:
            messagebox.showerror('Error', 'Os campos devem ser preenchidos corretamente!',)
            