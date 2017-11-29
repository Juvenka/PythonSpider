from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#driver = webdriver.Chrome('d:\chromedriver.exe', chrome_options=chrome_options)
driver = webdriver.Chrome('e:\chromedriver.exe')
driver.set_page_load_timeout(5)
#driver.implicitly_wait(10)
#driver.execute_async_script('document.title')
#set_script_timeout(time_to_wait) - 在一个 execute_async_script 调用期间，设置脚本等待的时间
try:
    driver.get("http://www3.uptorrentfilespacedownhostabc.net/updowm/file.php/OZYDZ9m.html")
except TimeoutException as e:
    print(e)
driver.get_screenshot_as_file('C:\\Users\Administrator\Downloads\pic.png')

try:
    print(driver.current_url)
    element = WebDriverWait(driver, 9).until(
        expected_conditions.presence_of_element_located((By.ID, "down_btn"))
    )
    element.click()
    print(driver.window_handles)
finally:
    driver.close()
    print(driver.window_handles)
