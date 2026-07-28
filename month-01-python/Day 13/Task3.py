print('Hello World')

import os

print(os.getcwd())
# To rename the directory or file
#os.rename('testing to create directory','test complete')

# # To create a file
# with open(r'C:\Users\HP\Documents\GitHub\Quant-Journey\test complete\test.txt','w') as f:
#     f.write('Hello')




#To delete a file
#os.remove(r'test complete\test.txt')
          
# To delete a empty directory
#os.rmdir('test complete')


# To delete a directory and everything inside

import shutil
def create_directory():
    os.makedirs('directory_test',exist_ok=True)

    with open('directory_test/test.txt','w') as f:
        f.write('This file is going to delete')
    

create_directory()

shutil.rmtree('directory_test')

