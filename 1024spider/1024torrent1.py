#http://9453hot.com/forum-41-1.html

import requests
import bs4
from selenium import webdriver

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#driver = webdriver.Chrome('D:\chromedriver.exe',chrome_options=chrome_options)
driver = webdriver.Chrome('D:\chromedriver.exe')
url = "http://9453hot.com/forum-41-1.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
r = requests.get(url,headers=headers).content
soup = bs4.BeautifulSoup(r,'html5lib')
tag = soup.find_all('a',attrs={'href':True,'onclick':"atarget(this)"})
print(tag)
for tag in tag:
        if ('騎兵' in tag.string) or ('动漫' in tag.string) or ('有碼' in tag.string) or ('灣搭' in tag.string):
            url = 'http://9453hot.com/' + tag['href']
            r = requests.get(url,headers=headers).content
            soup = bs4.BeautifulSoup(r,'html5lib')
            tag = soup.find('div',attrs={'class':"tpc_content",'id':"read_tpc"}).find_all('a',attrs={'href':True,'target':"_blank"})
            for tag in tag:
                if tag.string is not None:
                    print(tag.string)
                    driver.get(tag['href'])
                    r = driver.find_element_by_xpath('//*[@id="btnDownload"]').click()
                    with open('1.torrent','wb') as f:
                        f.write(r.content)
                    print(tag)
                    break
            break

