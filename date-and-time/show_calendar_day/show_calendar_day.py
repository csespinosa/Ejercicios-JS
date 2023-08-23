import calendar

def show_calendar_day(date: str):
    dates = date.split(" ")
    month = int(dates[0])
    day = int(dates[1])
    year = int(dates[2])
    weekday = calendar.weekday(month=month, day=day, year=year)
    return calendar.day_name[weekday].upper()

print(show_calendar_day("08 05 2015"))