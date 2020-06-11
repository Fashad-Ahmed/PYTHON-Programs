import datetime
import pytz

# today = datetime.date.today()         #OBJECT
# print(today)
# bday = datetime.date(2001,7,20)  # no 07 only
# print(bday) ; print(repr(bday))         # dbay and today is object not a string
# days_of_mine = (today - bday).days
# print(days_of_mine)
# tdelta = datetime.timedelta(days=10)
# print(tdelta + today)
# print(today.month) ; print(today.weekday()) ; print(today.year) ; print(today.ctime()) # monday = 0 sunday = 6
# print(datetime.time(7,20,5,36))
# hour_delta = datetime.timedelta(hours=10)
# print(datetime.datetime.now() + hour_delta)                                  # delta pichle se connection k liye
#
# datetime_today = datetime.datetime.now(tz=pytz.UTC)
# datetime_pacific = datetime_today.astimezone(pytz.timezone("US/Pacific")) # this aint working
# print(datetime_pacific)
#
# for itz in pytz.all_timezones:
#     print(itz)
#
#
# # string fomatting with dates
# # 2019-03-09  -----> March 09, 2019
# # strft
# )
# print(datetime_pacific.strftime("%B %d, %Y")

# from above one to (2019,09,3)
# strpt

# datetime_thingg = datetime.datetime.strptime(" March 09,2019"," %B %d, %Y")
# print(datetime_thingg)

'''  Maya datetime module usage  '''

now = maya.now
print(now)