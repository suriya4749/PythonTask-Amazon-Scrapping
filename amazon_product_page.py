# coding=utf-8
__author__ = 'suriyakumar.s2'

# Import Functions

import demjson, random
import requests, re, json, sys, helper
from bs4 import BeautifulSoup
from meta_functions import *
reload(sys)
sys.setdefaultencoding('UTF-8')

######importing meta_functions for removing the character from the attributes ########

# Main Class

class amazon_product_page():

    ##extractor function###

    def data_extractor(self, soup,source):
        dataList, dataDict, hitUrl = [], {}, url
        dataDict['product_url'] = hitUrl
        dataDict['product_name'] = soup.select('#productTitle')[0].text.strip() if soup.select('#productTitle') else 'n/a'
        price = soup.select('.a-button.a-button-selected.a-spacing-mini.a-button-toggle.format span')[0].text.strip() if soup.select('.a-button.a-button-selected.a-spacing-mini.a-button-toggle.format span') else 'n/a'
        dataDict['regular_price'] = re.findall('\d+\W+\d+',str(price))[0]
        prodDetails1 = soup.select('#detailBullets_feature_div ul li .a-list-item')
        prodList = []
        for val1 in prodDetails1:
            d1 = remove_meta_char(val1.text.strip())
            prodList.append(d1)
        dataDict['product_details'] = '#||#'.join(prodList)
        dataDict['product_image'] = soup.select('#img-wrapper #img-canvas img')[0].get('src') if soup.select('#img-wrapper #img-canvas img') else 'n/a'
        ###### Getting product_id #######
        prod_id = hitUrl
        if "dp/" in prod_id :
            dataDict['product_id'] = re.findall("dp/([0-9A-za-z]*)",prod_id)[0]
        elif soup.select('#ASIN') :
            dataDict['product_id'] = soup.select('#ASIN')[0]['value']
        elif prod_id:
            dataDict['product_id'] = prod_id.split('/')[-1]
        if len(dataDict) > 0: dataList.append(dataDict)
        return dataList


# Parse Function

def parse(source):
    soup = BeautifulSoup(source)
    amazon_product_page_object = amazon_product_page()
    output = amazon_product_page_object.data_extractor(soup,source)
    print output
    return [output]


# Main Function

if __name__ == "__main__":
    #amazon_fr
    url = 'https://www.amazon.fr/dp/000103863X'
    ########for creating random number in session-id it will consider uniques part for every url so it will bypass the captcha############
    randNum = random.randint(1000000,9999999)
    cookie = 'session-id=262-{}-{};'.format(str(randNum),str(randNum))
    header = {"Cookie":cookie,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}
    source = requests.get(url,headers=header).content
    # source = open("dump.html", "r").read()
    parse(source)