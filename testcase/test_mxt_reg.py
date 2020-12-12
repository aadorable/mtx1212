# *** coding: utf-8 ***
#@Time   : 2020/11/30 14:46
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test_mxt_reg.py

import pytest
import requests
import allure
from api.apiReg import ApiReg
from tools.readData import ReadData
from faker import Faker

all_cases = ReadData().get_excel_dict(['username', 'password', 'type', 'is_agree_agreement', 'exp'], 'reg_data.xlsx')

class TestReg():
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 实例化注册接口
        self.reg_obj = ApiReg()

    @allure.feature('注册功能')
    @allure.story('注册成功')
    @allure.title('注册成功的测试用例')
    @allure.severity('blocker')
    def test_reg_success(self):
        fake = Faker()
        username = fake.first_name()
        data = {
            'accounts': username,
            'pwd': '123456',
            'type': 'username',
            'is_agree_agreement': 1
        }
        resp = self.reg_obj.reg(self.session, data)
        assert resp.json()['msg'] == '注册成功'

    @allure.feature('注册功能')
    @allure.story('注册失败')
    @allure.title('注册失败的测试用例')
    @allure.severity('critical')
    @pytest.mark.parametrize('dic', all_cases)
    def test_reg_fail(self, dic):
        data = {
            'accounts': dic['username'],
            'pwd': dic['password'],
            'type': dic['type'],
            'is_agree_agreement': dic['is_agree_agreement']
        }
        resp = self.reg_obj.reg(self.session, data)
        assert resp.json()['msg'] == dic['exp']
