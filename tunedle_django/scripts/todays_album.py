from datetime import datetime


def getDate():
    current_date = datetime.date.now()
    print("Original date and time object:", current_date)
    
    # Retrieving each component of the date
    # i.e year,month,day,hour,minute,second and
    # Multiplying with multiples of 100
    # year - 10000000000
    # month - 100000000
    # day - 1000000
    print("Date and Time in Integer Format:",
        current_date.year*10000000000 +
        current_date.month * 100000000 +
        current_date.day * 1000000)