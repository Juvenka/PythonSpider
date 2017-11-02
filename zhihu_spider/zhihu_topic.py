import urllib.request
from bs4 import BeautifulSoup
import http
url = 'https://www.zhihu.com/topic/19776749/organize/entire'

zhihu_html = urllib.request.urlopen(url)
zhihu_soup = BeautifulSoup(zhihu_html,'lxml')
topic = zhihu_soup.find_all(name='ul',attrs={'class':'zm-topic-organize-list'})
print(zhihu_soup)
print(topic)
