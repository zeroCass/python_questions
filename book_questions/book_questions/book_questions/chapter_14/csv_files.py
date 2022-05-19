import csv
import enum
from operator import delitem
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir('..\\automate_online_materials')

with open('example.csv') as file:
    csv_reader = csv.reader(file)
    # convert into 2d list (matriz)
    data = list(csv_reader)
    # so, is able to acess using this notation
    print(data[0][0])
    

with open('example.csv', newline='') as file, open('csvwriter.csv', 'w', newline='') as write_file:
    csv_reader = csv.reader(file)
    # for large files, use loop to load small pieces in memory
    for row in csv_reader:
        print(', '.join(row))
    
    students = {
        'Jose': 5.5,
        'Maria': 7.8,
        'Jao': 9.891
    }

    # is possivel to define how the file will be write with delimiter and linetermintor
    csv_writer = csv.writer(write_file, delimiter='\t', lineterminator='\n\n')
    for key in students:
        csv_writer.writerow([str(key), str(students[key])])
