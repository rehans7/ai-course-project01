import csv
import numpy as np
instaMinutes=[]
waMinutes=[]
studyMinutes=[]
ytMinutes=[]
with open("digital_behaviour.csv", "r",encoding="utf-8") as file:
    reader=csv.DictReader(file)
    for row in list(reader):
        instaMinutes.append(int(row['Instagram_Minutes']))
        studyMinutes.append(int(row['Study_Minutes']))
        waMinutes.append(int(row['WhatsApp_Minutes']))
        ytMinutes.append(int(row['YouTube_Minutes']))
instaMinutes=instaMinutes[:7]
studyMinutes=studyMinutes[:7]

instaArray=np.array(instaMinutes)
studyArray=np.array(studyMinutes)
total= instaArray.sum()
average=instaArray.mean()
maxi=instaArray.max()
mini=instaArray.min()

print("===============Instagram==================")
a=instaArray[0]
b=instaArray[-1]#vector
c=instaArray[:3]#slicing
d=instaArray[-2:]
e=instaArray[1:4]

diff=instaArray-studyArray#subtracts each element of insta array from study array

hours=instaArray/60#dividesEveryElement

greater_than_100=instaArray>100#returns bool array that has true where condition meets

greaterArraythan100=instaArray[instaArray>100]#gives array of only values >100

greaterArraythanAvg=instaArray[instaArray>average]#gives array of only values >avg

countmorethan100=(instaArray>100).sum()#s true means one add 1 where ever condition is true

print(f'Difference between Instagram & study Time : {diff}\nInstagram time in hours :{hours}\nValues >Average :{greaterArraythanAvg}')


#Youtube
print("===============YouTube===============")
ytMinutes=ytMinutes[:7]
ytArray=np.array(ytMinutes)
diff=ytArray-studyArray
hours=ytArray/60
greaterArraythanAvg=ytArray[ytArray>average]
print(f'Difference between YouTube & study Time : {diff}\nInstagram time in hours :{hours}\nValues >Average :{greaterArraythanAvg}')

#WhatsApp
print("===============WhatsApp===============")
waMinutes=waMinutes[:7]
waArray=np.array(waMinutes)
diff=waArray-studyArray
hours=waArray/60
greaterArraythanAvg=waArray[waArray>average]
print(f'Difference between YouTube & study Time : {diff}\nInstagram time in hours :{hours}\nValues >Average :{greaterArraythanAvg}')
