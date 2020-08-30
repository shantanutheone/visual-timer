import csv
import time

def csvWriter(Info): # Writing in a CSV file
    with open("result.csv", "a+") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([Info["Topic"], Info["SubTopic"], Info["startDate"], Info["endDate"], Info["startTime"], Info["endTime"], Info["Duration"]])
        print("Writing Successful !!!!  Sleeping for 2 sec")
        time.sleep(2)