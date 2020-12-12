# *** coding: utf-8 ***
#@Time   : 2020/11/26 20:36
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test_mxt_login.py

import pytest
import requests
import allure
from tools.readData import ReadData
from api.apiLogin import ApiLogin

login_cases = ReadData().get_excel_list('login_data.xlsx')
ids = ['正向用例', '逆向用例', '逆向用例', '逆向用例']

class TestLogin():
    # 在所有测试用例之前创建session，实例化登录接口对象  ->setup_class
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 实例化登录接口对象
        self.login_object = ApiLogin()

    @allure.feature('登录功能')
    @allure.story('登录的参数：正向和逆向')
    @allure.title('登录的测试用例')
    @allure.severity('critical')
    @pytest.mark.parametrize('accounts, pwd, exp', login_cases, ids=ids)
    def test_login(self, accounts, pwd, exp):
        data = {
            'accounts': accounts,
            'pwd': pwd
        }
        resp = self.login_object.login(self.session, data).json()
        # 做断言 业务层
        assert resp['msg'] == exp
