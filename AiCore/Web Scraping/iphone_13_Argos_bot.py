#%% 
import requests 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 

driver = webdriver.Safari()

driver.get('https://www.argos.co.uk/product/9520103?clickSR=slp:term:iphone%2013:3:64:1')

driver.set_window_size(1200,1200)

cookies_button = driver.find_element_by_id("consent_prompt_submit")
cookies_button.click()

post_code_box = driver.find_element_by_id("search")
post_code_box.send_keys("NW2 6LW")
post_code_box.send_keys(Keys.RETURN)

sleep(6)

select_store = driver.find_element_by_xpath('//*[@id="content"]/main/div[1]/div[3]/div[1]/section[2]/section/div[10]/div[2]/div[2]/div[5]/button')
select_store.click()

sleep(6)

add_to_trolley = driver.find_element_by_xpath('//*[@id="content"]/main/div[1]/div[3]/div[1]/section[2]/section/div[10]/div[2]/div/div[7]/button/span/span')
add_to_trolley.click()


sleep(6)

go_to_trolley = driver.find_element_by_xpath('//*[@id="content"]/main/div[1]/div[3]/div[1]/section[2]/section/div[13]/div/div/div[1]/footer/div/div[2]/a')
go_to_trolley.click()


"""
search = driver.find_element_by_id("searchTerm")

search.send_keys("iphone 13")
search.send_keys(Keys.RETURN)
"""

sleep(6)
driver.quit()
#product_tag = driver.find_element('paste xpath in')


# Gets all text within this output. // means anywehre on the page, 
# * means any tag. /a (means within an a-tag). article[@class='class tag']
# Within tags we have attributes that have names and we can access. 
# one slash / means from where we are, // says anywhere within that
# html block. Use the get_attribute method on 
#print(product_tag.text)
# %%
