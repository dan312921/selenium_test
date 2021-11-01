import pandas as pd
from Tools.scripts.dutree import display
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

driver.get("https://www.trivago.hk/")

# driver.find_element_by_xpath("//body").click()

elem=driver.find_element(By.CSS_SELECTOR,"#querytext")
elem.clear()
elem.send_keys("香港")
elem.send_keys(Keys.RETURN)
# driver.find_element_by_xpath("//body").click()

time.sleep(3)

elem1=driver.find_element(By.CSS_SELECTOR,".btn.btn--primary.btn--regular.search-button.js-search-button")
elem1.click()

# elem=driver.find_element(By.CSS_SELECTOR,"svg")
# elem.send_keys(Keys.RETURN)   #how click 2 time
# elem.send_keys(Keys.RETURN)

time.sleep(3)

hotel_list = []

while True:
    i=0
    for hotel in driver.find_elements(By.CSS_SELECTOR, '.item-list>ol>li[id]'):

        star=hotel.find_element(By.CSS_SELECTOR,"div[class='stars-wrp']>meta").get_attribute('content')
        rating=hotel.find_element(By.CSS_SELECTOR,".item-components__pillValue--8d8e0.item-components__value-sm--6bc47.item-components__pillValue--8d8e0").text
        name = hotel.find_element(By.CSS_SELECTOR, ".item__name--link>h3").text
        # rating_number=hotel.find_element(By.CSS_SELECTOR,".rating-number").text
        price = hotel.find_element(By.CSS_SELECTOR, ".accommodation-list__prices--bf849>button>span>span[class='accommodation-list__price--f5d54']").text
        star=int(star)
        rating = float(rating)
        price=float(price[1:].replace(',',""))
        print(f' {name} {price} {star} {rating} ')

        i+=1
        if i>3:
           break
        hotel_list.append([name, price,star,rating])


#scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#next page doesnt work

 #   next_btn = driver.find_element(By.CSS_SELECTOR,
 #                                  "button[class='btn btn--pagination btn--small btn--page-arrow btn--next']")

  #  next_btn.click()

    try:
      next_btn = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(By.CSS_SELECTOR,
                                   "button[class='btn btn--pagination btn--small btn--page-arrow btn--next']"))

    finally:
         print("done")
         driver.close()

    next_btn.click()

pf=pd.DataFrame(hotel_list,columns=["name", "price","star","rating"])
print(pf)
# display(pf)
