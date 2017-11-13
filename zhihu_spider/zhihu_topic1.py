import requests
import http.cookiejar
from bs4 import BeautifulSoup
session = requests.Session()
session.cookies = http.cookiejar.LWPCookieJar("cookie")
headers = {
    'Host': 'www.zhihu.com',
    'Origin': 'https://www.zhihu.com/',
    'Referer': 'http://www.zhihu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
}
postdata = {'account': '362696076@qq.com', 'password': 'Zxw1213#'}
response = session.get("https://www.zhihu.com", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
postdata['_xsrf'] =xsrf
result = session.post('http://www.zhihu.com/login/email', data=postdata, headers=headers)
session.cookies.save(ignore_discard=True, ignore_expires=True)

zhihu_html = session.get('https://www.zhihu.com/people/beiki/activities',headers=headers)
soup = BeautifulSoup(zhihu_html.content,'html5lib')
myname = soup.find('span', attrs={"class": "ProfileHeader-name"})
print(myname.string)
