#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 鼠标动作链.py
# Author: MuNian
# Date  : 2019-12-11

from selenium import webdriver
from selenium.webdriver import ActionChains

'''
double_click() 双击
左键按住不放 --> click_and_hold

 tesseract ---> 机器识别 

'''

driver = webdriver.Chrome()
driver.get('https://www.12306.cn/index/')
# 实现鼠标移动  并且单击
ac = driver.find_element_by_id('fromStationText')
ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()

