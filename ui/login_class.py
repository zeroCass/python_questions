from tkinter import *
from tkinter import messagebox


class Window(Toplevel):
    def __init__(self, parent:Tk, window_name:str, geometry:str):
        super().__init__(parent)
        self.title(window_name)
        self.resizable(False, False)
        self.parent = parent
        #self.label = Label(self, text='Main Frame').pack()
        self.protocol('WM_DELETE_WINDOW', quit)
        self.geometry(geometry)
    
    def back(self):
        self.parent.deiconify()
        self.destroy()
        
    def quit(self) -> None:
        self.parent.destroy()



class Lobby(Window):
    def __init__(self, parent: Tk, window_name: str, geometry: str):
        super().__init__(parent, window_name, geometry)
        self.label = Label(self, text='SOU UMA LABEL FODA!!').pack()
        self.back_btn = Button(self, text='Back', command=super().back).pack()
    

class MainWindow(Window):
    def __init__(self, parent: Tk, window_name: str, geometry: str):
        super().__init__(parent, window_name, geometry)
        self.btn_lobby = Button(self, text='Lobby list', command=self.__get_lobby_list).pack()

    def __get_lobby_list(self):
        self.withdraw()
        Lobby(self, 'Lobby List', '300x300')




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
        self.login_btn = Button(self, text='Sign in', command=self.sign_in).place(x=160, y=65)
        self.register_btn = Button(self, text='Register', command=self.__register).place(x=80, y=65)

        
    
    def sign_in(self):
        if self.login_entry.get() != '' and self.pass_entry.get() != '':
            self.withdraw()
            MainWindow(self, 'Main', '500x500')
        else:
            messagebox.showerror('Error', 'Os campos devem ser preenchidos corretamente!',)

    def __register(self):
        self.withdraw()
        Register(self)



class Register(Tk):
    def __init__(self, parent):
        super().__init__()
        self.geometry('400x400')
        self.resizable(False, False)
        self.parent = parent

        #labels
        self.label_name = Label(self, text='Nome').grid(column=0, row=0)
        self.label_data_nsc = Label(self, text='Data de Nascimento').grid(column=0, row=1)
        self.label_email = Label(self, text='Email').grid(column=0, row=2)
        self.password = Label(self, text='Senha').grid(column=0, row=3)

        #Entries
        self.entry_name = Entry(self, width=100)
        self.entry_name.grid(column=1, row=0)
        self.entry_data_nsc = Entry(self, width=50).grid(column=1, row=1)
        self.entry_email = Entry(self, width=50).grid(column=1,row=2)
        self.entry_password = Entry(self, width=50).grid(column=1, row=3)

        #buttons
        self.btn_register = Button(self, text='Registrar', command=self.__register).grid(column=0, row=4)

    def __register(self):

        # verificar se os dados sao validos
        if self.entry_name.get() != '':
            print('Registrado')
            self.parent.deiconify()
            self.destroy()

        # inserir dados no banco de dados