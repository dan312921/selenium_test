from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


s=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=s)

driver.get("https://www.price.com.hk/product.php?p=515226")
lowerest_price=driver.find_element(By.CSS_SELECTOR,".product-price>span[data-price]").text

lowerest_price=float(lowerest_price.replace(',',""))
print(lowerest_price)

product_list = driver.find_elements(By.CSS_SELECTOR,'.page-product>ul>li[id]')

for product in product_list:
  #price=product.find_element(By.CSS_SELECTOR,".item-inner>span[text-price-number]")
  price = product.find_element(By.CSS_SELECTOR, ".text-price-number").text
  price=float(price.replace(',',""))

  if price==lowerest_price:
    button=product.find_element(By.CSS_SELECTOR,".new_referral_btn")
    button.click()  #not work
    break


#input_box=driver.find_element(By.CSS_SELECTOR,".rf-form")
# input_box=driver.find_element(By.CSS_SELECTOR,".rf-order")
#input_name=input_box.find_element(By.ID,'#contact_name')
# input_name.send_keys("dan")

#x=driver.find_element(By.CSS_SELECTOR,".wrapper-contact-title>label[title_MR]")
#y=driver.find_element(By.CSS_SELECTOR,".rf-form-control-lower")

#x=driver.find_element(By.CSS_SELECTOR,".rf-form-control[手提電話]")