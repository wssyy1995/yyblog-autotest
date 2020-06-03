import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base import Page

class Index(Page):
    url='/'
    #鼠标移动到logo上去
    def move_to_logo(self):
        self.open()
        logo=self.driver.find_element(By.ID,'banner_logo')
        ActionChains(self.driver).move_to_element(logo).perform()
        # 鼠标移动到logo上去后，这个logo 的style.background-position肯定会变，用js脚本获取这个background-position返回给position变量
        position=self.driver.execute_script("return window.getComputedStyle(document.getElementById('banner_logo')).getPropertyValue('background-position')")
        # 将position返回出去
        return position


    # 鼠标移动到gallery右侧小图
    def move_to_smallimg(self):
        self.open()
        ActionChains(self.driver).move_to_element(self.driver.find_elements(By.CLASS_NAME,'recommend_small_item')[0]).perform()
        # 鼠标移动到第一张小图上去后，small_image_shadow高度变为30px
        shadow_height=self.driver.execute_script("return window.getComputedStyle(document.getElementsByClassName('small_image_shadow')[0]).getPropertyValue('height')")
        return shadow_height



    #当前正播放的图片的索引
    def cur_big_img(self):
        recommend_slide=self.driver.find_elements(By.CLASS_NAME,'recommend_big_item')
        cur_pic=self.driver.find_element(By.CLASS_NAME,'active_pic')
        return recommend_slide.index(cur_pic)

    # 移到轮播图的action
    def move_to_bigimg(self):
        self.open()
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.ID,'recommend_slide')).perform()



    # 浏览器滚到页面底部
    def go_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    #点击post 分页：下一页
    def click_next_page(self):
        self.driver.find_element(By.ID,'next_mark').click()


    # 整合行为：post next page
    def post_next_page(self):
        self.open()
        self.go_to_bottom()
        self.click_next_page()
        return self.driver.current_url







if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get('http://localhost:5000')
    index=Index(driver)
    index.go_to_bottom()
    print(index.click_next_page())
    print(driver.current_url)
    print(index.domain_url+index.url+'?page=2#post_wrapper')


    driver.quit()