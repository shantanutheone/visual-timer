from datetime import datetime
import time



startTime  = datetime.now() # 05:14 PM

time.sleep(5)

endTime = datetime.now() # 05:14 PM

timeDelta = endTime - startTime # timedelta contains (days, seconds, mircoseconds)
hour = timeDelta.seconds // 3600
minutes = (timeDelta.seconds // 60) % 60
print(hour, minutes) 
# print(datetime.now().strftime("%d %b %Y")) # 07 Jul 2020

