from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#driver = webdriver.Chrome('d:\chromedriver.exe', chrome_options=chrome_options)
a = webdriver.Chrome('d:\chromedriver.exe')
#driver.implicitly_wait(10)
#driver.execute_async_script('document.title')
#set_script_timeout(time_to_wait) - 在一个 execute_async_script 调用期间，设置脚本等待的时间

a.get("http://www3.uptorrentfilespacedownhostabc.net/updowm/file.php/OZYDZ9m.html")
element = WebDriverWait(a, 2).until(expected_conditions.element_to_be_clickable((By.ID, "down_btn")))
element.click()
print(a.window_handles)

a.close()
print(a.window_handles)
#http://www3.uptorrentfilespacedownhostabc.net/updowm/down.php?type=torrent&id=OZYDZ9m&name=ABP660
#type=torrent&id=OZYDZ9m&name=ABP660
#http://www3.uptorrentfilespacedownhostabc.net/?type=torrent&id=OZYDZ9m&name=ABP660
