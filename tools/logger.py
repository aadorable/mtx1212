# *** coding: utf-8 ***
#@Time   : 2020/11/26 18:00
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : logger.py

import logging.handlers
from settings import DIR_NAME

class GetLogger():
    '''
    已创建过logger对象就无需再创建
    '''
    # logger对象的初始值设为None
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger == None:
            # 1. 获取日志器
            cls.logger = logging.getLogger()
            # 2. 设置总级别
            cls.logger.setLevel(logging.INFO)
            # 3. 获取格式器
            # 3.2 格式器的输出样式
            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] -%(message)s'
            # 3.3 创建格式器，并且设置样式
            fm = logging.Formatter(fmt)
            # 4. 创建处理器，按时间切割文件
            tf = logging.handlers.TimedRotatingFileHandler(filename= DIR_NAME + '/log/mtx.log',
                                                           when='S',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # 5. 在处理器中添加格式器
            tf.setFormatter(fm)
            # 6. 将处理器添加到日志器中
            cls.logger.addHandler(tf)
        return cls.logger



if __name__ == '__main__':
    logger = GetLogger.get_logger()
    logger.debug('调试')
    logger.error('错误')