import urllib.request
import bs4
import os
url= 'http://pc.feahh.cn/index.html?c=XH041&1=1&referer=http://4gjy.com/'

headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
URL = urllib.request.Request(url, headers=headers)
h = urllib.request.urlopen(URL)
html_web = bs4.BeautifulSoup(h,'xml')
target = html_web.find_all('img')
print(target)
i=1
if not os.path.exists('D:\\pic'):
    os.mkdir('D:\\pic')
for pic in target:
    if 'http' in pic['src']:
        urllib.request.urlretrieve(pic['src'],'D:\\pic'+os.sep+str(i)+'.jpg')
        print('第'+str(i)+'张下载完')
        i +=1
    else:
        continue
