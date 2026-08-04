import os
import csv


def csv_parameters():

    with open(rf'{os.getcwd()}\month-01-python\Day 15\people.csv','r') as file:
        reader=csv.reader(file,skipinitialspace=True,delimiter=',',quoting=csv.QUOTE_ALL)
        for row in reader:
            print(row)


csv_parameters()
