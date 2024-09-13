from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com')
driver.implicitly_wait(5)

tfld_username=driver.find_element(By.ID,'user-name')
tfld_username.send_keys('standard_user')

tfld_password=driver.find_element(By.ID,'password')
tfld_password.send_keys('secret_sauce')

btn_login=driver.find_element(By.ID,'login-button')
btn_login.click()
time.sleep(10)

btn_add_to_cart=driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack')
btn_add_to_cart.click()
time.sleep(10)

btn_basket=driver.find_element(By.CSS_SELECTOR,'a.shopping_cart_link')
btn_basket.click()
#btn_basket.
lbl_item=driver.find_element(By.CSS_SELECTOR,'div.inventory_item_name')
lbl_text=lbl_item.text
if(lbl_text=='Sauce Labs Backpack'):
    print()
else:
    print(lbl_text, 'error-test failed!')
btn_checkout=driver.find_element(By.ID, 'checkout')
btn_checkout.click()
time.sleep(5)
tfld_first_name= driver.find_element(By.ID,'first-name')
tfld_first_name.send_keys('John')

tfld_last_name= driver.find_element(By.ID,'last-name')
tfld_last_name.send_keys('Doe')
tfld_zip=driver.find_element(By.ID,'postal-code')
tfld_zip.send_keys('1934')
btn_continue=driver.find_element(By.ID,'continue')
btn_continue.click()
time.sleep(5)

btn_finish=driver.find_element(By.ID,'finish')
btn_finish.click()
time.sleep(5)
lbl_complete_header=driver.find_element(By.CSS_SELECTOR,'h2.complete-header')
lbl_complete_text=driver.find_element(By.CSS_SELECTOR,'div.complete-text')
time.sleep(5)
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















