from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd 
import urllib.request 
from time import sleep
import boto3
from selenium.webdriver.chrome.options import Options
import requests

class wallpaperScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("window-size=1400,1500")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("start-maximized")
        options.add_argument("enable-automation")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://4kwallpapers.com/black-dark/steve-jobs-theater-apple-park-modern-architecture-colorful-4450.html')
        self.bucket = boto3.resource('s3').Bucket('aicore-prac')
        sleep(3)

    def get_wallpaper(self):
        wallpaper_element = self.driver.find_element_by_xpath('//img[@itemprop="contentUrl"]')
        url = wallpaper_element.get_attribute('src')
        img_data = requests.get(url).content
        with open('Apple_Park_Wallpaper.jpg', 'wb') as handler:
            handler.write(img_data)
        self.bucket.upload_file('./Apple_Park_Wallpaper.jpg', 'Apple_Park_Wallpaper.jpg')
        self.driver.quit()

scraper = wallpaperScraper()
scraper.get_wallpaper()