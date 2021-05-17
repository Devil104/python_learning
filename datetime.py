import datetime
import Maya


today=datetime.date.today()
print(today)

birthday=datetime.date(1994,6,19)
print(birthday)

days_since_birth=(today-birthday).days
print(days_since_birth)

increase_date=datetime.timedelta(days=10)
print(today + increase_date)

print(datetime.time(7,40,35,45))

print(datetime.datetime.now())
hours_delta=datetime.timedelta(hours=20)
print(datetime.datetime.now() + hours_delta)

N=maya.MayaDT.from_datetime(datetime.now())
print(N)
