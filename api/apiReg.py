# *** coding: utf-8 ***
#@Time   : 2020/11/30 14:27
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : apiReg.py

from settings import IP, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()

class ApiReg():
    def __init__(self):
        logger.info('开始获取注册接口的URL...')
        self.url = IP + '/mtx/index.php?s=/index/user/reg.html'
        logger.info('注册接口的URL：{}'.format(self.url))

    def reg(self, session, data):
        logger.info('开始发起注册请求，请求参数是：{}，请求头是：{}'.format(data, HEADERS))
        resp_reg = session.post(self.url, data=data, headers=HEADERS)
        logger.info('响应结果是：{}'.format(resp_reg.json()))
        return resp_reg