# 定义浏览器驱动函数browser()，用来配置在不同的主机及浏览器的配置
from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def browser():
    chrome_options = Options()
    # 禁止浏览器系统的消息弹窗notification
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
    # 禁止弹窗加入
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # 使用remote来指定远程主机执行自动化测试
    # host='远程主机ip'
    # dc={'browserName':'chrome'} #指定浏览器('chrome','firefox')
    # driver=Remote(command_executor='http://'+host+'/wd/hub',desired_capabilities=dc)
    return driver

if __name__== '__main__':
    dr=browser()
    dr.get('http://www.wssyy2014.com')
    dr.quit()
