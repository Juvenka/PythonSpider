from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('e:\chromedriver')
try:
    driver.get("http://www3.uptorrentfilespacedownhostabc.net/updowm/file.php/P00SFRg.html")
    WebDriverWait(driver, 1, 0.1).until(EC.element_to_be_clickable((By.ID, 'down_btn'))).click()
finally:
    driver.close()
