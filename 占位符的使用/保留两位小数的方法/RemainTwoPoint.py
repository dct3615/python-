# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 09:21:11 2018
保留两位小数
@author: WANGLEI
"""

#a = 5.026
a = 17.955
b = 5.000

print(round(a,2))
print(round(b,2))
print('\n')

print('%.2f' % a)
print('%.2f' % b)
print('\n')

print(float('%.2f' % a))
print(float('%.2f' % b))
print('\n')

from decimal import Decimal

print(Decimal(str(a)).quantize(Decimal('0.00')))
print(Decimal('5.000').quantize(Decimal('0.00')))

'''多个值保留两位小数'''
ls1 = [1.2356,2.347,4.123]
ls2 = [float('%.2f' % a) for i in ls1]
print(ls2)
