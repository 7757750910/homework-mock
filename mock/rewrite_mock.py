import json
import mitmproxy.http
from mitmproxy import http, ctx


class Rewrite:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # 给定监听的url匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url \
                and "x=" in flow.request.pretty_url:
            # 打印请求发出去后的响应体内容
            ctx.log.info(f"{flow.response.text}")
            # 响应体内容格式为字符串
            ctx.log.info(str(type(flow.response.text)))
            # 使用json的loads方法转为字典格式
            data = json.loads(flow.response.text)
            # 修改字典中的指定位置的数据，实现rewrite
            data["data"]["items"][0]["quote"]["name"] = "小韩"
            # 替换响应体重的正文
            flow.response.text = json.dumps(data)


addons = [
    Rewrite()
]
# Debug模式
if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
