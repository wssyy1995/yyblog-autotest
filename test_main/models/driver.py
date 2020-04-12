# 定义浏览器驱动函数browser()，用来配置在不同的主机及浏览器的配置
from selenium.webdriver import Remote
from selenium import webdriver
def browser():
    driver=webdriver.Chrome()
    return driver

if __name__== '__main__':
    dr=browser()
    dr.get('http://www.wssyy2014.com')
    dr.quit()