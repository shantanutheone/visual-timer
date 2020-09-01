# Adding challenge feature

import pandas as pd
import matplotlib.pyplot as plt
from math import e
from matplotlib import style

style.use("seaborn")

df = pd.read_csv("database/result.csv",parse_dates=["startDate"])
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
df["Duration"] = df["Hour"] * 60 + df["Minute"]

Datewise = df.groupby(["startDate"]).sum().reset_index()
Datewise["labelDate"] = [str(i).split(" ")[0].split("-")[-1] +" " + monthAbbreviation[str(i).split(" ")[0].split("-")[-2]] for i in Datewise["startDate"]]

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
for i in Version:
    print("{:.2f}".format(i))
plt.plot(Datewise["labelDate"],Version,"b^")
plt.xticks(rotation = "vertical",color = "r")
plt.title("Version", fontsize = 40,fontweight = 900,family = "monospace")
plt.show()