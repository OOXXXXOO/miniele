import datetime

ymd = datetime.datetime.now().strftime('%Y-%m-%d')
print(ymd)

add_hour=datetime.datetime.now()+datetime.timedelta(hours=1)
