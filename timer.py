import time
from playsound import playsound
from datetime import datetime
import csvWriter
import pandas as pd

def databaseCheckpoint(startTime):
    df = pd.read_csv("./database/result.csv")
    lastRow = df.iloc[len(df) - 1].copy()
    endTime = datetime.now()
    #Change its [endDate, endTime, Hour, Minute,]
    # lastRow["endDate"] = endTime.strftime("%d %b %Y")
    lastRow["endTime"] = endTime.strftime("%I:%M %p")
    Delta = endTime - startTime # datetime.timedelta(seconds=15, microseconds=750128)
    Hour = Delta.seconds // 3600
    Minute = (Delta.seconds // 60) % 60 
    lastRow["Hour"] = Hour
    lastRow["Minute"] = Minute
    df.loc[len(df) - 1]  = lastRow
    df.to_csv("./database/result.csv", index = False)

def databaseInitialWriting(startTime,TopicInfo):    
    TimeInfo = {
        "startDate": startTime.strftime("%d %b %Y"),
        "endDate": startTime.strftime("%d %b %Y"),
        "startTime": startTime.strftime("%I:%M %p"),
        "endTime": startTime.strftime("%I:%M %p"),
        "Hour": 0,
        "Minute": 0
    }
    Info = {**TopicInfo, **TimeInfo}
    csvWriter.csvWriter(Info)
def timer(TopicInfo,counter,interval):
    if(counter == 0):
        amount = "INFINITE"
        counter = 300
    else:
        amount = counter
    print(f"Playing {amount} beeps at the interval of {interval}")
    startTime = datetime.now()

    #Logic for playing correct sound at each interval
    #==============================================================
    databaseInitialWriting(startTime,TopicInfo)
    for i in range(1, counter+1):
        time.sleep(interval)  # Sleep here for interval sec
        if(i%5!=0): # 1 2 3 4 
            print("+1")
        elif(i%60==0): # 1 hour 2 hour 3 hour
            playsound(f"./sounds/{i}.mp3")
            databaseCheckpoint(startTime)
            print(f"Checkpoint Created : {i//60} hours : {i%60} minutes")
        else:
            if(i%10==0):
                playsound(f"./sounds/{i%60}.mp3")
            # Also add here to the database if in case we quit program
            databaseCheckpoint(startTime)
            print(f"Checkpoint Created : {i//60} hours : {i%60} minutes")
