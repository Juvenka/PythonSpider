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
postdata = {'account': '13585884094', 'password': 'Zxw1213#'}
response = session.get("https://www.zhihu.com", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
postdata['_xsrf'] =xsrf
result = session.post('https://www.zhihu.com/login/phone_num', data=postdata, headers=headers)
session.cookies.save(ignore_discard=True, ignore_expires=True)

zhihu_html = session.get('https://www.zhihu.com/people/edit',headers=headers)
soup = BeautifulSoup(zhihu_html.content,'html5lib')
print(soup)
myname = soup.find('span', attrs={"class": "Field-text",'data-reactid':'133'})
print(myname)
