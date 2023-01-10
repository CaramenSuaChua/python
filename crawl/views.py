from django.shortcuts import render
from selenium import webdriver
from time import sleep
import pandas as pd
from .models import Data
from rest_framework.views import APIView
from selenium.webdriver.common.by import By
# Create your views here.
import json

class get_products:
    browser = webdriver.Chrome(executable_path='./chromedriver')

    for i in range(1):
        shop = 'collections/aztec'
        urlpage = 'https://www.amazstyle.com/' + shop + '?page='
        driver = browser # Khởi tạo Web Driver, nó sẽ show trình duyệt chrome để crawl
        driver.get(urlpage + str(i))
    
        data_name =[]
        data_price =[]
        data_link =[]
        data_img =[]
        # sleep(5)
        # ================================ GET name products
        list_name = driver.find_elements(By.TAG_NAME, "span")
        for name in list_name:
            if name.get_attribute("itemprop") == "name":
                data_name.append({'name' : name.text})
        # ================================ GET price products
        list_price = driver.find_elements(By.TAG_NAME, "span")
        for price in list_price:
            if price.get_attribute("class") == "has-text-weight-medium money money-original cl-black":
                data_price.append({'price':price.text})
        # ================================ GET description products
        list_links = driver.find_elements(By.TAG_NAME, "a")
        for link in list_links:
            if link.get_attribute("class") == ":hover-no-underline d-block":
                data_link.append({'link': link.get_attribute("href")})

        # ================================ GET img products
        list_img = driver.find_elements(By.TAG_NAME, "img")
        for price in list_img:
            if price.get_attribute("class") == "image sb-lazy priority":
                data_img.append({'image': price.get_attribute("src")})

        print("=====================================")
        print(data_name, "=====================================")
        print("=====================================")

        x = zip(data_name, data_price, data_link, data_img)
        data = json.dumps(tuple(x))
        print(data , '=======+++++++++++++++++++++++==------------------------')

        
    sleep(5)
    driver.quit()

