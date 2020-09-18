import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from pick import pick
from matplotlib import style
import webbrowser
import random
import numpy as np
from math import e
import os

style.use("seaborn")

BarColorDatewise = pd.read_csv("./database/timeColor.csv")

monthAbbreviation = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}


# Retriving color database and making colorDict for further use
color = pd.read_csv("./database/color.csv")
colorDict = dict()
for i in range(len(color)):
    colorDict[color.loc[i]["Topic"]] = color.loc[i]["Color"]



df = pd.read_csv("./database/result.csv",parse_dates=["startDate"])

df["Duration"] = df["Hour"] * 60 + df["Minute"]



def overAllBarChart():
    Grouped = df.groupby(["Topic"]).sum().reset_index()
    Grouped = Grouped[Grouped["Topic"].isin(color[color["Color"]!="#808080"]["Topic"])]
    fig, ax = plt.subplots()
    barplot= ax.bar(Grouped["Topic"],Grouped["Duration"])
    plt.subplots_adjust(left= 0.09,bottom= 0.11,right = 0.97,top = 0.91)
    # to put it into the upper left corner for example:
    # mngr.window.showMaximized()  # (50,100,640, 545)
    #Setting the color coding matched
    for i in range(len(Grouped)):
        setColor = colorDict[Grouped.iloc[i]["Topic"]]
        barplot[i].set_color(setColor)
    # Working on texts in plot
    # plt.xticks(rotation = '45')
    for i,h,dur, m in zip(range(len(Grouped["Hour"])),Grouped["Hour"],Grouped["Duration"],Grouped["Minute"]):
        if(m%60 < 10):
            min = "0" + str(m%60)
        else:
            min = str(m%60)
        plt.text(i,dur+20,str(str(h + m//60) +":" +min),ha = 'center',color='green',fontsize = 20,fontweight='bold')
    
    plt.title("TopicWise",fontsize = 40,fontweight = 800,family = "monospace")
    plt.xlabel("TOPIC", fontsize = 20, color = "r")
    plt.xticks(fontsize = 15,rotation = "45")
    plt.ylabel("HOURS", fontsize = 20, color = "g")
    plt.yticks(fontsize = 8)

    maxTick = max(ax.get_yticks().tolist())
    plt.yticks(ticks = np.arange(60,maxTick,60), labels = '-')# "np.arange(1,int(maxTick//60))"""
    plt.savefig("html/TopicWise.png", dpi = 100, bbox_inches = "tight")
    # plt.show()
    plt.clf()

def overAllPieChart():
    df1 = df[["Topic","Duration"]]
    Grouped = df1.groupby(["Topic"]).sum().reset_index()
    Grouped = Grouped[Grouped["Topic"].isin(color[color["Color"]!="#808080"]["Topic"])]
    plt.subplots_adjust(left= 0.36,bottom= 0.17,right = 0.57,top = 0.85)
    #Setting up correct color for every topic
    pie_wedge_collection = plt.pie(Grouped["Duration"], labels=Grouped["Topic"],radius = 4,autopct="%1.2f%%") #Making color that we want
    
    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor('white')
        pie_wedge.set_facecolor(colorDict[pie_wedge.get_label()])
    plt.savefig('html/pie.png', dpi = 100,bbox_inches = "tight")
    # plt.show()
    plt.clf()

def datewiseBarChart(week = False):
    Datewise = df.groupby(["startDate"]).sum().reset_index()
    Datewise["labelDate"] = [str(i).split(" ")[0].split("-")[-1] +" " + monthAbbreviation[str(i).split(" ")[0].split("-")[-2]] for i in Datewise["startDate"]]
    fig , ax = plt.subplots()
    # For week = True
    if(week):
        Datewise = Datewise.tail(7)
    barplot = ax.bar(Datewise["startDate"], Datewise["Duration"],tick_label = Datewise["labelDate"])
    for i in range(len(Datewise)):
        setColor = BarColorDatewise.iloc[int(Datewise.iloc[i]["Duration"]//60)]["CodeforcesColor"]
        barplot[i].set_color(setColor)
    # for p in ax.patches:
    #     ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    if(not week):
        for p in ax.patches:
            dur = p.get_height()
            hour = str(dur//60)
            min = dur%60
            if(min<10):
                min = "0" + str(min)
            else:
                min = str(min)
            ax.annotate(hour + ":" + min,(p.get_x()+p.get_width()/2., p.get_height()),ha='center', va='center', xytext=(0, 10),color='green',fontsize = 5,fontweight='bold',textcoords='offset points')
    else:
        for p in ax.patches:
            dur = p.get_height()
            hour = str(dur//60)
            min = dur%60
            if(min<10):
                min = "0" + str(min)
            else:
                min = str(min)
            ax.annotate(hour + ":" + min,(p.get_x()+p.get_width()/2., p.get_height()),ha='center', va='center', xytext=(0, 10),color='green',fontsize = 20,fontweight='bold',textcoords='offset points')


    plt.yticks(ticks=[60,120,180,240,300,360,420,480,540,600,660,720,780,840,900],labels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], color = "g")
    plt.xlabel("DATE",fontsize = 20,color = "red")
    plt.ylabel("HOURS",fontsize = 20,color = "green")
    if(week):
        plt.xticks(rotation = "90",color = "r",fontsize=  15)
        plt.subplots_adjust(left= 0.07,bottom= 0.16,right = 0.87,top = 0.89)
        plt.title("This Week", fontsize = 40,fontweight = 900,family = "monospace")
        plt.savefig("html/weekDateWise.png",dpi = 100,bbox_inches = "tight")
    else:
        plt.xticks(rotation = "90",color = "r",fontsize = 6)
        plt.subplots_adjust(left= 0.11,bottom= 0.13,right = 0.99,top = 0.90)
        plt.title("Overall", fontsize = 40,fontweight = 900,family = "monospace")
        plt.savefig("html/DateWise.png",dpi = 180,bbox_inches = "tight")
    plt.clf()


def stackedBarPlot(overAll = True):
    df["startDate"] = [str(i).split(" ")[0].split("-")[-1] +" " + monthAbbreviation[str(i).split(" ")[0].split("-")[-2]] for i in df["startDate"]]
    Datewise = df.groupby(["startDate"])
    Topics = []
    if(overAll):
        for i in range(len(color["Topic"])):
            Topics.append(color["Topic"][i])
    else:
        for i in range(len(color["Topic"])):
            if(colorDict[color["Topic"][i]] != "#808080"):
                Topics.append(color["Topic"][i])
    _init = pd.DataFrame(df["startDate"].unique(),columns=["startDate"]).set_index("startDate")
    for i in Topics:
        _init[i] = 0
    for date in df["startDate"].unique():
        date_then_topic_group = Datewise.get_group(date).groupby("Topic").sum().reset_index()
        for top, dur in zip(date_then_topic_group["Topic"], date_then_topic_group["Duration"]):
            _init.loc[date][top] = dur
    
    if(overAll):
        my_colors = color["Color"]
        ax = _init.plot(kind='bar', stacked=True, figsize=(18.5, 10.5), color = my_colors,title = "OVERALL DateWISE then TopicWISE")

        fig = ax.get_figure()
        fig.savefig("html/stackedBarPlot_overall.png",dpi = 80, bbox_inches = "tight")
    else:
        my_colors = []
        for i in Topics:
            my_colors.append(colorDict[i])
        ax = _init.plot(kind='bar', stacked=True, figsize=(18.5, 10.5), color = my_colors, title = "Selected DateWISE then TopicWISE",)
        fig = ax.get_figure()
        fig.savefig("html/stackedBarPlot_real.png",dpi = 100, bbox_inches = "tight")
    plt.clf()

def challenge():
    df = pd.read_csv("database/result.csv",parse_dates=["startDate"])
    df["Duration"] = df["Hour"] * 60 + df["Minute"]
    Datewise = df.groupby(["startDate"]).sum().reset_index()

    Datewise["labelDate"] =  [str(i).split(" ")[0].split("-")[-1] +" " + monthAbbreviation[str(i).split(" ")[0].split("-")[-2]] for i in Datewise["startDate"]]
    
    Datewise = Datewise[["labelDate", "Duration"]]

    Datewise["Change"] = Datewise["Duration"] - 300

    Datewise["Changeby60"] = Datewise["Change"]/60

    Datewise["ePowerChangeby60"] = e**Datewise["Changeby60"]

    Datewise["ePowerChangeby60"] = [e**i if i>0 else -e**(-i) for i in Datewise["Changeby60"]] 

    L = Datewise["ePowerChangeby60"].tolist()
    
    Version = []
    _ver = 0.0
    for i in range(len(L)):
        if(i>2):
            lastThree = L[i-1]+L[i-2]+L[i-3]
            _ver += (L[i]*2)/100 + (lastThree)/100
            Version.append(_ver/100)
        else:
            _ver += (L[i]*2)/100
            Version.append(_ver/100)
    print("==VERSION==")
    print("Previous : ","{:.3f}".format(Version[-2]))
    print("Gained :","{:.3f}".format(Version[-1]-Version[-2]))
    print("Current:","{:.3f}".format(Version[-1]))

    plt.plot(Datewise["labelDate"],Version,"X:m")
    plt.xlabel("DATE",fontsize = 20,color = "red")
    plt.ylabel("VERSION",fontsize = 20,color = "green")
    plt.xticks(rotation = "vertical",color = "r",fontsize = 12)
    plt.yticks(fontsize = 13)
    plt.title("Version", fontsize = 40,fontweight = 900,family = "monospace")
    plt.savefig("html/Version.png",dpi = 90,bbox_inches = "tight")
    plt.clf()
def totalTime():
    print("==DURATION==")
    print(f"Total: {df['Duration'].sum()//60} hours {df['Duration'].sum()%60} minutes")
    Datewise = df.groupby(["startDate"]).sum().reset_index()
    TodaysDuration = Datewise.iloc[-1]["Duration"]
    print(f"Today : {int(TodaysDuration//60)} hours {TodaysDuration%60} minutes")
    print()


def html():
    url = "file://" + "C://Users/hp/desktop/visual-timer/html/stats.html"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

    
totalTime()
overAllBarChart()
overAllPieChart()
datewiseBarChart()
datewiseBarChart(week = True)

stackedBarPlot(overAll=False)
challenge()
html()

