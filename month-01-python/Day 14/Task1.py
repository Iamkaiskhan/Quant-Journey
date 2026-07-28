import os
import csv


def creating_csv():
    current_directory=os.getcwd()
    with open(f'{current_directory}\people.csv','w') as file:
        file.write('name,age,branch')


def csv_file(x):
        

    if x=='list':
        with open(f'{os.getcwd()}\month-01-python\Day 14\people.csv','r') as file:
            reading=csv.reader(file)   # it will read the file in list format

            for row in reading:   # it will print the file in list format, this loop should be inside the with block to avoid ValueError: I/O operation on closed file.
                print(row)

    elif x=='dictonary':
        with open(f'{os.getcwd()}\month-01-python\Day 14\people.csv','r') as file:
            csv_filee=csv.DictReader(file)   # it will read the file in dictionary format

            for row in csv_filee:   # it will print the file in dictionary format, this loop should be inside the with block to avoid ValueError: I/O operation on closed file.
                print(row)


def main():

    format=input('Enter the format in which you want to read the file(list/dictonary): ')
    csv_file(format)


with open(rf'{os.getcwd()}\month-01-python\Day 14\task2.py','w') as f:
    f.write('#print(\'This is task 2\')')

