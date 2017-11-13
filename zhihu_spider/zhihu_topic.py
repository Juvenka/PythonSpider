from bs4 import BeautifulSoup
import requests
s = requests.session()
url = 'https://www.zhihu.com/login/email'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
cookies = {'account': '362696076@@qq.com', 'password': 'Zxw1213#', '_xsrf': '30646533636334372d306162382d343336652d396433312d633331363263356234656164'}
zhihu_html1 = s.post(url, data=cookies, headers=headers)
print(zhihu_html1)
zhihu_soup = BeautifulSoup(zhihu_html1.content,'html5lib')
print(zhihu_soup)

zhihu_html = s.get('https://www.zhihu.com/people/edit',headers=headers)
soup = BeautifulSoup(zhihu_html.content,'html5lib')
print(soup)
myname = soup.find('span', attrs={"class": "Field-text",'data-reactid':'133'})
print(myname)
#<div id="Popover-43436-11071-toggle" aria-haspopup="true" aria-expanded="false" aria-owns="Popover-43436-11071-content">机器学习</div>
#<div aria-expanded="false" aria-haspopup="true" aria-owns="null-content" data-reactid="150" id="null-toggle">数据分析</div>
#<span class="Field-text" data-reactid="133">临床医疗</span>