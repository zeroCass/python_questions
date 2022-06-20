import os
PATH = os.path.join(os.environ['USERPROFILE'], '\AppData\Roaming\Python\Python310\chromedriver.exe')
for file in os.walk(PATH):
    print(file)