import pandas as pd
import folium as fm
import numpy as np

jan = pd.read_csv("January.csv")
feb = pd.read_csv("February.csv")
mar = pd.read_csv("March.csv")
apr = pd.read_csv("April.csv")
may = pd.read_csv("May.csv")
jun = pd.read_csv("June.csv")
jul = pd.read_csv("July.csv")
aug = pd.read_csv("August.csv")
sep = pd.read_csv("September.csv")
oct = pd.read_csv("October.csv")
nov = pd.read_csv("November.csv")
dec = pd.read_csv("December.csv")

combined = pd.concat([jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec])

print(combined.tail(3))