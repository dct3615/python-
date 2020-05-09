# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:53:35 2018

@author: WANGLEI
"""

import  os, csv
from xlsxwriter.workbook import Workbook

path1 = 'C:\\Users\\WANGLEI\\Desktop\\1_linshi'#原始数据路径
path2 = 'C:\\Users\\WANGLEI\\Desktop\\InitialDociment4'#保存的位置
skipFirstName = 1
for folderName, subfolders, filenames, in os.walk(path1):   
    if skipFirstName ==1:
        skipFirstName = 0
        continue
    folderName1 = os.path.basename(folderName)#去除路径只显示文件名
    print(folderName1)
    csvCount = 0
    for csvFilename in filenames:
        
        os.chdir(path2)
        os.makedirs(folderName1, exist_ok=True)
        folderName2 = os.path.join(path2,folderName1)
        os.chdir(folderName2)#改变当前目录
        
        workbook = Workbook(csvFilename[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        
        os.chdir(folderName)
        if not csvFilename.endswith('.csv'):
            continue
        
        with open(csvFilename, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            os.chdir(folderName2)#改变当前目录
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()
