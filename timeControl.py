import datetime

def market_status():
    date_time = datetime.datetime.now()
    hour = int(date_time.strftime("%H"))
    minute = int(date_time.strftime("%M"))
    time = hour + (minute * 0.01)
    day = dayofweek_check()

    if (time >= 9.3 and time < 16.3) and day is True:
        print("Market is Open")
        return True
    else:
        print("Market is Closed")
        return False


def dayofweek_check():
    today = datetime.datetime.today()
    day = today.weekday()

    if day == 5 or day == 6:
        return False
    else:
        return True
