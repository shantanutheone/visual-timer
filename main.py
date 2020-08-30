import timer
import csvWriter
import picker
from pick import pick

while(True):
    # New thing [Using pip install pick && pip install windows-curse]
    Topic = picker.picker()
    
    SubTopic = input("Enter SubTopic: ")

    Counter = int(input("Enter the Time (in minutes): "))

    Interval = input("Enter interval: (Enter for default: 60)")

    if(Interval == ""):
        Interval = 60
    else:
        Interval = int(Interval)

    #Gathering Info
    TopicInfo = {
        "Topic": Topic,
        "SubTopic": SubTopic,
    }
    TimeInfo = timer.timer(Counter,Interval)
    Info = {**TopicInfo, **TimeInfo}

    #Writing Into File
    csvWriter.csvWriter(Info)


