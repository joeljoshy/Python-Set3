#today,tomorrow,yesterday

import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(1)
tomorrow = today + datetime.timedelta(1)
print(f"Yesterday : {yesterday.strftime('%d-%m-%Y')}\nToday : {today.strftime('%d-%m-%Y')}\nTomorrow : {tomorrow.strftime('%d-%m-%Y')}")