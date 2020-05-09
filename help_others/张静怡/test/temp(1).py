# -*- coding: utf-8 -*-
import pandas as pd
data = pd.read_table("1206.txt",header=None,encoding='gb2312',sep='|',skiprows=1)
data1 = pd.read_table("1206.txt",header=None,encoding='gb2312',sep='|',nrows=1)
data_first_row = data1.iloc[:,0:80]
cols_name = data_first_row.values.tolist()#转换为list 
sjldata = data.iloc[:,0:80]
sjldata.columns = cols_name#加上列名称
sjldata.rename(columns=lambda x:x.replace(' ',''),inplace=True)#删掉列名中的空格
sjldata.rename(columns=lambda x:x.replace('_',''),inplace=True)#删掉列名中的下划线
sjldata.rename(columns=lambda x:x.replace(',',''),inplace=True)#删掉列名中的逗号
MinAgl=sjldata[['latdeg','londeg','altftagl']]
aa=MinAgl[(MinAgl['latdeg']>39.14) & (MinAgl['latdeg']<39.17)]#筛选符合条件的经度
bb=MinAgl[(MinAgl['londeg']>117.51) & (MinAgl['londeg']<117.53)]#筛选符合条件的维度
#cc=aa.dropna(axis=0, how='all')
#dd=bb.dropna(axis=0, how='all')
#ee=sjldata[(sjldata[['latdeg']]>39.14) & (sjldata[['latdeg']]<39.17)]#筛选符合条件的经度
#ff=ee.dropna(axis=0, how='all')