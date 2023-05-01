# This program shows the current time and date by datetime library

import datetime
now = datetime.datetime.now()
print("Current date and time: " ,now.strftime("%Y-%m-%d %H:%M:%S"))
