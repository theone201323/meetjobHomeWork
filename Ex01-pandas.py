# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd # pandas = 數據分析

data = pd.Series([60,70,65,90]) #Series 一維陣列 串列

print(data)

# dataframe = 表格 二維陣列

student = pd.Series([70,90,80], index = ['李四','張三','王五'])

print(student)

print(student['張三'])

score = {'name':['John','Tom'], 'grade':[80,60]}
score_df = pd.DataFrame(score)

print(score_df)