import os 
import csv


def create_filetxt():
    with open('Day 16/numbers.txt','w') as file:
        file.write('1,2,3,4,5,6,7,8,9,1,2,13,4,34,5,56,657,3423,65,23,4,56,4,365,467,3,5,2')




def even_numbers_count():

    with open('Day 16/numbers.txt','r') as file:
        data=file.read()
        print(data)
        num=''
        number_list=[]
        for i in range(len(data)):
            if data[i]==',':
                number_list.append(int(num))
                num=''

            else:
                num+=data[i]

        number_list.append(int(num))  # the last number have to be print like this
            
    print(number_list)
    status=True
    for i in range(len(number_list)):
        if number_list[i]%2==0:
            if status:
                print('The even numbers are:')
                status=False
            print(number_list[i])

    if status:
        print('There are no even numbers')



even_numbers_count()