import pandas as pd
df=pd.read_csv("digital_behaviour.csv")
print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.columns)
print(df.describe())
print(df["Instagram_Minutes"].describe())
print(df[["Instagram_Minutes","Study_Minutes"]].describe())
print(df["Instagram_Minutes"].sum())
print(df["Instagram_Minutes"].mean())
print(df["Instagram_Minutes"].max())
print(df[df["Instagram_Minutes"]>100])
print(df[df["Study_Minutes"]>180])
print(df[df["Instagram_Minutes"]>df["Study_Minutes"]])
print(df[df["Instagram_Minutes"]>(df["Instagram_Minutes"].mean())])
print(df.sort_values(by="Instagram_Minutes",ascending=False))
print(df.sort_values(by="Instagram_Minutes",ascending=False).head(5))
print(df.sort_values(by="Study_Minutes",ascending=False).head(5))
df["Total_Screen_Time"]=df["Instagram_Minutes"]+df["YouTube_Minutes"]+df["WhatsApp_Minutes"]+df["LinkedIn_Minutes"]
df["Screen_Hours"]=df["Total_Screen_Time"]/60
df["Digital_Balance"]=df["Study_Minutes"]/df["Total_Screen_Time"]
df["Day_Type"]="Normal"
df.loc[(df["Total_Screen_Time"]>300),"Day_Type"]="Heavy"


df.to_csv("digital_behaviour.csv",index=False)

#1
i,w,l,y=(df["Instagram_Minutes"].sum(),df["WhatsApp_Minutes"].sum(),df["LinkedIn_Minutes"].sum(),df["YouTube_Minutes"].sum())
print(i,w,l,y)

#2
maxi=max([i,w,l,y])
if i==maxi:
    print("Instagram")
elif w==maxi:
    print("WhatsApp")
elif l==maxi:
    print("LinkedIn")
else:
    print("YouTube")


#3
print((df["Day_Type"]=="Heavy").sum())

#4
print(df[df["Study_Minutes"]==(df["Study_Minutes"].max())]["Date"])

#5
print(df[df["Total_Screen_Time"]==(df["Total_Screen_Time"].max())]["Study_Minutes"])



#6
print(df["Digital_Balance"].mean())





#YouTube
print(df["YouTube_Minutes"].sum())
print(df["YouTube_Minutes"].mean())
print(df["YouTube_Minutes"].max())

#WhatsApp
print(df["WhatsApp_Minutes"].sum())
print(df["WhatsApp_Minutes"].mean())
print(df["WhatsApp_Minutes"].max())
