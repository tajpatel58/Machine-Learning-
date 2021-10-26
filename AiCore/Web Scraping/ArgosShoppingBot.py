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

sleep(3)

check_button = driver.find_element_by_xpath('//*[@id="content"]/main/div[1]/div[3]/div[1]/section[2]/section/div[9]/div/form/div/div/button')

sleep(1)

check_button.click()

sleep(4)

select_staples_corner = driver.find_element_by_xpath('//*[@id="content"]/main/div[1]/div[3]/div[1]/section[2]/section/div[9]/div[2]/div/div/div[1]/div/div[2]/div[3]/div/div/ol/li[1]/div/div[2]/button/span/span')
select_staples_corner.click()

sleep(2)

continue_without_insurance = driver.find_element_by_xpath('//*[@id="content"]/main/div[1]/div[3]/div[1]/section[2]/section/div[12]/div/div/div[1]/footer/div/div/a')
continue_without_insurance.click()

sleep(6)

pay_now = driver.find_element_by_xpath('//*[@id="basket-content"]/main/div[2]/section[3]/div[2]/div[1]/div/div/div/button/span[1]')
pay_now.click()

sleep(3)

login_email = driver.find_element_by_xpath('//*[@id="email"]')
login_email.send_keys('tajpatel58@gmail.com')

password_box = driver.find_element_by_xpath('//*[@id="password"]')
password_box.send_keys('Taj290898')

sign_in = driver.find_element_by_xpath('//*[@id="app"]/main/div/div/form/button/div/div[1]')
sign_in.click()

sleep(3) 

promo_code = driver.find_element_by_xpath('//*[@id="app-content"]/main/div/div/div[2]/div[3]/div[1]/a/div/section/div[1]/h2')
promo_code.click()

sleep(3)

discount_box = driver.find_element_by_xpath('//*[@id="promoReference"]')
discount_box.send_keys('DISCOUNT')
discount_box.send_keys(Keys.RETURN)

sleep(5)

payment_options = driver.find_element_by_xpath('//*[@id="app-content"]/main/div/div/div[2]/div[3]/div[4]/form/button')

payment_options.click()

sleep(20)

cvc = driver.find_element_by_xpath('//*[@class="hps-detail hps-mandatory"]')

sleep(3)

cvc.send_keys('976')

pay_button = driver.find_element_by_xpath('//*[@id="hps-continue"]')
pay_button.click()


# %%


# %%
