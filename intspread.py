# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:50:43 2022

@author: sigma
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np

df=pd.read_excel(r'D:\Stony Brook AMS\AMS 2022 Spring\AMS517\AMS517 project\Paper 6 draft\DBP.xlsx')

sample_timeseries_data ={'Date':df["Date"], 'T5YFF':df["T5YFF"], 'T10Y2Y':df["T10Y2Y"]}

dataframe = pd.DataFrame(
  sample_timeseries_data,columns=[
    'Date', 'T5YFF', 'T10Y2Y'])

dataframe["Date"] = dataframe["Date"].astype("datetime64")
dataframe = dataframe.set_index("Date")
dataframe

x= df["Date"]
y1 =df["T5YFF"]
y2 = df["T10Y2Y"]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y1, 'cornflowerblue')
ax2.plot(x, y2, 'lightgray')

ax1.set_xlabel('Date')
ax1.set_ylabel('T5YFF', color='cornflowerblue')
ax2.set_ylabel('T10Y2Y', color='lightgry')
plt.show()

