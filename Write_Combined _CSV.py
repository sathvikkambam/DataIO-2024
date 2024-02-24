import pandas as pd
import folium as fm
import numpy as np
import datetime as dt

# jan = pd.read_csv("January.csv")
# feb = pd.read_csv("February.csv")
# mar = pd.read_csv("March.csv")
# apr = pd.read_csv("April.csv")
# may = pd.read_csv("May.csv")
# jun = pd.read_csv("June.csv")
# jul = pd.read_csv("July.csv")
# aug = pd.read_csv("August.csv")
# sep = pd.read_csv("September.csv")
# oct = pd.read_csv("October.csv")
# nov = pd.read_csv("November.csv")
# dec = pd.read_csv("December.csv")

combined = pd.read_csv("combined.csv")

print(combined.iloc[5155806])

started = combined.loc[:,'started_at']
ended = combined.loc[:,'ended_at']

dt_format = '%Y-%m-%d %H:%M:%S'

started = started.apply(dt.datetime.fromisoformat)
ended = ended.apply(dt.datetime.fromisoformat)

diff = ended.sub(started)

diff = diff.apply(dt.timedelta.total_seconds)

diff.to_csv("time_diff.csv")

