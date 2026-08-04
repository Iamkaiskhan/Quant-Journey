import csv
import os

def csv_quotes():
    row_list = [
        ['Book', 'Quote'],
        ['Lord of the Rings',
            '"All we have to decide is what to do with the time that is given us."'],
        ['Harry Potter', '"It matters not what someone is born, but what they grow to be."']
    ]

    with open(r'day 18\quotes.csv','w',newline='') as file:

        writing=csv.writer(file,quoting=csv.QUOTE_NONE,escapechar='/')

        writing.writerows(row_list)



csv_quotes()