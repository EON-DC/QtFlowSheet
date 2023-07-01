import datetime

date_a = datetime.datetime.strptime('01-01 01:00', '%m-%d %H:%M')
date_b = datetime.datetime.strptime('01-01 01:00', '%m-%d %H:%M')

print(date_a == date_b)
