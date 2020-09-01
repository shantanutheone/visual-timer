#Files importing
import timer
import csvWriter
import picker

while(True):
    # New thing [Using pip install pick && pip install windows-curse]
    Topic = picker.picker()
    
    SubTopic = input("Enter SubTopic: ")

    #Gathering Info
    #=============================================================
    TopicInfo = {
        "Topic": Topic,
        "SubTopic": SubTopic,
    }
    timer.timer(TopicInfo,0,60) #Now only call this




