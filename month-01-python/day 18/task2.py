# lets learn about error and exceptions

try:
    num=int(input('Enter the number:'))
    assert num%2==0                     # asssert checks and return if the number is even or not,if not even then except is executed

except:
    print('Not an even number')

else:                                # if we pass even number i.e if try block works then else will be executed
    reciprocal=1/num
    print(reciprocal)

finally:
    print('This will execute,no matter what')