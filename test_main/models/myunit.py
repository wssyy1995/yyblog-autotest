# 自定义测试框架类，继承unittest.TeseCase,主要是为每一个测试类都定义好通用的setUp和tearDown函数
from selenium import webdriver
from driver import browser
import unittest
import os,sys
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()

