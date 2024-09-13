import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import dotenv
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
print(dotenv_path)
print("selenium==", selenium.__version__)

BROWSER=os.getenv("BROWSER")
if BROWSER=="1":
   print(f"{BROWSER} BROWSER Chrome")
   driver=webdriver.Chrome() 
elif BROWSER=="2":
    driver=webdriver.Firefox()
    print(f"{BROWSER} BROWSER Chrome")
elif BROWSER=="3":
    driver=webdriver.Edge() 
    print(f"{BROWSER} BROWSER EDGE")
elif BROWSER=="4":
    driver=webdriver.Safari()
    print(f"{BROWSER} BROWSER SAFARI")
    
else:
    driver=webdriver.Chrome() 
    print(f"{BROWSER} default BROWSER Chrome")   
#driver=webdriver.Firefox()
#driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com')
driver.implicitly_wait(5)

tfld_username=driver.find_element(By.ID,'user-name')
tfld_username.send_keys('standard_user')

tfld_password=driver.find_element(By.ID,'password')
tfld_password.send_keys('secret_sauce')

btn_login=driver.find_element(By.ID,'login-button')
btn_login.click()
#time.sleep(10)
EC.element_to_be_clickable

btn_add_to_cart=driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(btn_add_to_cart))

btn_add_to_cart.click()
#time.sleep(10)


btn_basket=driver.find_element(By.CSS_SELECTOR,'a.shopping_cart_link')
WebDriverWait(driver,20).until(EC.element_to_be_clickable(btn_basket))
btn_basket.click()
#btn_basket.
lbl_item=driver.find_element(By.CSS_SELECTOR,'div.inventory_item_name')
WebDriverWait(driver,25).until(EC.visibility_of(lbl_item))
lbl_text=lbl_item.text

if(lbl_text=='Sauce Labs Backpack'):
    print()
else:
    print(lbl_text, 'error-test failed!')

btn_checkout=driver.find_element(By.ID, 'checkout')
WebDriverWait(driver,25).until(EC.element_to_be_clickable(btn_checkout))
btn_checkout.click()
#time.sleep(5)
#WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(),driv)
tfld_first_name= driver.find_element(By.ID,'first-name')
WebDriverWait(driver,20).until(EC.visibility_of(tfld_first_name))
tfld_first_name.send_keys('John')

tfld_last_name= driver.find_element(By.ID,'last-name')
tfld_last_name.send_keys('Doe')
tfld_zip=driver.find_element(By.ID,'postal-code')
tfld_zip.send_keys('1934')

btn_continue=driver.find_element(By.ID,'continue')
WebDriverWait(driver,20).until(EC.element_to_be_clickable(btn_continue))
btn_continue.click()
#time.sleep(5)

btn_finish=driver.find_element(By.ID,'finish')
WebDriverWait(driver,20).until(EC.element_to_be_clickable,btn_finish)
btn_finish.click()
#time.sleep(5)

lbl_complete_header=driver.find_element(By.CSS_SELECTOR,'h2.complete-header')
lbl_complete_text=driver.find_element(By.CSS_SELECTOR,'div.complete-text')
#time.sleep(5)
header_txt=lbl_complete_header.text
delivery_txt=lbl_complete_text.text
response_str=f'''header_txt={header_txt}
delivery_txt={delivery_txt}
 '''
print(response_str)
if(header_txt== 'Thank you for your order!' and delivery_txt== 'Your order has been dispatched, and will arrive just as fast as the pony can get there!' ):
    print('OK, test passed')
else:
    print('Error, test failed')


#continue
#finish
#div.summary_total_label
#div.inventory_item_name
#div.complete-text   Your order has been dispatched, and will arrive just as fast as the pony can get there!
#h2.complete-header   Thank you for your order!
exit()















