import os 
import csv

def csv_quotes():
    with open('day 17/quotes.csv','r') as csv_file:
        reading=csv.reader(csv_file,quoting=csv.QUOTE_ALL,skipinitialspace=True)
        for row in reading:
            print(row)



# now we will learn about dialect,it is similar like creating a function and to use it for multiple files

csv.register_dialect('mydialect',
                     skipinitialspace=True,
                     delimiter='|',
                     quoting=csv.QUOTE_ALL)


def csv_dialect_test():
    with open('day 17/office.csv','r') as file:
        reading=csv.reader(file,dialect='mydialect')

        for row in reading:
            print(row)


# lets learn about sniffer()

def csv_dialectread():
    with open('day 17/office.csv','r') as file:
        sample=file.read(70)   # this will read intial 70 characters of the file
        has_heading=csv.Sniffer().has_header(sample)   # it will check if the file has heading or not
        print(has_heading)

        dialect=csv.Sniffer().sniff(sample)   # it will automatically fetch the dialect data


    with open('day 17/office.csv','r') as file:
        reading=csv.reader(file,dialect)
        for row in reading:
            print(row)

csv_dialectread()




