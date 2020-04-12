# page_obj模式：
# 为每个网页页面的元素和操作方法集合到一个页面类中，base是每个页面都需要有的方法和元素
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class Page:
    domain_url='http://localhost:5000'
    def __init__(self,driver):
        self.driver=driver
        self.timeout=30

    def _open(self,url):
        url=self.domain_url+url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s'%url

    def open(self):
        self._open(self.url)


    def on_page(self):
        return self.driver.current_url==(self.domain_url+self.url)

    # 注释掉find_element,直接在各页面用self.driver调用driver的内置find_element方法
    # # find_element是一个统一定位元素的方法，需要两个参数，第一个是By.查询方式，第二个参数是元素id/路径等
    # # *loc接收多个形参，以元祖形式传给函数
    # def find_element(self,*loc):
    #     return self.driver.find_element(loc[0],loc[1])
    #
    # def find_elements(self,*loc):
    #     return self.driver.find_elements(loc[0],loc[1])
    #
    # def script(self,js):
    #     return self.driver.execute_script(js)

    def flash_message(self):
        return self.driver.find_element(By.ID,'flash_message').text


# test
if __name__=='__main__':
    driver=webdriver.Chrome()
    page=Page(driver)
    page.open()
    username_ele=page.driver.find_element(By.ID,'username')
    username_ele.send_keys('yayan')
    time.sleep(1)

    driver.quit()



