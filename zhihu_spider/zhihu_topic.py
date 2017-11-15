import requests
from bs4 import BeautifulSoup
import time
import json
s = requests.Session()

headers = {

    'Host': 'www.zhihu.com',
    'Origin': 'https://www.zhihu.com/',
    'Referer': 'https://www.zhihu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
input_points = [[22.796875, 22], [42.796875, 22], [63.796875, 21], [84.796875, 20], [107.796875, 20],[129.796875, 22], [150.796875, 22]]
captcha={"img_size":[200,44],"input_points":[]}
postdata = {'email': '362696076@qq.com', 'password': 'Zxw1213#'}

response = s.get("https://www.zhihu.com", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
postdata['_xsrf'] = xsrf
headers['X-Xsrftoken'] = xsrf

#获取验证码
t = str(int(time.time() * 1000))#验证码是按时间戳命名
captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login&lang=cn"
print(captcha_url)
gifhtml = s.get(captcha_url,headers=headers)
with open('captcha.jpg','wb') as f:
    f.write(gifhtml.content)
    f.close()

seq = input('输入位置:')
for i in seq:
    captcha["input_points"].append(input_points[int(i)-1])
captcha = json.dumps(captcha)

postdata['captcha'] = captcha
postdata['captcha_type'] = 'cn'
print(postdata)
result = requests.post('https://www.zhihu.com/login/email', data=postdata, headers=headers)
print(result.status_code)
result.raise_for_status()
result_soup = BeautifulSoup(result.content, "html5lib")
print(result_soup)
login_code = result.json()
print(login_code['msg'])
print(s.cookies)
r = s.get("https://www.zhihu.com/settings/profile", headers=headers)
print(r.status_code)
print(r.text)
with open("xx.html", "wb") as f:
    f.write(r.content)

#zhihu_html = s.get('https://www.zhihu.com',headers=headers)"
#soup = BeautifulSoup(zhihu_html.content,'html5lib')"
#print(soup)"
#myname = soup.find('span', attrs={"class": "TopstorySideBar-navText",'data-reactid':'1241'})
#print(myname)



##<span class="TopstorySideBar-navText" data-reactid="1241">我关注的问题</span>

#<img class="Captcha-image" alt="验证码" style="display: block;" src="/captcha.gif?r=1510713934158&amp;type=login&amp;lang=cn">

#Request URL:https://www.zhihu.com/captcha.gif?r=1510715551212&type=login&lang=cn

#_xsrf:5f437ea53ccac17dbd4ead28bb54b11a
#password:Zxw1213#1
#captcha:{"img_size":[200,44],"input_points":[[19.5,20.609375],[48.5,31.609375],[63.5,25.609375],[94.5,25.609375],[125.5,21.609375],[146.5,26.609375],[169.5,28.609375]]}
#captcha_type:cn
#email:362696076@qq.com
