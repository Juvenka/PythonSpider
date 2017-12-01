import requests
import bs4
import os
from time import sleep
import requests.exceptions

url = "http://1024.skswk9.pw/pw/simple/index.php?f3.html"
headers1 = {
    'Host': 'www3.uptorrentfilespacedownhostabc.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 '
                  'Safari/537.36',}
headers2 = {
    'Host': 'www3.uptorrentfilespacedownhostabc.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 '
                  'Safari/537.36',
    'Origin': 'http://www3.uptorrentfilespacedownhostabc.net',
    'Content-Type': 'application/x-www-form-urlencoded'}
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
y = 0
for i in tag:
    i = i.find('a')
    if ('骑兵' in i.string) or ('騎兵' in i.string) or ('动漫' in i.string) or ('有碼' in i.string) or ('灣搭' in i.string):
        url = 'http://1024.skswk9.pw/pw/' + i['href']
        r = requests.get(url, headers=headers).content
        soup = bs4.BeautifulSoup(r, 'lxml')
        tag_ = soup.find('td', attrs={'colspan': '2','class': 'tpc_content'}).\
            find_all('a', attrs={'href': True, 'target': "_blank"})
        headers1['Referer'] = url
        for i_ in tag_:
            if (i_.string is not None) and (i_.string != '點擊進入下載'):
                r = requests.get(i_['href'],headers=headers1).content
                soup = bs4.BeautifulSoup(r, 'lxml')
                tag_id = soup.find('input', attrs={'id': 'id'})
                tag_name = soup.find('input', attrs={'id': 'name'})
                headers2['Referer'] = i_['href']
                data = {'type': 'torrent', 'id': tag_id['value'], 'name': tag_name['value']}
                r = requests.post('http://www3.uptorrentfilespacedownhostabc.net/updowm/down.php', data=data, headers=headers2, timeout=5)
                with open('C:\\Users\\Administrator\\Desktop\\torrent\\' + tag_name['value'] + '.torrent', 'wb') as f:
                    f.write(r.content)
                y += 1
                print(y)
                sleep(2)
print(headers1)
print(headers2)
