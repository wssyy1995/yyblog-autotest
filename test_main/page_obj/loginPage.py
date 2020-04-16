# 为login页面编写页面对象，对用户登录页面上的用户名/密码输入框，登录按钮和提示信息的行为进行封装
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base import Page

class Login(Page):
    url='/auth/login?next=%2F%3F'

    # 单个元素的action
    def input_username(self,username):
        self.driver.find_element(By.ID,'username').send_keys(username)

    def input_pwd(self,password):
        self.driver.find_element(By.ID,'password').send_keys(password)

    def login_submit(self):
        self.driver.find_element(By.ID,'submit').click()

    #整合了登录的整个流程的方法
    def user_login(self,username='test',password='1234'):
        self.open()
        self.input_username(username)
        time.sleep(1)
        self.input_pwd(password)
        time.sleep(1)
        self.login_submit()
        time.sleep(1)

    #登陆后验证login文本是否改变 >logout
    def log_text(self):
        # 获取.log_text元素的文本内容，注意是自动strip了空格
        return self.driver.find_element(By.CLASS_NAME,'log_text').text






# test
if __name__=='__main__':
    driver=webdriver.Chrome()
    login=Login(driver)
    login.user_login()
    logtext=login.log_text()
    flash_m=login.flash_message()
    if logtext=='Log Out' and flash_m=='Welcome back.':
        print('log in success ')

    else:
        print('log in fail')

    driver.quit()



