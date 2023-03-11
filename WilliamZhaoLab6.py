##
# Student Name: William Zhao
# Course: CIS 502 Applied Python Programming
# Lab # 6 - Pandas: DataFrames
# Application: Regulating Temperature
# Description: This program uses basic pandas functions to
#              format and analyze data
# Version: Python 3.9.4
# Solution File: WilliamZhaoLab6.py
# Date: 03/10/23
##

#Source Code
import pandas as pd

temps = {
    'Maxine': [98.6, 96.9, 97.7], 
    'James': [98.9, 100.3, 101.1], 
    'Amanda': [98.5, 98.3, 98.7]
}

temperatures_df = pd.DataFrame(temps, index=["Morning", "Afternoon", "Evening"])
temperatures_df["Maxine"]
'''
Morning      98.6
Afternoon    96.9
Evening      97.7
'''
temperatures_df.loc["Morning"]
'''
Maxine    98.6
James     98.9
Amanda    98.5
'''
temperatures_df.loc[["Morning", "Evening"]]
'''
        Maxine	James	Amanda
Morning	98.6	98.9	98.5
Evening	97.7	101.1	98.7
'''

temperatures_df[["Amanda", "Maxine"]]
"""	        Amanda	Maxine
Morning	    98.5	98.6
Afternoon	98.3	96.9
Evening	    98.7	97.7
"""
temperatures_df[["Amanda", "Maxine"]].loc[["Morning", "Afternoon"]]

"""         Amanda	Maxine
Morning	    98.5	98.6
Afternoon	98.3	96.9
"""
temperatures_df.describe()
"""     Maxine	James	Amanda
count	3.000000	3.000000	3.0
mean	97.733333	100.100000	98.5
std	    0.850490	1.113553	0.2
min	    96.900000	98.900000	98.3
25%	    97.300000	99.600000	98.4
50%	    97.700000	100.300000	98.5
75%	    98.150000	100.700000	98.6
max	    98.600000	101.100000	98.7
"""
temperatures_df = temperatures_df.T
"""	    Morning	Afternoon	Evening
Maxine	98.6	96.9	97.7
James	98.9	100.3	101.1
Amanda	98.5	98.3	98.7
"""
temperatures_df.sort_index(axis=1)

"""     Afternoon	Evening	Morning
Maxine	96.9	97.7	98.6
James	100.3	101.1	98.9
Amanda	98.3	98.7	98.5
"""