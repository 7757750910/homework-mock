import logging

import requests


class BASEApi:
    _CORPID = "ww7d10c0f7ed8fd1d7"
    _CORPSECRET = "pHD8DqdH-u9B2SpFgMIEko8AIH-7FVw04aVi5zb9oMs"
    _BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"

    def __init__(self):
        # 传递参数
        self.token = self.get_token()

    def get_token(self):
        logging.info("获取'access_token'")
        corpid = self._CORPID
        corpsecret = self._CORPSECRET
        url = self._BASE_URL + f"gettoken?corpid={corpid}&corpsecret={corpsecret}"
        self.access_token = requests.get(url).json().get('access_token')
        return self.access_token

    def send(self, method, url, **kwargs):
        """
                封装发送请求
                :param method: 请求方式
                :param url: 路由地址
                :param kwargs: 其它参数
                :return:
                """
        # post 和 get 底层实现，requests.get == requests.request("GET",)
        url = self._BASE_URL + url
        return requests.request(method, url, **kwargs)
