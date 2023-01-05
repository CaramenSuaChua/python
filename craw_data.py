from selenium import webdriver
from time import sleep
import os 
import pandas as pd
import urllib.request
from data_helpers import DataObject
from bs4 import BeautifulSoup
#import webdrive broweser
browser = webdriver.Chrome(executable_path='./chromedriver')

for i in range(10):
    shop = 'genzofficial'
    urlpage = 'https://shopee.vn/' + shop + '?page='
    driver = browser # Khởi tạo Web Driver, nó sẽ show trình duyệt chrome để crawl
    driver.get(urlpage + str(i))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") # Đoạn scrip để scroll trang web

    name = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/a/div/div/div[2]/div[1]/div/div")
    data =[]
    for browse in name:
        text = browse.text
        data.append({"name" : text})
    
    for i in data:
        try:
            name = i["name"]
            try:
                data = DataObject().create( name = name)
            except OSError:
                print ("Creation of the image %s failed" )
            else:
                print ("Successfully created the image %s " )
        except:
            pass
    driver.quit()