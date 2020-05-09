#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 填充表单.py
# Author: MuNian
# Date  : 2019-12-11

'''

弹窗处理:
switch_to_alert()
页面切换:
switch_to_window

'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000')

# 找到name的选项卡
select = Select(driver.find_element_by_name('status'))


# select.select_by_index(2)
select.select_by_visible_text('审核不通过')


