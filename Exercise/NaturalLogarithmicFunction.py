# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:15:03 2023

@author: Somayeh
"""

import math
import numpy as np
import pandas as pd


log_dic = {'x':[], 'logx':[]}
for i in np.arange(0.01,100,0.01):
    log_dic["x"].append(i)
    log_dic["logx"].append(math.log(i))


log_df = pd.DataFrame(log_dic) 
#log_df.to_csv("nutralLogarithm.csv")
