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

    # _open函数可以在执行打开url前先对url进行验证
    def _open(self,url):
        url=self.domain_url+url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s'%url

    def on_page(self):
        return self.driver.current_url==(self.domain_url+self.url)

    def open(self):
        self._open(self.url)


    # flash_mesage是网页全局的一个元素，卸载Page基类中，之后继承的页面子类都可以通过调用这个方法获得flash_message上的文本信息
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



