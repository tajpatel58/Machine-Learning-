#%% 
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 

driver = webdriver.Safari()

cat_num = '9340039'

driver.get('https://www.argos.co.uk')

sleep(1)

driver.set_window_size(1200,1200)

cookies_button = driver.find_element_by_id("consent_prompt_submit")

sleep(1)

cookies_button.click()

sleep(1)

search = driver.find_element_by_id("searchTerm")
search.send_keys(cat_num)
search.send_keys(Keys.RETURN)

sleep(8)


post_code_box = driver.find_element_by_id("search")
post_code_box.send_keys("staples corner")

sleep(6)

check_button = driver.find_element_by_xpath('//button[@data-test="fulfilment-search-stock-search-button"]')

sleep(1)

check_button.click()

sleep(6)

select_staples_corner = driver.find_element_by_xpath('//button[@data-test="store-selector-att-button-button"]')
select_staples_corner.click()

sleep(5)

go_to_trolley = driver.find_element_by_xpath('//a[@data-test="component-att-button-basket"]')
go_to_trolley.click()

sleep(5)
"""
continue_without_insurance = driver.find_element_by_xpath('//*[@id="content"]/main/div[1]/div[3]/div[1]/section[2]/section/div[12]/div/div/div[1]/footer/div/div/a')
continue_without_insurance.click()

sleep(5)
"""

pay_now = driver.find_element_by_xpath('//button[@data-e2e="continue-with-collection-button"]')
pay_now.click()

sleep(3)

login_email = driver.find_element_by_xpath('//*[@id="email"]')
login_email.send_keys('tajpatel58@gmail.com')

password_box = driver.find_element_by_xpath('//*[@id="password"]')
password_box.send_keys('Taj290898')

sign_in = driver.find_element_by_xpath('//button[@data-e2e="login-submit-button"]')
sign_in.click()

sleep(3) 

promo_code = driver.find_element_by_xpath('//h2[@data-test="component-title"]')
promo_code.click()

sleep(3)

discount_box = driver.find_element_by_xpath('//*[@id="promoReference"]')
discount_box.send_keys('DISCOUNT')
discount_box.send_keys(Keys.RETURN)

sleep(8)

choose_payment = driver.find_element_by_xpath('//button[@data-test="choose-payment-button"]')
choose_payment.click()

sleep(10)

cvc = driver.find_element_by_xpath('//input[@id="hps-cvv"]')

sleep(3)

cvc.send_keys('976')

pay_button = driver.find_element_by_xpath('//input[@id="hps-continue"]')
pay_button.click()


# %%


# %%
