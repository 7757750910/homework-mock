import logging

import requests

from Test_api.BASE_API.base_api import BASEApi


class Member(BASEApi):
    def test_get(self):
        logging.info('读取企业通讯录的成员的信息并返回')
        userid = 'HanShouShuai'
        r = self.send("GET", f"user/get?access_token={self.token}&userid={userid}")
        return r

    def test_add(self):
        logging.info('新增企业通讯录的成员的信息并返回')
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "department": [1],
            "email": "zhangsan@gzdev.com",
        }
        r = self.send("POST", f"user/create?access_token={self.token}", json=data)
        return r

    def test_update(self):
        logging.info('更新企业通讯录的成员的信息并返回')
        data = {
            "userid": "775778",
            "alias": "李六",
        }
        r = self.send("POST", f"user/update?access_token={self.token}", json=data)
        return r

    def test_delete(self):
        logging.info('删除企业通讯录的成员的信息并返回')
        userid = '1'
        r = self.send("GET", f"user/delete?access_token={self.token}&userid={userid}")
        return r
