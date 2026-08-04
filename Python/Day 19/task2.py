import datetime as dt
import pytz
def datetime_to_string():
    current_datetime=dt.datetime.now()

    customize=current_datetime.strftime('%a,%#d,%b,%I %p')      # %-d == %#d

    print(customize)


def string_to_datetime():
    datetime='20 June,2026'

    customize=dt.datetime.strptime(datetime,'%d %B,%Y')     # strptime function is used for string to datetime conversion

    print(customize)



def datetime_timedelta():
    datetime1=dt.timedelta(weeks=2,days=3,hours=2)
    datetime2=dt.timedelta(days=10,hours=5,minutes=10)

    delta=datetime1-datetime2

    print(delta)




def learning_strftime():

    from datetime import datetime

    # current date and time
    now = datetime.now()

    t = now.strftime("%H:%M:%S")
    print("Time:", t)

    s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
    # mm/dd/YY H:M:S format
    print("s1:", s1)

    s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
    # dd/mm/YY H:M:S format
    print("s2:", s2)
    
    s3=now.strftime('%c')          # %c will print the local time date for eg 'Thu Jul 30 08:27:09 2026'
    print('s3',s3)                  # %x and %X are also more useful so we can use this as well


learning_strftime()

def learning_timezone():

    local=dt.datetime.now()
    print('Local',local.strftime('%d/%m/%Y,%H:%M:%S'))


    tz_NY=pytz.timezone('America/New_York')   # it has timezone data
    datetime_NY=dt.datetime.now(tz_NY)
    print('New York',datetime_NY.strftime('%d/%m/%Y,%H:%M:%S'))

    tz_london=pytz.timezone('Europe/London')
    datetime_London=dt.datetime.now(tz_london)
    print('London',datetime_London.strftime('%d/%m/%Y,%H:%M:%S'))

