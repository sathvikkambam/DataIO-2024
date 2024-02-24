import pandas as pd
import folium as fm
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import time

time_diff = pd.read_csv("time_diff.csv")

time_diff = time_diff.loc[:, '0']

dur_min = time_diff.divide(60)

print(dur_min.mean())

plt.figure()

print(list(dur_min < 40000).index(False))

dur_min = dur_min[(dur_min < 180)]
dur_min = dur_min[(dur_min > 0)]
dur_min.plot.hist(bins=100)

plt.title("Amount of time bikers rent")
plt.xlabel("Minutes rented")


plt.show()