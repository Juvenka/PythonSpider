import urllib.request
import bs4
import collections

firsturl = "http://1024.2048xd.info/pw/thread.php?fid=17"
will_see = collections.deque()
saw = set()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

while True:
    URL = urllib.request.Request(firsturl,headers = headers)
    h = urllib.request.urlopen(URL)
    html_web = bs4.BeautifulSoup(h,'html5lib',from_encoding='UTF-8')
    target = html_web.find_all(name='a',attrs={'class':'a2 fn'})
    i = 1
    print('客人想看点什么？我们有:')
    for t in target:
        print(str(i)+'、'+t.string,end=' ')
        i += 1
    break
    i = 0
    for p in target:
        pic = urllib.request.Request(p['src'],headers = headers)
        sex_pic = urllib.request.urlopen(pic)
        i += 1
        f = open(str(i)+'.jpeg','wb')
        f.write(sex_pic.read())
        f.close()
        print('第'+str(i)+'张下载完成')
    if len(will_see) == 0:
        break
print('下载结束')
