import os
import csv
# we will learn about writing in python 

# example to write single rows at a time

def csv_singlerow():
    with open('day 17/innovators.csv','w') as file:         # without newline=''  ,it will leave 1 blank space after every row
        writer=csv.writer(file)
        writer.writerow(["SN", "Name", "Contribution"])
        writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
        writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
        writer.writerow([3, "Guido van Rossum", "Python Programming"])


# example to write multple rows at a time
def csv_multiplerow():
    row_list=[["SN", "Name", "Contribution"],
              [1, "Linus Torvalds", "Linux Kernel"],
              [2, "Tim Berners-Lee", "World Wide Web"],
              [3, "Guido van Rossum", "Python Programming"]]

    with open('day 17/innovators.csv','w',newline='') as file:     # with newline='' ,it will create file as we want
        writer=csv.writer(file)
        writer.writerows(row_list)


# example to write file in pipe delimiter

def csv_pipedelimiter():
    row_list=[["SN", "Name", "Contribution"],
              [1, "Linus Torvalds", "Linux Kernel"],
              [2, "Tim Berners-Lee", "World Wide Web"],
              [3, "Guido van Rossum", "Python Programming"]]

    with open('day 17/innovators.csv','w',newline='') as file:

        writing=csv.writer(file,delimiter='|')
        writing.writerows(row_list)


# now we will do example to write csv which will quote only non numeric,which means numeric will be treated as float or int

def csv_quotes():
    row_list=[["SN", "Name", "Contribution"],
                  [1, "Linus Torvalds", "Linux Kernel"],
                  [2, "Tim Berners-Lee", "World Wide Web"],
                  [3, "Guido van Rossum", "Python Programming"]]

    with open('day 17/innovators.csv','w',newline='') as file:

        writing=csv.writer(file,delimiter=';',quoting=csv.QUOTE_NONNUMERIC)
        writing.writerows(row_list)


#now we will learn example of custom quoting

def csv_customquote():
     row_list=[["SN", "Name", "Contribution"],
                   [1, "Linus Torvalds", "Linux Kernel"],
                   [2, "Tim Berners-Lee", "World Wide Web"],
                   [3, "Guido van Rossum", "Python Programming"]]

     with open('day 17/innovators.csv','w',newline='') as file:

         writing=csv.writer(file,quoting=csv.QUOTE_NONNUMERIC,
                            delimiter=';',quotechar='*')

         writing.writerows(row_list)


# in this writing also we can also use dialect 

# now we learn to write using dict

def csv_dictwrite():

    with open('day 17/rating.csv','w',newline='') as file:
        fieldnames=['player name','rating']
        writing=csv.DictWriter(file,fieldnames=fieldnames)

        writing.writeheader()
        writing.writerow({'player name':'kais','rating':2000})
        writing.writerow({'player name':'qais','rating':3000})

csv_dictwrite()





