import time
import unittest,random,sys,os
sys.path.append(os.path.dirname(os.getcwd())+'/models')
sys.path.append(os.path.dirname(os.getcwd())+'/page_obj')
import myunit,function
from loginPage import Login


# login测试类
class loginTest(myunit.MyTest):
    # 登陆成功,login>logout,并且flash message 应该是'Welcome back.'

    def test_login1(self):
        self.log.info('Login1:right username,right password,')
        # login为Login页面类实例化对象，传入的self.driver是在myunit.MyTest中构造的
        login=Login(self.driver)
        login.user_login(username='yayan',password='1234')
        function.insert_img(self.driver,'login_success')
        self.log.info('Login1:flash_message: %s'%login.flash_message())
        self.assertTrue(login.flash_message()=='Welcome back.' and login.log_text()=='Log Out',msg='login should success')


    # 登陆失败：username正确，密码错误
    def test_login2(self):
        self.log.info('Login2:right username,wrong password,')
        login=Login(self.driver)
        login.user_login(username='yayan', password='1111')
        function.insert_img(self.driver,'login_fail_with_wrong_pwd')
        self.log.info('Login2:flash_message: %s'%login.flash_message())
        self.assertTrue(login.flash_message()=='Invalid username or password.' and login.log_text()=='Log In',msg='login should fail')



    #登陆失败 ：username为空，密码为空
    def test_login3(self):
        login=Login(self.driver)
        self.log.info('Login3:right username,empty password,')
        login.user_login(username='yayan', password='')
        function.insert_img(self.driver,'login_fail_with_empty_pwd')
        self.log.info('Login3:log_text: %s'%login.log_text())
        self.assertTrue(login.log_text()=='Log In',msg='login should fail')




if __name__=='__main__':
    unittest.main()