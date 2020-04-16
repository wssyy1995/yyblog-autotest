# 自定义测试框架类，继承unittest.TeseCase,主要是为每一个测试类都定义好通用的setUp和tearDown函数
from selenium import webdriver
from driver import browser
from logger import Log
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.log = Log()
        self.log.info('-----------testcase-----------')
    def tearDown(self):
        self.driver.quit()

