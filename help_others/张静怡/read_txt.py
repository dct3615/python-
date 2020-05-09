# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 21:03:43 2019

@author: 00124175
"""

"""
读取txt文件
该文本中的分割符既有空格又有制表符（'/t'）,sep参数用'/s+'，可以匹配任何空格。
"""
#header=None:没有每列的column name，可以自己设定
#encoding='gb2312':其他编码中文显示错误
#sep=',':用逗号来分隔每行的数据
#index_col=0:设置第1列数据作为index
import pandas as pd
data = pd.read_table("1206sjl.txt",header=None,encoding='gb2312',sep='|',skiprows=1)
data1 = pd.read_table("1206sjl.txt",header=None,encoding='gb2312',sep='|',nrows=1)

cols_name = data1.iloc[:,0:80]
mydata = data.iloc[:,0:80]#读所有的行，0-79列
cols_name = cols_name.values.tolist()#转换为list
mydata.columns = cols_name#加上列名称
mydata.rename(columns=lambda x: x.strip(' '),inplace=True)#去掉dataframe中的前后空格
mydata[['__lat,__deg','__lon,__deg']] = mydata[['__lat,__deg','__lon,__deg']].apply(pd.to_numeric)

my_need_data = mydata[(mydata['__lat,__deg']>39.14) & (mydata['__lat,__deg']<39.17)&(mydata['__lon,__deg']>117.51)&(mydata['__lon,__deg']<117.53)]
print(my_need_data.iloc[:,0:3])
my_need_data.to_csv("result_csv.csv", index=0)






