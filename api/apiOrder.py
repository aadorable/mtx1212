# *** coding: utf-8 ***
#@Time   : 2020/11/28 10:03
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : apiOrder.py

import settings
from settings import  IP,HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()

class ApiOrder():
    def __init__(self):
        logger.info('开始获取下单接口的URL...')
        self.url = IP + '/mtx/index.php?s=/index/buy/add.html'
        logger.info('下单接口的URL：{}'.format(self.url))

    def order(self, session):
        '''
        发起下订单的请求
        :param session:
        :return:
        '''
        data = {
            'goods_id': 1,
            'stock': 1,
            'buy_type': 'goods',
            'address_id': 1290,
            'payment_id': 1,
            'spec': '',

        }
        logger.info('开始发起下单请求，请求参数是：{}，请求头是：{}'.format(data, HEADERS))
        resp_order = session.post(self.url, data=data, headers=HEADERS)
        settings.JUMP_URL = resp_order.json().get('data').get('jump_url')
        logger.info('响应结果是：{}'.format(resp_order.json()))
        return resp_order