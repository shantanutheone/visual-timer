from pick import pick
import pandas as pd
from datetime import datetime

df = pd.read_csv("./database/result.csv")
df["Duration"] = df["Hour"]*60 + df["Minute"]

def todays_data():
    todays_date = datetime.today().strftime("%d %b %Y")

    print(todays_date)
    df1 = df[df["startDate"] == todays_date].reset_index()
    sum_df = df1.groupby(['Topic','SubTopic']).agg({'Duration': 'sum'})
    X = sum(sum_df["Duration"])
    print(int(X//60)," Hours", X%60," Minutes")
    print("-----More Details----(Press Enter)")
    _ = input()
    if(_ == ""):
        print(sum_df)

title = "==Choose One of the following features=="

options = ["Today's Data"]

option, index = pick(options, title)

if(index == 0):
    todays_data()

