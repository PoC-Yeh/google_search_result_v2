from bs4 import BeautifulSoup
import requests
import re
import progressbar
import time
import csv
import pickle
from get_serp import *


def crawl(url, filename):
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
            
    return(serp_list)

    f = open('gs_{}.csv'.format(filename), 'w')
    w3 = csv.writer(f)
    w3.writerows(serp_list)
    
    with open("gs_{}_pickle.txt".format(filenmae), "wb")as c:
        pickle.dump(serp_list, c)
