import time

def learning_sleep():
    x=float(input("Enter the sleep interval:"))
    print("This will print immediately")
    time.sleep(x)
    print(f'It will print after {x} seconds.')


def creating_digitalclock():

    while True:
        now=time.localtime()
        format_time=time.strftime('%I:%M:%S %p',now)
        print(format_time)
        time.sleep(1)

def time_functions():
    print(time.time())  # it prints the time in timestamp
    print(time.ctime(4423479439))   # converts epoch to date
    print(time.localtime())     # it prints 9 tuple elements according to local time
    print(time.gmtime())           #it prints the 9 tuple elements according to UTC
    print(time.mktime((2022, 12, 28, 8, 44, 4, 4, 362, 0)))     # it takes the struct_ time and returns epoch in local time
    print(time.asctime((2022, 12, 28, 8, 44, 4, 4, 362, 0)))    # it prints it in date format

time_functions()
