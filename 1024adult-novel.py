import urllib.request
import bs4
import os
import socket
firsturl = "http://1024.2048xd.info/pw/thread.php?fid=17"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/61.0.3163.79 Safari/537.36'}

URL = urllib.request.Request(firsturl, headers=headers)
h = urllib.request.urlopen(URL)
html_web = bs4.BeautifulSoup(h, 'html5lib', from_encoding='UTF-8')
target = html_web.find_all(name='a', attrs={'class': 'a2 fn'})
i = 1
Referer = 'http://1024.2048xd.info/pw/'
num = dict()
print('客人想看点什么？我们有:')

for t in target:
    print(str(i)+'、'+t.string)
    num[str(i)] = t.string
    i += 1
print('请输入序号：', end=' ')
series = num[input()]
halfTybe = series.parent['href']
Tybe = Referer + halfTybe
Tybe_url = urllib.request.Request(Tybe, headers=headers)
Tybe_open = urllib.request.urlopen(Tybe_url)
Tybe_page = bs4.BeautifulSoup(Tybe_open, 'html5lib', from_encoding='UTF-8')
tar_tag = Tybe_page.find_all(name='a', attrs={'href': True, 'id': True})
i = 0
if not os.path.exists('C:\\Users\\Administrator\\Desktop\\erotic_novels'):
    os.mkdir('C:\\Users\\Administrator\\Desktop\\erotic_novels')
for tar in tar_tag:
    i += 1
    if i <= 6:
        continue
    else:
        f = open('C:\\Users\\Administrator\\Desktop\\erotic_novels' + os.sep + series + tar.string + '.txt', 'w')
        erotic_novel = urllib.request.Request(Referer+tar['href'], headers=headers)
        try:
            erotic_novel_open = urllib.request.urlopen(erotic_novel,timeout=10)
            erotic_novel_html = bs4.BeautifulSoup(erotic_novel_open, 'lxml', from_encoding='UTF-8')
            novel = erotic_novel_html.find(name='div', attrs={'class': 'tpc_content', 'id': 'read_tpc'})
        except socket.timeout as e:
            continue
        for nov in novel.stripped_strings:
            nov = nov.replace('\xa0' , ' ')
            nov = nov.replace('\ue0ff', ' ')
            nov = nov.replace('\ue197', ' ')
            f.write('    '+nov+'\n\n')
        f.close()
        print('第'+str(i-6)+'篇'+tar.string+'下载完毕')
print('第一页'+str(i-6)+'下载完')
