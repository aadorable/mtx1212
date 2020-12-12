# *** coding: utf-8 ***
#@Time   : 2020/11/30 17:01
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test_mtx_pay.py

import requests
import allure
from api.apiPay import ApiPay
from api.apiLogin import ApiLogin
from api.apiOrder import ApiOrder

class TestPay():
    def setup_class(self):
        # 创建session对象
        self.session = requests.session()
        # 登录系统
        ApiLogin().login_success(self.session)
        # 下单
        ApiOrder().order(self.session)
        # 实例化支付接口
        self.pay_obj = ApiPay()

    @allure.feature('支付功能')
    @allure.story('支付成功')
    @allure.title('支付成功的测试用例')
    @allure.severity('critical')
    def test_pay(self):
        resp = self.pay_obj.pay(self.session)
        assert '支付成功' in resp.text