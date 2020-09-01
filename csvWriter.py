import csv
import time
import pandas as pd

def csvWriter(Info): # Writing in a CSV file
    with open("./database/result.csv", "a+") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([Info["Topic"], Info["SubTopic"], Info["startDate"], Info["startTime"], Info["endTime"], Info["Hour"], Info["Minute"]])



    