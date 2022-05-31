import time
import datetime

# time.time() return the total of seconds passed sice 1970
# time.sleep(x) pause(sleep) the curent thread for x seconds
t0 = time.time()
time.sleep(1)
tf = time.time() - t0
print(tf)


# datetime.datetime.now() -> returns a string with year-month-day-hour-min-sec-milsec
dt = datetime.datetime.now()
print(dt)
# datetime.datetme returns a obj datetime, so we can call dt.day for exemple
print(f'{dt.day}-{dt.month}-{dt.year}')


# we can pass a timestamp value (in seconds) to datetime.fromtimestamp
dt = datetime.datetime.fromtimestamp(60)
print(f'10.000 seconds after timestamp 1/01/1970: {dt}\ntimestamp from now: {datetime.datetime.fromtimestamp(time.time())}')

# it is possible do boolean comparation over datetime objs
dt1 = datetime.datetime(2020, 10, 31)
dt2 = datetime.datetime(2021, 10, 31)
print(dt1 > dt2)


# timedelta -> obj that represet a duration of time, so we can do arithimetc operation
half_day = datetime.timedelta(hours=12)
day = datetime.timedelta(days=1)
print(f'One day + 12hours = {str(half_day + day)}')

# so we can add 1000 days from now
thousand = datetime.timedelta(days=1000, hours=12, minutes=30)
print(f'Daqui a 1000 dias, 12horas e 30min serah = {datetime.datetime.now() + thousand}')

# we can do this, cause timedelta returs a total of time over the parameters we passed throught it
# so, total_seconds() returns total of seconds from x. Then we can add, sub..
print(f'Mil dias tem: {thousand.total_seconds()} segundos')

# it is possible convert time to a formated string using strftime()
# we can convert string into time through strptime(), but we need specify the format of string (ex: %y/%m/%d)