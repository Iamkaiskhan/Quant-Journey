import csv
import os


def txt_file():
    with open('Day 15/file.txt','w') as file:
        file.write('My name is Kais Khan\nI am learning Python')


def file_read():
    f=open('Day 15/file.txt','r')
    data=f.read()
    print(data)

    # once the file reads the whole file it will then only give spaces as output,the file is readed only once
    line1=f.readline()
    print(line1)

    line2=f.readline()
    print(line2)


    f.close()

# now we will learn to write in a file

def file_write():
    f=open('Day 15/file.txt','w')
    f.write('My name is Kais Khan\nI am learning Python\nI want to be a quant trader')

    f.close()

def file_append():
    f=open('Day 15/file.txt','a')
    f.write('\nI want to complete my python course in next 12 months')
    f.close()

#file_append()

# lets learn about r+,w+ and a+

def file_rplus():
    f=open('Day 15/file.txt','r+')
    f.write('abc')   # r+ will overwrite in the file with pointer at beginning,but if u will read the file it will print after the overwrite statement because pointer is shifted further
    data=f.read()       # r+ is open for both read and write
    print(data)
    f.close()

def file_wplus():
    f=open('Day 15/file.txt','w+')   # it is open for both read and write and it truncates the file
    data=f.read()
    print(data)
    f.close()

#file_wplus()

def file_aplus():
    f=open('Day 15/file.txt','a+') # a+ allows to read and write,but the cursor starts from end ,so if u want to read nothing will print 
    data=f.read()
    print(data)
    f.write('\nI am a student')
    data=f.read()
    print(data)
    f.close()

# practice
with open('Day 15/practice.txt','w') as file:
    file.write('Hi everyone\nwe are learning file I/O\nusing java\nI like programming in java')

def replace():
    # To replace Java with Python
    with open('Day 15/practice.txt','r') as file:
        data=file.read()  # it will store data as string


    new_data=data.replace('java','Python')
    print(new_data)



def find_word():
    # if to check if the word is present in the text file or not
    with open('Day 15/practice.txt','r') as file:
        data=file.read()

        word='clearning'
        if (data.find(word)!=-1):
            print('Found')

        else :
            print('Not Found')

def word_line():

    with open('Day 15/practice.txt','r') as file:

        data=True

        word=input("Enter the word:")
        line=1
        while data:
            data=file.readline()

            if (word in data):
                print(f'{word} found in line {line}')
                
            line+=1

        data=file.read()
        if (word not in data):
            print(f'{word} not found')


def word_line_loopmethod():
    status=False
    line=1
    with open('Day 15/practice.txt','r') as file:

        word=input('Enter the word:')

        for text in file:
            if word in text:
                print(f'{word} found in line {line}')
                status=True

            line+=1

        if not status:
            print(f'{word} not found')

word_line_loopmethod()


            
            

