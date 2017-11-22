import requests
from bs4 import BeautifulSoup
import time
import json
import http.cookiejar

headers = {
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
s = requests.Session()
s.cookies = http.cookiejar.LWPCookieJar('zhihu_cookie')
#加载cookies
try:
    s.cookies.load(ignore_discard=True,ignore_expires=True)
    r = s.get("https://www.zhihu.com/people/edit", headers=headers)
    print(r.status_code)
    with open("xx.html", "wb") as f:
        f.write(r.content)
except:
    print('未加载')
    #获取xsrf
    response = s.get("https://www.zhihu.com", headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
    #获取验证码并且输入
    t = str(int(time.time() * 1000))#验证码是按时间戳命名
    captcha_url = 'https://www.zhihu.com/captcha.gif?r='+ t + '&type=login&lang=cn'
    print(captcha_url)
    gifhtml = s.get(captcha_url,headers=headers)
    with open('captcha.jpg','wb') as f:
        f.write(gifhtml.content)
    captcha={"img_size":[200,44],"input_points":[]}
    input_points = [[22.796875, 22], [42.796875, 22], [63.796875, 21], [84.796875, 20], [107.796875, 20],[129.796875, 22], [150.796875, 22]]
    seq = input('输入位置:')
    for i in seq:
        captcha["input_points"].append(input_points[int(i)-1])
    captcha = json.dumps(captcha)
    #登陆
    postdata = {'email': '362696076@qq.com','password': 'Zxw1213#','_xsrf': xsrf,"captcha": captcha,'captcha_type': 'cn'}
    result = s.post('https://www.zhihu.com/login/email', data=postdata, headers=headers).json()
    print(result['msg'])
    #保存cookies
    s.cookies.save(ignore_discard=True,ignore_expires=True)




