# encoding: utf-8
# !/usr/bin/env python

import time

import json
import requests
from bs4 import BeautifulSoup
s = requests.session()
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}


response = s.get("https://www.zhihu.com", headers=headers, verify=False)
soup = BeautifulSoup(response.content, "html.parser")
xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")


    #把验证码图片保存到当前目录，手动识别验证码

t = str(int(time.time() * 1000))#验证码是按时间戳命名
captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login&lang=cn"
print(captcha_url)
r = s.get(captcha_url, headers=headers)
with open('captcha.gif', 'wb') as f:
    f.write(r.content)
    f.close()

captcha = {
    'img_size': [200, 44],
    'input_points': [],
}
points = [[22.796875, 22], [42.796875, 22], [63.796875, 21], [84.796875, 20], [107.796875, 20],[129.796875, 22], [150.796875, 22]]
seq = input('请输入倒立字的位置\n>')
for i in seq:
    captcha['input_points'].append(points[int(i) - 1])
captcha = json.dumps(captcha)


login_url = 'https://www.zhihu.com/login/email'
data = {
    'email': '362696076@qq.com',
    'password': 'Zxw1213#',
    '_xsrf': xsrf,
    "captcha": captcha,
    'captcha_type': 'cn',}

response = s.post(login_url, data=data, headers=headers)
login_code = response.json()
print(login_code['msg'])

r = s.get("https://www.zhihu.com/settings/profile", headers=headers)
print(r.status_code)
print(r.text)
with open("xx.html", "wb") as f:
    f.write(r.content)
