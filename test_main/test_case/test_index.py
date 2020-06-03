import time
import unittest,random,sys,os
sys.path.append(os.path.dirname(os.getcwd())+'/models')
sys.path.append(os.path.dirname(os.getcwd())+'/page_obj')
import myunit,function
from indexPage import Index

class indexTest(myunit.MyTest):
    #判断logo鼠标悬浮之后的图片偏移量是否变化
    def ntest_logo(self):
        index=Index(self.driver)
        # position是logo鼠标悬浮之后的图片偏移量
        position=index.move_to_logo()
        self.log.info('after move to logo ,position: %r'%(position))
        function.insert_img(self.driver, 'move to logo,logo change')
        self.assertNotEqual(position,'0% 0%')

    # 判断小图片悬浮后文字是否出现
    def ntest_smallimg(self):
        index=Index(self.driver)
        shadow_height=index.move_to_smallimg()
        self.log.info('after move to small_img ,the shadow height: %r'%(shadow_height))
        function.insert_img(self.driver,'move to small img,text appear')
        self.assertEqual(shadow_height,'30px')

    # 判断鼠标移到大图后，大图停止轮播
    def ntest_timer(self):
        index=Index(self.driver)
        index.move_to_bigimg()
        function.insert_img(self.driver,'timmer,before move')
        pre_move_pic = index.cur_big_img()
        self.log.info('move to the big img,current img index is :%r'%(pre_move_pic))
        time.sleep(5)
        function.insert_img(self.driver,'timmer,after move')
        after_move_pic = index.cur_big_img()
        self.log.info(' 5s after moving to the big img,current img index is :%r'%(after_move_pic))
        self.assertEqual(pre_move_pic,after_move_pic)

    # 轮播图下一张
    # 轮播图上一张
    # 点击小点


    #点击post分页:跳转到下一页
    def test_next_page(self):
        index=Index(self.driver)
        cur_url=index.post_next_page()
        self.log.info('after click the post next page,the cur_url is :%r'%(cur_url))
        function.insert_img(self.driver,'after click the post next page,cur_url should be page=2')
        self.assertEqual(cur_url,index.domain_url+index.url+'?page=2#post_wrapper')










if __name__=='__main__':
    unittest.main()