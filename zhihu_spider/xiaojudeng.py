from bs4 import BeautifulSoup
import requests
s = requests.session()
url = 'http://www.iivd.net/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
password = {'username':'juvenbaby','password':'bnm1235'}
zhihu_html_1 = s.post(url,headers=headers,data=password)

zhihu_html = s.get('http://www.iivd.net',headers=headers)
zhihu_soup = BeautifulSoup(zhihu_html.content,'html5lib')
print(zhihu_soup)
topic = zhihu_soup.find(name='a',attrs={'href':True,'target':'_blank','title':'访问我的空间'})
print(topic.string)

#fastloginfield:username
#username:juvenbaby
#password:bnm1235
#cookietime:2592000
#quickforward:yes
#handlekey:ls
#<a href="http://www.iivd.net/home.php?mod=space&amp;uid=6682"
#target="_blank" title="访问我的空间">juvenbaby</a>
