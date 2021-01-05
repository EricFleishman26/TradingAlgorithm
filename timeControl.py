import datetime

def market_status():
    date_time = datetime.datetime.now()
    hour = int(date_time.strftime("%H"))
    minute = int(date_time.strftime("%M"))
    time = hour + (minute * 0.01)

    if time >= 9.3 and time < 16.3:
        print("Market is Open")
        return True
    else:
        print("Market is Closed")
        return False
