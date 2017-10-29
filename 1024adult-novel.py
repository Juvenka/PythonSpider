import urllib.request
import bs4
import collections
import os

firsturl = "http://1024.2048xd.info/pw/thread.php?fid=17"
will_see = collections.deque()
saw = set()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

URL = urllib.request.Request(firsturl,headers = headers)
h = urllib.request.urlopen(URL)
html_web = bs4.BeautifulSoup(h,'html5lib',from_encoding='UTF-8')
target = html_web.find_all(name='a',attrs={'class':'a2 fn'})
i = 1
Referer = 'http://1024.2048xd.info/pw/'
num = dict()
print('客人想看点什么？我们有:')

for t in target:
    print(str(i)+'、'+t.string)
    num[str(i)] = t.string
    i += 1
print('请输入序号：',end=' ')

halfTybe = num[input()].parent['href']
Tybe = Referer + halfTybe
Tybe_url = urllib.request.Request(Tybe,headers=headers)
Tybe_open = urllib.request.urlopen(Tybe_url)
Tybe_page = bs4.BeautifulSoup(Tybe_open,'html5lib', from_encoding='UTF-8')
tar_tag = Tybe_page.find_all(name='a',attrs={'href':True,'id':True})
i = 0
if not os.path.exists('E:\\1024novels'):
    os.mkdir('E:\\1024novels')
for tar in tar_tag:
    i += 1
    if i<=6:
        continue
    else:
        f = open('E:\\1024novels'+os.sep+ tar.string + '.txt', 'w')
        erotic_novel = urllib.request.Request(Referer+tar['href'],headers=headers)
        erotic_novel_open = urllib.request.urlopen(erotic_novel)
        erotic_novel_html = bs4.BeautifulSoup(erotic_novel_open,'lxml',from_encoding='UTF-8')

        novel = erotic_novel_html.find(name='div',attrs={'class':'tpc_content','id':'read_tpc'})
        for nov in novel.stripped_strings:
            f.write('    '+nov.replace(u'\xa0', u' ')+'\n')
        f.close()
        print('第'+str(i-6)+'篇下载完毕')
print('第一页'+str(i-6)+'下载完')
