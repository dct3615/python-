# -*- coding: utf-8 -*-
"""
将指定文件夹的csv文件全部复制粘贴到另一个路径
‘其中国航QAR\\InitialDocimentGrops\\第一组’中的文件有子文件夹
'G:\\国航QAR\\Grops\\第一组'无子文件夹
"""

import  os
import shutil


def findTxt3(folder,groups):
    csvNum = 1
    os.chdir(folder)#改变当前目录
    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.endswith('.csv'):
                name = os.path.join(folder, root)
                os.chdir(name)#把路径设置为当前文件夹
                
                #从新命名文件，从1开始
                temp = str(csvNum)+'.csv'
                csvNum += 1
                
                #如果目录不存在，创建一个
                isExists=os.path.exists(groups)
                if not isExists:
                    os.makedirs(groups) 
 
                shutil.copy(file,groups +'\\' + temp)#复制一个文件
                os.chdir(folder)#把路径设为主文件夹
                
 

path1 = 'G:\国航QAR\QAR_TEST'#保存的地址
path2 = 'G:\\国航QAR\\QAR_remove_parameters_grops'  #原始数据目录              
findTxt3(path2 + '\\1第一组',path1 + '\\Grops\\第一组')#需要备份的文件夹
findTxt3(path2 + '\\2第二组',path1 + '\\Grops\\第二组')#需要备份的文件夹
findTxt3(path2 + '\\3第三组',path1 + '\\Grops\\第三组')#需要备份的文件夹
#findTxt3('G:\\国航QAR\\InitialDocimentGrops\\第四组','G:\\国航QAR\\Grops\\第四组')#需要备份的文件夹




   
 


#shutil.copy(local_img_name,path+'/'+new_obj_name)

