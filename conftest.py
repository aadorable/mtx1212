# *** coding: utf-8 ***
#@Time   : 2020/11/21 10:32
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : conftest.py

'''
conftest.py 名字是固定的
钩子函数（hook）——— 名字是固定的
pytest_collection_modifyitems(items)    （重点是运行时机）
底层对用例名字起作用的两个字段 name, _nodeid
unicode_escape
'''

def pytest_collection_modifyitems(items):
    print('测试')
    for item in items:
        item.name = item.name.encode().decode('unicode_escape')
        item._nodeid = item.nodeid.encode().decode('unicode_escape')