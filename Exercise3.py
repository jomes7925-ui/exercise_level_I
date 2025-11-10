# simple python program to display the current date and time
# import datetime

# get current date and time
# now = datetime.datetime.now()

# print("current date and time: ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# ===========Using datetime.today()
# from datetime import datetime

# print("Current date and time: ")
# print(datetime.today())

# ===========Using time module
# import time

# print("Current date and time")
# print(time.strftime("%Y-%m-%d %H:%M%S"))

# ===========Using pytz for timezone-aware time
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Phnom_Penh')
now = datetime.now(tz)

print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M%S"))