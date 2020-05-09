# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:24:23 2019

@author: 00124175
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

#设置你自己的chormedriver存放路径
driver_path = r"C:\Users\00124175\Desktop\python\抢票脚本\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
 
#自动输入网址，访问豆瓣
driver.get("https://accounts.douban.com/passport/login?source=movie")
 
#出发地的操作，网页元素定位
#ID定位click()
driver.implicitly_wait(1.5)#等待0.1s
driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()#点击登录

driver.find_element_by_id('username').send_keys('19922619717')#输入用户名
driver.find_element_by_name('password').send_keys('863764733dct')#输入密码

driver.find_element_by_name('password').send_keys(Keys.ENTER)#点回车登录
#driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()#点击登录

