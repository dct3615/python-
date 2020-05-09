# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 16:55:48 2018

@author: WANGLEI
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:16:48 2018

@author: WANGLEI
"""

import os
import glob
import csv
from xlsxwriter.workbook import Workbook

path1 = 'C:\\Users\\WANGLEI\\Desktop\\1_linshi'#原始数据路径
path2 = 'C:\\Users\\WANGLEI\\Desktop\\InitialDociment4'#转化后保存的路径
'''
for folderName, subfolders, filenames, in os.walk(path1):
    print(folderName)
    print(subfolders)
    print(filenames)
    continue
'''
os.chdir(path1)#改变当前目录
for csvfile in glob.glob(os.path.join('.', '*.csv')):
    print(os.getcwd())   
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()