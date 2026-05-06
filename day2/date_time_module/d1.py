import datetime
from datetime import timedelta,tzinfo

#date class, today method gives the current date
d=datetime.date.today()
print(d)
print(d.year)
print(d.month)
print(d.day)

#weekday name in short
print("weekday name in short = ",d.strftime("%a"))
#weekday name in full
print("weekday name in full = ", d.strftime("%A"))
print("weekday as a number = ",d.strftime("%w"))

#same for month name
print(d.strftime("%b"))
print(d.strftime("%B"))



#datetime class, now method gives the current date with time
d2=datetime.datetime.now()
print(d2)

#crete custom date
d3=datetime.date(2026,6,6)
print(d3)

#crete custom time
d4=datetime.time(12,27)
print(d4)

#format date
today=datetime.datetime.now()
print(today.strftime("%d/%m/%y"))

delta = timedelta(days=2, hours=5, minutes=30)
print(delta)

#timedelta: duration - diff btw two dates and times
new_day=today+timedelta(days=5)
print(new_day)

new_time=today+timedelta(hours=5)
print(new_time)

new_week=today+timedelta(weeks=4)
print(new_week)

new_min=today-timedelta(minutes=10)
print(new_min)

