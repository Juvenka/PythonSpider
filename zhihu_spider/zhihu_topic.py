from bs4 import BeautifulSoup
import requests
s = requests.session()
url = 'https://www.zhihu.com/login/email'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
cookies = {'account':'362696076@qq.com','password':'Zxw1213#','_xsrf':'6f7f24b92e8dcde6b5760b4436e13d43'}
zhihu_html1 = s.post(url,headers=headers,data=cookies)
print(zhihu_html1)
zhihu_soup = BeautifulSoup(zhihu_html1.content,'html5lib')
print(zhihu_soup)
r = s.get(url,headers=headers)
print(r)
zhihu_soup = BeautifulSoup(r.content,'html5lib')
print(zhihu_soup)
