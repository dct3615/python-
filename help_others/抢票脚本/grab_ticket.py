# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:24:23 2019

@author: 00124175
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#设置你自己的chormedriver存放路径
driver_path = r"C:\Users\00124175\Desktop\python\抢票脚本\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
 
#自动输入网址，访问12306
driver.get("https://www.12306.cn/index/")
 
#出发地的操作，网页元素定位
#ID定位click()
driver.implicitly_wait(0.1)#等待0.1s
driver.find_element_by_id('fromStationText').click()
driver.find_element_by_id('fromStationText').send_keys('长沙')

#模拟键盘操作
driver.find_element_by_id('fromStationText').send_keys(Keys.ENTER)

#到达地元素定位
#class name

driver.find_element_by_id('toStationText').click()
driver.find_element_by_id('toStationText').send_keys('天津')
#模拟键盘操作
driver.find_element_by_id('toStationText').send_keys(Keys.ENTER)

#出发日期处理方式
#xpath

#出发日期的处理方式 xpath
driver.find_element_by_xpath("//*[@id='train_date']").click()
so = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[2]/div[26]/div').click()