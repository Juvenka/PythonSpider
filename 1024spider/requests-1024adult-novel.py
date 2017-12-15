import requests
import os
import bs4
import time
start =time.clock()

#中间写上代码块

firsturl = "http://1024.2048xd.info/pw/thread.php?fid=17"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__cfduid=dca3abd512615187557755e6e4c9b91e61509545168; aafaf_ol_offset=97; aafaf_readlog=%2C734300%2C; visid_incap_1237688=Pbqrd0t6RpK+1Ohe33h27jo+GVoAAAAAQUIPAAAAAADmt0J0AR4HdbpKp/rlaoR5; incap_ses_636_1237688=bh4CdSpO9UuhzcU3CofTCDo+GVoAAAAArEuaH5QVGCELxwPVoGOb5g==; aafaf_lastpos=F17; aafaf_lastvisit=341%091511603847%09%2Fpw%2Fthread.php%3Ffid%3D17; aafaf_threadlog=%2C3%2C17%2C; a0888_pages=2; a0888_times=3; __tins__17810888=%7B%22sid%22%3A1511603755874%2C%22vd%22%3A2%2C%22expires%22%3A1511605561640%7D; __51cke__=; __51laig__=2',
    'Upgrade-Insecure-Requests': '1',
    'Host': '1024.skswk9.pw',
    'Referer': 'http://1024.skswk9.pw/pw/thread.php?fid=3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
URL = requests.get(firsturl, headers=headers, timeout=None)
html_web = bs4.BeautifulSoup(URL.content, 'html5lib')
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
halfTybe = num[input()].parent['href']
Tybe = Referer + halfTybe
Tybe_open = requests.get(Tybe, headers=headers, timeout=3)
Tybe_page = bs4.BeautifulSoup(Tybe_open.content, 'html5lib', from_encoding='UTF-8')
tar_tag = Tybe_page.find_all(name='a', attrs={'href': True, 'id': True})
i = 0
if not os.path.exists('C:\\Users\\Administrator\\Desktop\\erotic_novels'):
    os.mkdir('C:\\Users\\Administrator\\Desktop\\erotic_novels')
for tar in tar_tag:
    if tar.parent.parent.find('img') is not None:
        continue
    else:
        i += 1
        try:
            erotic_novel_open = requests.get(Referer + tar['href'], headers=headers, timeout=2)
            erotic_novel_html = bs4.BeautifulSoup(erotic_novel_open.content, 'html5lib', from_encoding='UTF-8')
            novel = erotic_novel_html.find(name='div', attrs={'class': 'tpc_content', 'id': 'read_tpc'})
        except requests.ConnectionError as e:
            print(e)
            continue
        except requests.Timeout as e:
            print(e)
            continue
        f = open('C:\\Users\\Administrator\\Desktop\\erotic_novels' + os.sep + tar.string + '.txt', 'w')
        for nov in novel.strings:
            nov = nov.replace('\xa0', ' ')
            nov = nov.replace('\ue0ff', ' ')
            nov = nov.replace('\ue197', ' ')
            nov = nov.replace('\ue1d2', ' ')
            nov = nov.replace('\ue4c6', ' ')
            try:
                f.write('  '+nov+'\n\n')
            except UnicodeEncodeError as e:
                print(e)
                continue
        f.close()
        print('第'+str(i)+'篇'+tar.string+'下载完毕')
print('第一页'+str(i)+'下载完')
end = time.clock()
print('Running time: %s Seconds'%(end-start))
