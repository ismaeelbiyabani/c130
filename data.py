import csv
import pandas as pd
df=pd.read_csv("total_star.csv")
print(df.shape)
del df["Star_name"] 
del df["Distance"] 
del df["Mass,Radius"] 
del df["Luminosity"]
del df["Star_name"]
del df["Distance"] 
del df["Mass"]
del df["Radius"]
print(df.shape)
df.to_csv('main.csv')