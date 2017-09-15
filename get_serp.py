from bs4 import BeautifulSoup
import requests
import re
import progressbar
import time


def get_title(soup, serp_list):
    all_results = soup.find_all("div", class_= "g")

    for result in all_results:
        title = result.find("h3")
        link = result.find("cite")
        description = result.find("span", class_ = "st")
        try:
            inside = [title.text, link.text, description.text.replace("\xa0", "").replace("\n", "")]
            serp_list.append(inside)
        except:
            continue
            
            
def next_page(soup):
    next_page = soup.find_all(href=re.compile("/search?"))
    
    if "下一頁" in str(next_page[-1]):    
        next_page_url = next_page[-1].get("href")
        domain = "https://www.google.com.tw"
        whole_url = domain + next_page_url
        return(whole_url)
    else:
        return(None)
        
        
      
