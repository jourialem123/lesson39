import datetime
x=datetime.datetime.now()

print("The time now is ",x)
print("Today's date is ",x.strftime("%d"))
print("this month is ",x.strftime("%b"))
print("Current hour is ",x.strftime("%H"))
print("Current minute is ",x.strftime("%M"))
print("Current second is ",x.strftime("%S"))

import calendar

print(calendar.calendar(2025))