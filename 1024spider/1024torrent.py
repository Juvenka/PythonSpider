import requests.exceptions
import bs4
import os
import time
start = time.clock()
# 中间写上代码块
url = "http://1024.skswk9.pw/pw/simple/index.php?f3.html"
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 '
                  'Safari/537.36'}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 '
                  'Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'}
headers = {
    'Host': '1024.skswk9.pw',
    'Referer': 'http://1024.skswk9.pw/pw/simple/index.php?f3.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
if not os.path.exists('C:\\Users\Public\\torrent'):
    os.mkdir('C:\\Users\Public\\torrent')
r = requests.get(url, headers=headers).content
soup = bs4.BeautifulSoup(r, 'html5lib')
tag = soup.find_all('li')
y = 0
x = 0
for i in tag:
    i = i.find('a')
    if ('骑兵' in i.string) or ('騎兵' in i.string) or ('动漫' in i.string) or ('有碼' in i.string) or ('灣搭' in i.string):
        url = 'http://1024.skswk9.pw/pw/' + i['href']
        r = requests.get(url, headers=headers).content
        soup = bs4.BeautifulSoup(r, 'lxml')
        tag_ = soup.find('td', attrs={'colspan': '2', 'class': 'tpc_content'}).\
            find_all('a', attrs={'href': True, 'target': "_blank"})
        headers1['Referer'] = url
        x += 1
        print(x)
        for i_ in tag_:
            if (i_.string is not None) and (i_.string != '點擊進入下載'):
                if 'org' in i_.string:
                    url_ = 'http://www3.uptorrentfilespacedownhostabc.org/updowm/down.php'
                    headers1['Host'] = 'www3.uptorrentfilespacedownhostabc.org'
                    headers2['Host'] = 'www3.uptorrentfilespacedownhostabc.org'
                elif 'biz' in i_.string:
                    url_ = 'http://www3.uptorrentfilespacedownhostabc.biz/updowm/down.php'
                    headers1['Host'] = 'www3.uptorrentfilespacedownhostabc.biz'
                    headers2['Host'] = 'www3.uptorrentfilespacedownhostabc.biz'
                elif 'net' in i_.string:
                    url_ = 'http://www3.uptorrentfilespacedownhostabc.net/updowm/down.php'
                    headers1['Host'] = 'www3.uptorrentfilespacedownhostabc.net'
                    headers2['Host'] = 'www3.uptorrentfilespacedownhostabc.net'
                elif 'pw' in i_.string:
                    url_ = 'http://www3.uptorrentfilespacedownhostabc.pw/updowm/down.php'
                    headers1['Host'] = 'www3.uptorrentfilespacedownhostabc.pw'
                    headers2['Host'] = 'www3.uptorrentfilespacedownhostabc.pw'
                elif 'com' in i_.string:
                    url_ = 'http://www3.uptorrentfilespacedownhostabc.com/updowm/down.php'
                    headers1['Host'] = 'www3.uptorrentfilespacedownhostabc.com'
                    headers2['Host'] = 'www3.uptorrentfilespacedownhostabc.com'
                elif 'club' in i_.string:
                    url_ = 'http://www3.uptorrentfilespacedownhostabc.club/updowm/down.php'
                    headers1['Host'] = 'www3.uptorrentfilespacedownhostabc.club'
                    headers2['Host'] = 'www3.uptorrentfilespacedownhostabc.club'
                else:
                    url_ = 'http://www3.uptorrentfilespacedownhostabc.info/updowm/down.php'
                    headers1['Host'] = 'www3.uptorrentfilespacedownhostabc.info'
                    headers2['Host'] = 'www3.uptorrentfilespacedownhostabc.info'
                try:
                    r = requests.get(i_['href'], headers=headers1,timeout=1.5).content
                except requests.exceptions.ReadTimeout as e:
                    print(e)
                    continue
                except requests.exceptions.ConnectionError as e:
                    print(e)
                    continue
                soup = bs4.BeautifulSoup(r, 'lxml')
                tag_id = soup.find('input', attrs={'id': 'id'})
                tag_name = soup.find('input', attrs={'id': 'name'})
                headers2['Referer'] = i_['href']
                try:
                    data = {'type': 'torrent', 'id': tag_id['value'], 'name': tag_name['value']}
                    r = requests.post(url_, data=data, headers=headers2, timeout=5)
                    with open("C:\\Users\Public\\torrent\\" + tag_name['value'] + '.torrent', 'wb') as f:
                        f.write(r.content)
                    y += 1
                    print(y)
                except TypeError as e:
                    print(e)
                except requests.exceptions.ConnectionError as e:
                    print(e)
                except requests.exceptions.ReadTimeout as e:
                    print(e)
end = time.clock()
print('Running time: %s Seconds' % (end-start))
