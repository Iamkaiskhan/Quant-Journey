# lets learn about error and exceptions
def learning_exception():
    try:
        num=int(input('Enter the number:'))
        assert num%2!=0                     # asssert checks and return our needed answer,if not then except is executed

    except:
        print('Not an even number')

    else:                                # if we pass even number i.e if try block works then else will be executed
        reciprocal=1/num
        print(reciprocal)

    finally:
        print('This will execute,no matter what')




## now lets learn about custom exceptions

class InvalidAge(Exception):
    'Raised when the age is less than 18'
    pass

number=18

try:
    age=int(input("Enter your age:"))
    if age<number:
        raise InvalidAge

    else:
        print("Eligible to vote")

except InvalidAge:
    print('Not eligible for vote')

