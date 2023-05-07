# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 16:11:25 2023

@author: Somayeh
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ln_x = pd.read_csv('E:/Exercise/nutralLogarithm.csv')

x = ln_x['x']

y = ln_x['logx']

delta_x = []
delta_y = []
df_dx = []
d2f_dx = []
delta_df = []
for i in range(1, len(ln_x)-1):
    delta_y.append(y[i+1] - y[i])
    delta_x.append(x[i+1] - x[i])
    df_dx.append(delta_y[i-1]/delta_x[i-1])


plt.plot(x, y, label = "ln")

for i in range(1, len(df_dx)-1):
    delta_df.append(df_dx[i+1] - df_dx[i])
    d2f_dx.append(delta_df[i-1]/delta_x[i-1])

#plt.plot(x[0:len(x)-1], df_dx, label = "1/x")
#plt.plot(x[0:len(x)-2], d2f_dx)"""
"""fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('x')
ax1.set_ylabel('Ln', color=color)
ax1.plot(x, y, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('1/x', color=color)  # we already handled the x-label with ax1
ax2.plot(x[0:len(x)-1], df_dx, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

dr1 = {'fd': [df_dx, 'null'],'sd': [d2f_dx, 'null', 'null']}
drivative = pd.DataFrame(dr1) 
drivative.to_excel("nutralLogarithm1.xlsx")
"""