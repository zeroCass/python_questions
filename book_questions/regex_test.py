import sys, os

file_name = 'wiki.txt'
try:
    with open(file_name, 'r'):
        file = file_name.read()
    
except FileNotFoundError as e:
    print(e)
