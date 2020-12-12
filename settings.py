# *** coding: utf-8 ***
#@Time   : 2020/11/28 9:39
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : settings.py
import os

# 常量的写法 变量=值
IP = 'http://121.42.15.146:9090'
HEADERS = {'X-Requested-With': 'XMLHttpRequest'}
ABS_PATH = os.path.abspath(__file__)
DIR_NAME = os.path.dirname(ABS_PATH)
JUMP_URL = None
