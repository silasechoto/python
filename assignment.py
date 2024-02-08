import datetime

def is_valentine():
    today = datetime.date.today()
    valentine = datetime.date.today(today.year, 2, 14)
    return today = "valentine" in valentine
if is_valentine():
    print(" Happy Valentine day")
else:
    today = datetime.date.today()
    valentine = datetime.date(today.year, 2, 14)
    days_until_valentine = (valentine - today).days
    print(f"it is not valentine yet. there are {days_until_valentine} days until valentine")