#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep 
import requests 
import os 
import pandas as pd
#%% 

driver = webdriver.Safari()
driver.get('https://www.asos.com/men/fashion-feed/2018_10_22-mon/top-10-halloween/?ctaref=articles+related+stories')

product_tags = driver.find_elements(By.XPATH, '//div[@class="content"]//a')

for product_tag in product_tags:
    title = product_tag.get_attribute("text")
    price = int(title.split('£')[-1])
    print(price)
#%% 

path = f'{os.getcwd()}/ASOS_files'
# %%

product_images = driver.find_elements(By.XPATH, '//div[@class="image"]//img')

for index, image in enumerate(product_images):
    picture = image.get_attribute("src")
    img_data = requests.get(picture).content
    with open(f'{path}/Halloween_{index}.jpg', 'wb') as handler:
        handler.write(img_data)

# Getting around CAPATCHA, keeping all cookies with selenium. When we instantiate a webdriver, we can use a argument to specify the cookies. Cookies save on a 
# port. Need to store the port number. 

# %%
