import requests
import bs4
from selenium import webdriver

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#driver = webdriver.Chrome('e:\chromedriver.exe', chrome_options=chrome_options)
driver = webdriver.Chrome('e:\chromedriver.exe')
url = "http://1024.skswk9.pw/pw/thread.php?fid=3"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__cfduid=dca3abd512615187557755e6e4c9b91e61509545168; aafaf_ol_offset=97; aafaf_readlog=%2C734300%2C; '
              'visid_incap_1237688=Pbqrd0t6RpK+1Ohe33h27jo+GVoAAAAAQUIPAAAAAADmt0J0AR4HdbpKp/rlaoR5; incap_ses_636_1237'
              '688=bh4CdSpO9UuhzcU3CofTCDo+GVoAAAAArEuaH5QVGCELxwPVoGOb5g==; aafaf_lastpos=F17; aafaf_lastvisit=341%091'
              '511603847%09%2Fpw%2Fthread.php%3Ffid%3D17; aafaf_threadlog=%2C3%2C17%2C; a0888_pages=2; a0888_times=3; _'
              '_tins__17810888=%7B%22sid%22%3A1511603755874%2C%22vd%22%3A2%2C%22expires%22%3A1511605561640%7D; __51cke_'
              '_=; __51laig__=2',
    'Upgrade-Insecure-Requests': '1',
    'Host': '1024.skswk9.pw',
    'Referer': 'http://1024.skswk9.pw/pw/thread.php?fid=3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
r = requests.get(url, headers=headers).content
soup = bs4.BeautifulSoup(r, 'html5lib')
tag = soup.find_all('a', attrs={'href': True, 'id': True})
for tag in tag:
<<<<<<< HEAD
        if ('騎兵' in tag.string) or ('动漫' in tag.string) or ('有碼' in tag.string) or ('灣搭' in tag.string):
            url = 'http://1024.skswk9.pw/pw/' + tag['href']
            r = requests.get(url,headers=headers).content
            soup = bs4.BeautifulSoup(r,'html5lib')
            tag = soup.find('div',attrs={'class':"tpc_content",'id':"read_tpc"}).find_all('a',attrs={'href':True,'target':"_blank"})
            for tag in tag:
                if tag.string is not None:
                    print(tag)
                    print(tag.string)
                    break
                    driver.get(tag['href'])
                    r = driver.find_element_by_xpath('//*[@id="down_btn"]').click()
                    with open('1.torrent','wb') as f:
                        f.write(r.content)
                    print(tag)
                    break
            break
=======
    if ('騎兵' in tag.string) or ('动漫' in tag.string) or ('有碼' in tag.string) or ('灣搭' in tag.string):
        url = 'http://1024.skswk9.pw/pw/' + tag['href']
        r = requests.get(url, headers=headers).content
        soup = bs4.BeautifulSoup(r, 'lxml')
        tag = soup.find('div', attrs={'class': "tpc_content", 'id': "read_tpc"}).\
            find_all('a', attrs={'href': True, 'target': "_blank"})
        for tag_ in tag:
            if (tag_.string is not None) and (tag_.string != '點擊進入下載'):
                print(tag_.string)
                driver.get(tag_['href'])
                driver.find_element_by_id('down_btn').click()
                driver.quit()
                break
        break
>>>>>>> eee99940569d397daedf2a02992adf5ae4ad1baf
