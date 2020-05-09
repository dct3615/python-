# -*- coding: utf-8 -*-
import pandas as pd
data = pd.read_table("1206.txt",header=None,encoding='gb2312',sep='|',skiprows=1)
data1 = pd.read_table("1206.txt",header=None,encoding='gb2312',sep='|',nrows=1)
data_first_row = data1.iloc[:,0:80]
cols_name = data_first_row.values.tolist()#转换为list
sjldata = data.iloc[:,0:80]
sjldata.columns = cols_name#加上列名称
sjldata[['   __lat,__deg ','   __lon,__deg ']] = sjldata[['   __lat,__deg ','   __lon,__deg ']].apply(pd.to_numeric)
criteria = (sjldata['   __lat,__deg ']>39.14) & (sjldata['    __lat,__deg ']<39.17)&(sjldata['   __lon,__deg ']>117.51)&(sjldata['    __lon,__deg ']<117.53)
sjldata[criteria]
