import requests
from bs4 import BeautifulSoup
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
    r = s.get("https://www.zhihu.com/topic/19776749/organize/entire", headers=headers)
    print(r.status_code)
    print(r.text)
    with open("xx.html", "wb") as f:
        f.write(r.content)
except:
    print('未加载')
