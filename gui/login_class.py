from tkinter import *
from tkinter import messagebox


class Window(Toplevel):
    def __init__(self, parent:Tk, main_window:Tk, window_name:str, geometry:str):
        super().__init__(parent)
        self.title(window_name)
        self.resizable(False, False)
        self.parent = parent
        self.main_window = main_window
        self.label = Label(self, text='Main Frame').pack()
        self.protocol('WM_DELETE_WINDOW', self.quit)
        self.geometry('%s+%d+%d' % (geometry, ((1080/2)), ((920/2))))
        
    def quit(self) -> None:
        self.main_window.destroy()
        print(f'destroyin {self.main_window} from {self}')


    def back(self) -> None:
        self.parent.deiconify()
        self.destroy()



class MainApp(Window):
    def __init__(self, parent: Tk, main_window:Tk, window_name: str, geometry: str):
        super().__init__(parent, main_window, window_name, geometry)
        self.name_label = Label(self, text='Name').pack()
        self.btn_lobby_list = Button(self, text='Lobby list', command=self.__get_lobby).pack()
        #self.btn_back = Button(self, text='Back', command=self.__back).pack()


    def __get_lobby(self):
        self.withdraw()
        Lobby(self, self.main_window, 'Lobby Window', '500x500')



class Lobby(Window):
    def __init__(self, parent: Tk, main_window:Tk, window_name: str, geometry: str):
        super().__init__(parent, main_window, window_name, geometry)
        self.name_label = Label(self, text='Lobby').pack()
        self.btn_back = Button(self, text='Back', command=self.back)
        self.btn_back.pack()



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
            MainApp(self, self,  'Main', '500x500')
            
        else:
            messagebox.showerror('Error', 'Os campos devem ser preenchidos corretamente!',)
            