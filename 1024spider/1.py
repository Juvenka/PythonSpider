from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#driver = webdriver.Chrome('e:\chromedriver.exe', chrome_options=chrome_options)
driver = webdriver.Chrome('e:\chromedriver.exe')
driver.get("http://www3.uptorrentfilespacedownhostabc.net/updowm/file.php/OZYDZ9m.html")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "down_btn"))
    )
    element.click()
finally:
    driver.close()
