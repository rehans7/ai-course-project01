import csv
import numpy as np
instaMinutes=[]
studyMinutes=[]
with open("digital_behaviour.csv", "r",encoding="utf-8") as file:
    reader=csv.DictReader(file)
    for row in list(reader):
        instaMinutes.append(int(row['Instagram_Minutes']))
        studyMinutes.append(int(row['Study_Minutes']))
instaMinutes=instaMinutes[:7]
studyMinutes=studyMinutes[:7]

instaArray=np.array(instaMinutes)
studyArray=np.array(studyMinutes)

