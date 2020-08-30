from pick import pick
import pandas as pd

def picker():
    df = pd.read_csv("result.csv")
    Topics = list(set(df["Topic"]))
    Topics.append("==Create New Topic==")
    Title = "Select one of them or create one : "
    Picked,option = pick(Topics, Title)
    if(option == len(Topics) - 1):
        # Request of creating new Topic
        print("You've requested to create new topic")
        Topic = input("Enter New Topic : ")
        return Topic
    else:
        # Picking from old topics
        return Picked



