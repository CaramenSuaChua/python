from selenium import webdriver
from time import sleep
import os 
import pandas as pd
import urllib.request
# from crawl.data_helpers import *
from bs4 import BeautifulSoup
#import webdrive broweser
browser = webdriver.Chrome(executable_path='./chromedriver')

for i in range(10):
    shop = 'genzofficial'
    urlpage = 'https://shopee.vn/' + shop + '?page='
    driver = browser # Khởi tạo Web Driver, nó sẽ show trình duyệt Firefox để crawl
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


# shop = 'genzofficial'
# url = 'https://shopee.vn/' + shop + 'page=0'
# print(url)
# browser.get(url)
# sleep(5)
# def get_product_one_page():
#     paqe_source = BeautifulSoup(browser.page_source)

#     parent_tag = paqe_source.find_all('div', class_ = 'shopee-searchbar-input' )

#     for results in parent_tag:
#         name_results = results.find_all('div', class_= '_16lgia _3UdQUf _3Q4n5M' )
#         price_results = results.find_all('div', class_='_2AKyiQ _1UJbfe')
#         link_results = results.find_all('div', class_ = 'col-xs-2 shop-collection-view__item')

#     list_product_names = []
#     list_product_price_current = []
#     list_product_link = []

#     for item in range(len(name_results)):
#         name_item  = name_results[item].text
#         price_item = price_results[item].text
#         link_item = link_results[item].text

#         list_product_names.append(name_item)
#         list_product_price_current.append(price_item)
#         list_product_link.append(link_item)
#         item = item + 1 

#     df = pd.DataFrame
#     df['name'] = list_product_names
#     df['price'] = list_product_price_current
#     df['link'] = list_product_link

#     return df 