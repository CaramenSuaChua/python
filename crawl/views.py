from django.shortcuts import render
from selenium import webdriver
from time import sleep
import os 
import pandas as pd
import urllib.request
# from .data_helpers import DataObject

from bs4 import BeautifulSoup
from .models import Data
from rest_framework.views import APIView
# Create your views here.
class get_products(APIView):
    browser = webdriver.Chrome(executable_path='./chromedriver')

    for i in range(10):
        shop = 'genzofficial'
        urlpage = 'https://shopee.vn/' + shop + '?page='
        driver = browser # Khởi tạo Web Driver, nó sẽ show trình duyệt chrome để crawl
        driver.get(urlpage + str(i))
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") # Đoạn scrip để scroll trang web

        name = driver.find_elements('class="_16lgia _3Q4n5M"')
        data =[]
        for browse in name:
            text = browse.text
            data.append({"name" : text})
        print(data)
        for i in data:
            try:
                name = i["name"]
                try:
                    data = Data.objects.create(name=name)
                except OSError:
                    print ("Creation of the image %s failed" )
                else:
                    print ("Successfully created the image %s " )
            except Exception as e:
                print(e)
    driver.quit()