import pandas as pd 
import csv 
import plotly.express as px
import numpy as np
df = pd.read_csv("final_gravity.csv")

masses = df["Star_Mass"].tolist()
radiuses = df["Star_Radiuses"].tolist()
gravity = df["Star_Gravity"].tolist()
for i , data in enumerate(masses):
    masses[i] = float(data)/1.989e+30
for i , data in enumerate(radiuses):
    radiuses[i] = float(data)/6.957e+8

fig  = px.scatter(df , x =  "Star_Radiuses", y = "Star_Mass" , title = "Radius Vs Mass graph")
fig.show()
fig2  = px.scatter(df , x =  "Star_Mass", y = "Star_Gravity" , title = "Radius Vs Mass graph")
fig2.show()