from HTMLTestRunner import HTMLTestRunner
import time
import unittest,random,sys,os
sys.path.append(os.getcwd()+'/test_main/models')
sys.path.append(os.getcwd()+'/test_main/page_obj')

test_dir='./test_main/test_case'
discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
# runner=unittest.TextTestRunner()
# runner.run(discover)

# 用HTMLTestRunner 来执行测试用例，生成测试报告
# (1)定义报告存放路径
report_address=open('./report/html_report/'+time.ctime()+'.html','wb')
# 创建HTMLTestRunner类的runner对象
runner=HTMLTestRunner(stream=report_address,title='YYBLOG-autotest',description='the report of yyblog autotest')
runner.run(discover)
