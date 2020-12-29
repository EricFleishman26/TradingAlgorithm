import datetime


def get_hour():
    time = datetime.datetime.now()
    hour = int(time.strftime("%H"))
    return hour


def get_minute():
    time = datetime.datetime.now()
    minute = int(time.strftime("%M"))
    return minute


def time_control():
    hour = get_hour()
    minute = get_minute()
    if hour >= 15:
        if minute >= 30:
            return False
    else:
        return True
