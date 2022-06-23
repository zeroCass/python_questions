import pathlib
import os

home = str(pathlib.Path.home())
print(home)
#PATH = os.path.join(home, '\AppData\Roaming\Python\Python310')
PATH = home + '\AppData\Roaming\Python\Python310'
print(PATH)
for file in os.walk(PATH):
    print(file)



