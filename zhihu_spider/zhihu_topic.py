from bs4 import BeautifulSoup
import requests.auth
url = 'https://www.zhihu.com/signin?next=%2F%3Fnext%3D%252Ftopic%252F19776749%252Forganize%252Fentire'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
zhihu_html = requests.get(url,headers=headers,auth=requests.auth.HTTPBasicAuth('362696076@qq.com', 'Zxw1213#'))

zhihu_soup = BeautifulSoup(zhihu_html.content,'html5lib')
topic = zhihu_soup.find(name='div',attrs={'id':'zh-topic-organize-page-children'})
print(topic)
myname = zhihu_soup.body.find('span',attrs={'class':'name'})
print(myname.string)
print(zhihu_html.url)
print(zhihu_html.history)
