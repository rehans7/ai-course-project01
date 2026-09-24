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
total= instaArray.sum()
average=instaArray.mean()
maxi=instaArray.max()
mini=instaArray.min()

instaArray[0]
instaArray[-1]#vector
instaArray[:3]#slicing
instaArray[-2:]
instaArray[1:4]

diff=instaArray-studyArray#subtracts each element of insta array from study array
hours=instaArray/60#dividesEveryElement

greater_than_100=instaArray>100

