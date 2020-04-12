# 定义一些通用的方法，比如截图
from selenium import webdriver
import time
def insert_img(driver,file_name):
    # file_path的路径是基于运行脚本(即run_test.py)的相对路径
    file_path='./report/image/'+file_name+'_'+time.ctime()+'.png'
    driver.get_screenshot_as_file(file_path)



# 用来测试insert_img，只有在直接运行当前模块时才会运行下面的代码
if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get('http://www.wssyy2014.com')
    insert_img(driver,'yytest')
    driver.quit()