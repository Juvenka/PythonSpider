import urllib.request
import bs4
import collections

firsturl = ["http://1024.2048xd.info/pw/htm_data/3/1710/835746.html"]
will_see = collections.deque(firsturl)
saw = set()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

while True:
    web = will_see.popleft()
    if web not in saw:
        urlop = urllib.request.Request(web,headers = headers)
    else:
        continue

    h = urllib.request.urlopen(urlop)
    saw.add(web)
    html_web = bs4.BeautifulSoup(h,'lxml',from_encoding='UTF-8')
    target = html_web.find(name='div',attrs={'class':'tpc_content','id':'read_tpc'}).find_all(name='img',attrs={'border':'0'})
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
