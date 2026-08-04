
from datetime import datetime
import math

def learning_errorinstrp():
    try:
        date_string = "12/11/2018"
        date_object = datetime.strptime(date_string, "%d %m %Y")

        print("date_object =", date_object)

    except ValueError:
        print("Check the format")

def learning_timestamp():
    from datetime import datetime

    # timestamp is number of seconds since 1970-01-01 
    timestamp = 1545730073

    # convert the timestamp to a datetime object in the local timezone
    dt_object = datetime.fromtimestamp(timestamp)

    # print the datetime object and its type
    print("dt_object =", dt_object)
    print("type(dt_object) =", type(dt_object))


def datetime_to_timestamp():
    from datetime import datetime

    # current date and time
    now = datetime.now()

    # convert from datetime to timestamp
    ts = datetime.timestamp(now)

    print("Timestamp =", ts)

def checking_timedelay():
    
    now1=datetime.now()
    ts1=datetime.timestamp(now1)
    now2=datetime.now()
    ts2=datetime.timestamp(now2)
    print((ts2-ts1)*pow(10,10))