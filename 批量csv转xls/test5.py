# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:06:04 2018

@author: WANGLEI
"""
import csv
import xlwt
import os

path1 = 'C:\\Users\\WANGLEI\\Desktop\\1_linshi'#原始数据路径
path2 = 'C:\\Users\\WANGLEI\\Desktop\\InitialDociment4'#转化后保存的路径
#os.chdir(path1 + '\\崔美叶')#改变当前目录



def csv_to_xlsx(csvfile,folderName1):
    with open(csvfile, 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')  # 创建一个sheet表格
        l = 0
        for line in read:
            #print(line)
            r = 0
            for i in line:
                #print(i)
                sheet.write(l, r, i)  # 一个一个将单元格数据写入
                r = r + 1
            l = l + 1
        os.chdir(path2)#改变当前目录
        os.makedirs(folderName1, exist_ok=True)#创建一个文件夹
        os.chdir(path2 + '\\' + folderName1)#改变当前目录
        workbook.save(csvfile[:-4] + '.xls')  # 保存Excel
        
if __name__ == '__main__':
    skipFirstName = 1
    count = 0
    for folderName, subfolders, filenames, in os.walk(path1):   
        if skipFirstName ==1:
            skipFirstName = 0
            continue
        folderName1 = os.path.basename(folderName)#去除路径只显示文件名
        for csvFilename in filenames:
            count = count + 1
            print('第' + count + '个')
            if not csvFilename.endswith('.csv'):
                continue
            os.chdir(folderName)#改变当前目录
            csv_to_xlsx(csvFilename,folderName1)

   