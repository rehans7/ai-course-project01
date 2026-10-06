import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv
import pandas as pd


df=pd.read_csv("digital_behaviour.csv")
day=[f"D{i+1}" for i in range(len(df))]

plt.figure(figsize=(32,12))
plt.bar(day,df["Total_Screen_Time"],color="Green")
plt.title("My Screen Time By Day")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.savefig("charts/img1.png",dpi=1000)
plt.close()

plt.figure(figsize=(4,10))
appMinutes=[]
appMinutes.append(df["Instagram_Minutes"].sum())
appMinutes.append(df["YouTube_Minutes"].sum())
appMinutes.append(df["WhatsApp_Minutes"].sum())
appMinutes.append(df["LinkedIn_Minutes"].sum())
apps=["Instagram","YouTube","WhatsApp","LinkedIn"]
plt.bar(apps,appMinutes,color="Blue")
plt.title("Total Time By App")
plt.xlabel("Apps")
plt.ylabel("Minutes")
plt.savefig("charts/img2.png",dpi=1000)
plt.close()

plt.figure(figsize=(30,10))
plt.plot(day,df["Total_Screen_Time"],marker="o",label="Screen Time",color="Green")
plt.plot(day,df["Study_Minutes"],marker="x",label="Study Time",color="Blue")
plt.title("Line Graph")
plt.xlabel("Days")
plt.ylabel("Minutes")
plt.xticks(rotation=45)
plt.legend()
plt.savefig("charts/img3.png",dpi=1000)
plt.close()

plt.figure(figsize=(30,10))
plt.plot(day,df["Total_Screen_Time"],marker="o",label="Screen Time",color="Green")
plt.plot(day,df["Study_Minutes"],marker="x",label="Study Time",color="Blue")
plt.title("Line Graph")
plt.xlabel("Days")
plt.ylabel("Minutes")
plt.xticks(rotation=45)
plt.legend()
plt.savefig("charts/img3.png",dpi=1000)
plt.close()

plt.figure(figsize=(7,7))
plt.pie(appMinutes,labels=apps,colors=["Green","Pink","Blue","Yellow"],autopct="%1.1f%%",startangle=90)
plt.title("Pie Chart")
plt.legend()
plt.savefig("charts/img4.png",dpi=1000)
plt.close()
plt.show()


