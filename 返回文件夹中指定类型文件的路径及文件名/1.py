

import os

def file_name(file_dir): 
    '''返回文件夹中指定类型文件的路径及文件名'''
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                L.append(os.path.join(root, file))
    return L

print(file_name('C:\\Users\\WANGLEI\\Desktop\\python_program\\叶数据处理\\第6个\\数据'))
