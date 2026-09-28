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

#YouTube
print(df["YouTube_Minutes"].sum())
print(df["YouTube_Minutes"].mean())
print(df["YouTube_Minutes"].max())

#WhatsApp
print(df["WhatsApp_Minutes"].sum())
print(df["WhatsApp_Minutes"].mean())
print(df["WhatsApp_Minutes"].max())
