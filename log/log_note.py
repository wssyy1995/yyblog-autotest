一.将logging模块和log类封装到logger.py
二.在myunit测试基类中实例化log=Log()
三.在每个页面测试类的每条测试方法中，需要输出log的地方调用log.info/debug等方法输出log