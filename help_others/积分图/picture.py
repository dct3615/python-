# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:26:50 2019

@author: 00124175
"""

#代码及效果图
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

def func(x):
    return (np.sin(x) + 1)/np.sqrt(x**2 + 1)

x = np.linspace(-5,10)
y = func(x)

fig,axes = plt.subplots()
#绘制曲线
plt.plot(x,y,'r',linewidth = 2)
a=-2
b=5
 
#坐标轴设置
axes.set_xticks([a,b])
axes.set_xticklabels(['$a=-2$','$b=5$'])
axes.set_yticks([])
plt.figtext(0.9,0.05,'$x$')
plt.figtext(0.1,0.9,'$y$')

#绘制灰色多边形
ix=np.linspace(a,b)
iy=func(ix)
ixy = zip(ix,iy)
verts=[(a,0)]+list(ixy)+[(b,0)]
poly = Polygon(verts,facecolor='0.9',edgecolor='0.5')
axes.add_patch(poly)

#添加数学公式
x_math =(a+b)*0.5*0.8
y_math = 1.45
plt.text(x_math,y_math,'$int_a^b((sin(x)+1)/sqrt(x^2 + 1)dx$',fontsize=10,horizontalalignment='center')
plt.show()



