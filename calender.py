import calendar




print(calendar.weekheader(2))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2021,2,5))
print(calendar.monthcalendar(2021,2))
print(calendar.calendar(2021))
day_of_today=calendar.weekday(2022,2,23)
print(day_of_today)
is_leap=calendar.isleap(2024)
print(is_leap)
how_many_leap_days=calendar.leapdays(1,10000)
print(how_many_leap_days)

