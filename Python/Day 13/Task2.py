import os 
 
print(os.listdir())    # it will list all the directories inside the folder of Quant-Journey


print(os.listdir('Puzzles'))      # it will list the sub directories which means directories inside 'Puzzles'

# we can also run loop here

for item in os.listdir('month-01-python'):
    if item.endswith('.ipynb'):
        print(item)



# To create a folder
##   os.mkdir('testing to create directory')

# # creates nested + no error if exists, the below code will work fine if the folder already exist and it will not show error

os.makedirs('testing to create directory',exist_ok=True)

# to create a file
code="print('Hello World')"

with open('month-01-python/Day 13/Task3.py','w') as f:
    f.write(code)
