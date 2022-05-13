f = open('today.txt', 'r')
today_string = f.read()
f.close()

import time 
fmt = "%Y-%m-%d"
now = time.strptime(today_string, fmt)
print(time.strftime('%d', now))

from datetime import date

birthday = date(2000, 3, 29)

from datetime import timedelta
party_day = birthday + timedelta(days=10000)
print(party_day)