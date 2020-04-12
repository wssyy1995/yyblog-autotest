# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://127.0.0.1:5000/')
# driver.find_element_by_id('search_text').send_keys("yayan")
# time.sleep(5)
# print('finish')
# driver.find_element_by_id('search_submit').click()

# driver.set_window_size(480,800)
# time.sleep(2)
# driver.maximize_window()

# recommend_slide=driver.find_element_by_id('recommend_slide')
# print(recommend_slide)
# ActionChains(driver).move_to_element(recommend_slide).perform()
# print('move to recommend_slide ')
# left_trigger=driver.find_element_by_id('left_trigger')
# right_trigger=driver.find_element_by_id('right_trigger')
# ActionChains(driver).click(right_trigger).perform()
# time.sleep(1)
# ActionChains(driver).click(right_trigger).perform()
# time.sleep(1)
# ActionChains(driver).click(left_trigger).perform()
# time.sleep(1)
# ActionChains(driver).click(left_trigger).perform()

# search_text=driver.find_element_by_id('search_text')
# search_text.send_keys('yayan')
# time.sleep(1)
# search_text.send_keys(Keys.SPACE)
# search_text.send_keys(Keys.ENTER)
# print(driver.current_url)
# print(driver.title)
#

# 评论
# index_handle=driver.current_window_handle
# print('index_handle:  '+index_handle)
# yayan_test_post=driver.find_element_by_link_text("yayan note")
# yayan_test_post.click()
# yayan_test_post_handle=driver.window_handles[1]
#
# driver.switch_to.window(yayan_test_post_handle)
# author_name=driver.find_element_by_css_selector('#comment_form_author input')
# comment_body=driver.find_element_by_tag_name('textarea')
# comment_submit=driver.find_element_by_id('comment_submit')
# author_name.send_keys('yayan autotest')
# time.sleep(1)
# comment_body.send_keys('yayan autotest comment')
# time.sleep(1)
# comment_submit.click()
# time.sleep(1)


# alert
# gallery=driver.find_element_by_link_text('Gallery')
# gallery.click()
# time.sleep(1)
# alert=driver.switch_to.alert
# print(alert.text)
# time.sleep(1)
#

# 防止alert弹出导致的UnexpectedAlertPresentException
# from selenium.common.exceptions import UnexpectedAlertPresentException
# js="window.alert('hello,hs alert');"
# driver.execute_script(js)
# try:
#     driver.get_screenshot_as_file("./" + time.ctime() + ".png")
#     print('try')
# except UnexpectedAlertPresentException:
#     # 问题：catch 到了 UnexpectedAlertPresentException之后，会自动dismiss掉alert ?
#     driver.get_screenshot_as_file("./" + time.ctime() + ".png")
#     print('except')
# #
#
#


js="document.getElementById('bottom_footer'.innerText)"

title=driver.execute_script("return document.getElementById('bottom_footer').innerText")
print(title)





time.sleep(2)
driver.quit()


