from pick import pick
import pandas as pd
import time
import csvWriter
import csv 

def picker():
    df = pd.read_csv("./database/color.csv")
    Topics = list(df[df["Color"]!="#808080"]["Topic"]) #----WARNING (MAKE BETTER ALGORIGTHM)
    Topics.append("==Create New Topic==")
    Title = "Select one of them or create one : "
    Picked,option = pick(Topics, Title)
    if(Picked == "==Create New Topic=="):
        Picked = input("Enter New Topic: ")
        Color = input("Enter Hexa code for new topic")
        addToColor(Picked, Color)
    return Picked

def addToColor(Picked,Color):
    with open("./database/color.csv", "a+") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([Picked,Color])