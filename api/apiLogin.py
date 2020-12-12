# *** coding: utf-8 ***
#@Time   : 2020/11/28 9:51
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : apiLogin.py

'''
登录请求的信息
'''
from settings import IP,HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()

class ApiLogin():
    def __init__(self):
        '''
        记录日志信息的时候，不能用逗号拼接
        '''
        logger.info('开始获取登录接口的URL...')
        self.url = IP + '/mtx/index.php?s=/index/user/login.html'
        logger.info('登录接口的URL：{}'.format(self.url))

    def login(self, session, data):
        '''
        对登录接口进行自动化测试
        :data: 请求参数（post,get)   场景：1.参数化 业务层传递   2.验证这个功能，直接写死就可以了
        :return: 
        '''
        # 发起请求
        logger.info('开始发起登录请求，请求参数是：{}，请求头是：{}'.format(data, HEADERS))
        resp_login = session.post(url=self.url, data=data, headers=HEADERS)
        logger.info('响应结果是：{}'.format(resp_login.json()))
        return resp_login

    def login_success(self, session):
        '''
        跟其他接口进行关联，发起成功的登录请求
        :return: 
        '''
        data = {
            'accounts': 'xueqing',
            'pwd': '123456'
        }
        logger.info('开始发起登录请求，请求参数是：{}，请求头是：{}'.format(data, HEADERS))
        resp_login = session.post(url=self.url, data=data, headers=HEADERS)
        logger.info('响应结果是：{}'.format(resp_login.json()))
        return resp_login