# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:42:00 2018

@author: WANGLEI
"""

str1 = "12345"
list1 = list(str1)
print(list1)
 
str2 = "123 sjhid dhi"
list2 = str2.split() #or list2 = str2.split(" ")
print(list2)
 
str3 = "www.google.com"
list3 = str3.split(".")
print(list3)



str4 = "".join(list3)
print(str4)
str5 = ".".join(list3)
print(str5)
str6 = " ".join(list3)
print(str6)

ls1 = ['a', 1, 'b', 2]
ls2 = [str(i) for i in ls1]
print(ls2)
ls3 = ''.join(ls2)
print(ls3)
