from bs4 import BeautifulSoup
import requests
import re
import progressbar
import time
import csv
import pickle
from get_serp import *


url = "https://www.google.com.tw/search?q=%E5" #search query of the keyword
page_count = 0
bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength) 
serp_list = []

while True:
    text = requests.get(url).text
    soup = BeautifulSoup(text, "html.parser")
    
    get_title(soup, serp_list)
    url = next_page(soup)
    if url != None:
        page_count += 1
        bar.update(page_count)
        if page_count % 4 == 0:
            time.sleep(60*1)
    else:
        break
            
            
f = open('google_serp.csv', 'w')
w3 = csv.writer(f)
w3.writerows(serp_list)

with open("google_serp_pickle.txt", "wb")as c:
    pickle.dump(serp_list, c)
