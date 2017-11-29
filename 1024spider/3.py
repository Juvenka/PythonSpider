import requests
import bs4

headers = {
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
'Cookie': '__cfduid=d0497e3f785a62ad6020160c209a7f7161511853230; a4184_pages=4; a4184_times=2; __tins__18654184=%7B%22s'
          'id%22%3A1511934196373%2C%22vd%22%3A2%2C%22expires%22%3A1511936829816%7D; __51cke__=; __51laig__=2',
}
data = {'type': 'torrent', 'id': 'OZYDZ9m', 'name': 'ABP660'}
r = requests.post('http://www3.uptorrentfilespacedownhostabc.net/updowm/down.php',data=data, headers=headers).content
with open('1.torrent','wb') as f:
    f.write(r)

#r = bs4.BeautifulSoup(r, 'html5lib')
#print(r)


#?type=torrent&id=OZYDZ9m&name=ABP660
