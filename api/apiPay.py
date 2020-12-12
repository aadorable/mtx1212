# *** coding: utf-8 ***
#@Time   : 2020/11/30 15:40
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : apiPay.py

import settings

class ApiPay():
    def __init__(self):
        self.url = settings.JUMP_URL

    def pay(self, session):
        resp = session.get(self.url, allow_redirects=False)
        resp_pay = session.get(resp.headers['Location'])
        return resp_pay

