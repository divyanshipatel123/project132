import pandas as pd 
import csv 
import plotly.express as px
import numpy as np
df = pd.read_csv("final_gravity.csv")

fig  = px.scatter(df , x =  "Star_Radiuses", y = "Star_Mass" , title = "Radius Vs Mass graph")
fig.show()
fig2  = px.scatter(df , x =  "Star_Mass", y = "Star_Gravity" , title = "Radius Vs Mass graph")
fig2.show()