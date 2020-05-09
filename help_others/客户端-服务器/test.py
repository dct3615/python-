# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:34:12 2019

@author: 00124175
"""

from numpy import *
import operator


def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

group,labels = createDataSet()
print(group,labels)