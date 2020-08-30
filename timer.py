import time
from playsound import playsound
from datetime import datetime

def timer(counter,interval = 5):
    print(f"Playing {counter} beeps at the interval of {interval}")
    startTime = datetime.now()
    for i in range(counter,0,-1):
        time.sleep(interval)  # Sleep here for interval sec
        playsound(f"./numbers-mp3/{i}.mp3") # Playing the remaining time
    endTime = datetime.now()
    
    
    Delta = endTime - startTime # datetime.timedelta(seconds=15, microseconds=750128)
    hour = Delta.seconds // 3600
    minutes = (Delta.seconds // 60) % 60    
    Duration = f"{hour}:{minutes}"
    TimeInfo = {
        "startDate": startTime.strftime("%d %b %Y"),
        "endDate": endTime.strftime("%d %b %Y"),
        "startTime": startTime.strftime("%I:%M %p"),
        "endTime": endTime.strftime("%I:%M %p"),
        "Duration": Duration
    }
    return TimeInfo