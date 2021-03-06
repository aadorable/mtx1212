# *** coding: utf-8 ***
#@Time   : 2020/11/28 9:57
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test_mtx_order.py

'''
前提：依赖登录接口
下订单的所有场景
step1：先调用登录接口
step2：下订单接口
宗旨：设计测试用例的时候，接口调用之间没用依赖关系的（降到最低）
举例：存在依赖关系的接口，登录接口失败了，并不会影响下订单接口
'''

import requests
import allure
from api.apiLogin import ApiLogin
from api.apiOrder import ApiOrder


class TestOrder:
    def setup_class(self):
        self.session = requests.session()
        # 创建order对象
        self.order_obj = ApiOrder()
        # 调用成功的登录接口
        ApiLogin().login_success(self.session)

    @allure.feature('下单功能')
    @allure.story('下单成功 ')
    @allure.title('下单成功的测试用例')
    @allure.severity('critical')
    def test_order(self):
        '''
        测试用例
        :return:
        '''
        resp_order = self.order_obj.order(self.session)
        # 断言
        assert resp_order.json().get('msg') == '提交成功'