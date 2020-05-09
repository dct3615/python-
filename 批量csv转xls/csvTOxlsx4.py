# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:10:23 2018

@author: WANGLEI
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:16:48 2018

@author: WANGLEI
"""

import os
import csv
from xlsxwriter.workbook import Workbook

path1 = 'C:\\Users\\WANGLEI\\Desktop\\1_linshi'#原始数据路径
path2 = 'C:\\Users\\WANGLEI\\Desktop\\InitialDociment4'#转化后保存的路径

skipFirstName = 1
for folderName, subfolders, filenames, in os.walk(path1):   
    if skipFirstName ==1:
        skipFirstName = 0
        continue
    folderName1 = os.path.basename(folderName)#去除路径只显示文件名
    path3 = os.path.join(path2,folderName1)#保存路径深入一级
    path4 = os.path.join(path1,folderName1)#原始数据深入一级
    os.chdir(path2)#改变当前目录
    os.makedirs(folderName1, exist_ok=True)#创建一个文件夹
    os.chdir(path3)#改变当前目录
    #print(path3)
    #print(path4)
    csvCount = 0
    for csvFilename in filenames:
        if not csvFilename.endswith('.csv'):
            continue
        workbook = Workbook(csvFilename[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        os.chdir(path4)#改变当前目录
        with open(csvFilename, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            os.chdir(path3)#改变当前目录
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        