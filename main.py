  
  
import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]
del df["Mass"]
del df["Radius"]
del df["Distance"]
del df["Star"]
del df["Star_name"]



df = df.rename({
                'Mass': "Mass", 
                'Radius': "Radius", 
                'Distance': "Distance", 
            }, axis='columns')

df.to_csv('main.csv') 