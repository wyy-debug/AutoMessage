import json

import requests
class HttpHandle:
    # 接口初始化
    def __init__(self):
        pass

    def get(self, url):
        r = requests.get(url)
        return r.content.decode('UTF-8')

    def post(self, url, postdata):
        p = requests.post(url, data=postdata)
        return p.text

    def put(self, url, putdata):
        p = requests.put(url, data=putdata)
        return p.text

    def add_device(self,data):
        return self.post("http://127.0.0.1:5000/api/device/",data)

    def get_devices(self):
        return self.get("http://127.0.0.1:5000/api/device/")

    def add_number(self, data, device_id):
        return self.post("http://127.0.0.1:5000/api/number/"+str(device_id),data)

    def get_numbers(self, device_id):
        return self.get("http://127.0.0.1:5000/api/number/"+str(device_id))

    def add_message(self, data):
        return self.post("http://127.0.0.1:5000/api/number/",data)

    def get_messages(self, device_id):
        return self.get("http://127.0.0.1:5000/api/number/"+str(device_id))
