import requests
import bs4
import os

url = "http://1024.skswk9.pw/pw/simple/index.php?f3.html"
headers = {
    'Host': '1024.skswk9.pw',
    'Referer': 'http://1024.skswk9.pw/pw/simple/index.php?f3.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
if not os.path.exists('C:\\Users\\Administrator\\Desktop\\torrent'):
    os.mkdir('C:\\Users\\Administrator\\Desktop\\torrent')
r = requests.get(url, headers=headers).content
soup = bs4.BeautifulSoup(r, 'html5lib')
tag = soup.find_all('li')
x = 0
y = 0
z = 0
for i in tag:
    i = i.find('a')
    if ('骑兵' in i.string) or ('騎兵' in i.string) or ('动漫' in i.string) or ('有碼' in i.string) or ('灣搭' in i.string):
        url = 'http://1024.skswk9.pw/pw/' + i['href']
        r = requests.get(url, headers=headers).content
        soup = bs4.BeautifulSoup(r, 'lxml')
        tag_ = soup.find('td', attrs={'colspan': '2','class': 'tpc_content'}).\
            find_all('a', attrs={'href': True, 'target': "_blank"})
        for i_ in tag_:
            if (i_.string is not None) and (i_.string != '點擊進入下載'):
                print(i_.string)
                break
