# -*- coding: utf-8 -*-
import requests
import re

def crawler(sURL):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
    r = requests.get(sURL, headers = header)
    html = r.text
    linksList = re.findall('<a href=(.*?)>.*?</a>',html)
    for link in linksList:
        print link




if __name__ == "__main__":
    url = "http://panjin.dlut.edu.cn"
    crawler(url)