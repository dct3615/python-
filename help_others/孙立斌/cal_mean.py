# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:04:32 2020

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
df=pd.read_excel('777盖板工时(1).xlsx',sheet_name='Sheet1')#可以通过sheet_name来指定读取的表单
data=df.head(5)#默认读取前5行的数据
#print("获取到所有的值:\n{0}".format(data))#格式化输出
#print(data['盖板号'].unique())#行索引

result = df.groupby(['盖板号'])['打开工时','关闭工时'].mean()#分组统计
result2 = df.groupby(['盖板号'])['适用性'].aggregate(lambda x:','.join(x))
result = result.reset_index()
result['适用性'] = list(result2)
result.to_excel('result.xlsx')








