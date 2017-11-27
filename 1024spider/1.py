from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#driver = webdriver.Chrome('e:\chromedriver.exe', chrome_options=chrome_options)
driver = webdriver.Chrome('e:\chromedriver.exe')
driver.get("http://www3.uptorrentfilespacedownhostabc.net/updowm/file.php/OZYDZ9m.html")
try:
    print(driver.current_url)
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "down_btn"))
    )
    element.click()
    print(driver.window_handles)
finally:
    driver.close()
    print(driver.window_handles)
