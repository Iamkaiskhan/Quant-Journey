#print('This is task 2')
# now we will learn to write in csv file using csv module in python
import os
import csv
import pandas as pd
def write_as_list():
    with open(rf'{os.getcwd()}\month-01-python\Day 14\movies.csv','w') as file:
        writing=csv.writer(file)  # it will write the file in list format
        writing.writerow(['SN','movie','year'])
        writing.writerow([1,'Iron man',2000])
        writing.writerow([2,'Spider Man',1998])


def write_as_dictonary():
    with open(rf'{os.getcwd()}\month-01-python\Day 14\player.csv','w',newline='') as file:
        fieldnames=['player_name','fide_rating']    # it is the coloumn names
        writer=csv.DictWriter(file,fieldnames=fieldnames) # it will tell to access the file and fieldname will give acess to column

        writer.writeheader()   # it will write the column, without this header will not be created

        writer.writerow({'player_name': 'Kais Khan','fide_rating': 3210})
        writer.writerow({'player_name':'Tania','fide_rating':3500})

# To write and read csv through panda module

## To read csv file
def readcsv_panda():

    k=pd.read_csv(rf'{os.getcwd()}\month-01-python\Day 14\player.csv')
    print(k)


## To create a csv file


def create_csv_panda():


    # first create a data-frame
    dp=pd.DataFrame([['kais',2005],['sama',2003]],columns=['Name','age'])

    # then move data frame to csv file
    dp.to_csv(rf'{os.getcwd()}\month-01-python\Day 14\info.csv')


