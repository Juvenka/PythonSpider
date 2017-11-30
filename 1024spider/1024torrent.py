import requests
import bs4
import os
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome('D:\chromedriver', chrome_options=chrome_options)
# driver = webdriver.Chrome('D:\chromedriver')
url = "http://1024.skswk9.pw/pw/thread.php?fid=3"
headers1 = {
    'Host': 'www3.uptorrentfilespacedownhostabc.net',
    'Connection': 'keep-alive',
    'Content-Length': '35',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://www3.uptorrentfilespacedownhostabc.net',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 '
                  'Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://www3.uptorrentfilespacedownhostabc.net/updowm/file.php/OZYDZ9m.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '__cfduid=d0497e3f785a62ad6020160c209a7f7161511853230; a4184_pages=4; a4184_times=2; __tins__18654184='
              '%7B%22sid%22%3A1511934196373%2C%22vd%22%3A2%2C%22expires%22%3A1511936829816%7D; __51cke__=; __51laig__=2'
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Host': '1024.skswk9.pw',
    'Referer': 'http://1024.skswk9.pw/pw/thread.php?fid=3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
if not os.path.exists('C:\\Users\\Administrator\\Desktop\\torrent'):
    os.mkdir('C:\\Users\\Administrator\\Desktop\\torrent')
r = requests.get(url, headers=headers).content
soup = bs4.BeautifulSoup(r, 'html5lib')
tag = soup.find_all('a', attrs={'href': True, 'id': True})
for tag in tag:
    if ('骑兵' in tag.string) or ('騎兵' in tag.string) or ('动漫' in tag.string) \
            or ('有碼' in tag.string) or ('灣搭' in tag.string):
        url = 'http://1024.skswk9.pw/pw/' + tag['href']
        r = requests.get(url, headers=headers).content
        soup = bs4.BeautifulSoup(r, 'lxml')
        tag = soup.find('div', attrs={'class': "tpc_content", 'id': "read_tpc"}).\
            find_all('a', attrs={'href': True, 'target': "_blank"})
        for tag_ in tag:
            if (tag_.string is not None) and (tag_.string != '點擊進入下載'):
                r = requests.get(tag_['href']).content
                soup = bs4.BeautifulSoup(r, 'html5lib')
                tag_id = soup.find('input', attrs={'id': 'id'})
                tag_name = soup.find('input', attrs={'id': 'name'})
                data = {'type': 'torrent', 'id': tag_id['value'], 'name': tag_name['value']}
                r = requests.post('http://www3.uptorrentfilespacedownhostabc.net/updowm/down.php',
                                  data=data, headers=headers1)
                with open('C:\\Users\\Administrator\\Desktop\\torrent\\' + tag_name['value'] + '.torrent', 'wb') as f:
                    f.write(r.content)
