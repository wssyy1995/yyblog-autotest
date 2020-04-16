import logging,time,os

# 通过logging.basicConfig进行参数设定
#
# logging.basicConfig(
#     # 默认是warning级别才会输出,level可以设置
#     level=logging.DEBUG,
#     # log默认在终端输出，filenname可以指定输出的文件地址
#     filename='logging_'+time.ctime()+'.text',
#     # format规范日志的内容和格式：
#         # %（）s 括号内为要输出的内容； lineno代表打印日志在代码第几行;message就为log信息;levelname为log等级
#     format='%(levelname)s %(message)s [line:%(lineno)d]'
#
# )
#
# logging.debug('yy debug message')
# logging.info('yy info message')
#
# logging.warning('yy warning message')
# logging.error('yy error message')
# logging.critical('yy critical message')
# logging.info('yy2 info message')
#

class Log():
    def __init__(self):
        # 文件的命名
        self.logname =os.getcwd()+'/log/log_'+time.strftime('%Y_%m_%d')+'.text'
        print()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - [line:%(lineno)d] - %(levelname)s: %(message)s')
    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

if __name__ == "__main__":
   log = Log()
   log.info("---测试开始----")
   log.info("输入密码")
   log.warning("----测试结束----")