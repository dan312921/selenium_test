import os

import wget as wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

s=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=s)

driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
login = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")

username.clear()
password.clear()
username.send_keys('91415532')
password.send_keys('Dan12cat')
login.click()

search = WebDriverWait(driver, 150).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='搜尋']"))
)
keyword = "#dog"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
)

#scroll 3 time
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

#imgs = driver.find_elements_by_class_name("FFVAD")
imgs = driver.find_elements(By.CSS_SELECTOR, ".FFVAD")
path = os.path.join(keyword)
os.mkdir(path)

count = 0
for img in imgs:
    save_as = os.path.join(path, keyword + str(count) + '.jpg')
    # print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"), save_as)
    count += 1