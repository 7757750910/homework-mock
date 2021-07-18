import logging

import requests


from Test_api.BASE_API.member import Member


class Test_api():

    def setup_class(self):
        self.member = Member()

    def test_get(self):
        logging.info('开始执行获取成员信息用例')
        r = self.member.test_get()
        logging.info('断言返回码')
        assert r.json().get('errcode') == 0

    def test_add(self):
        logging.info('开始执行创建成员信息用例')
        r = self.member.test_add()
        logging.info('断言返回码')
        assert r.json().get('errcode') == 0

    def test_update(self):
        logging.info('开始执行更新成员信息用例')
        r = self.member.test_update()
        logging.info('断言返回码')
        assert r.json().get('errcode') == 0

    def test_delete(self):
        logging.info('开始执行删除成员信息用例')
        r = self.member.test_delete()
        logging.info('断言返回码')
        assert r.json().get('errcode') == 0
