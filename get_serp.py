from bs4 import BeautifulSoup
import requests
import re


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
    ahref = soup.select(".fl")
    check_if_next_page_exist = 0
    for urls in ahref:
        if urls.text == "下一頁":
            check_if_next_page_exist += 1
            next_page_url = urls.get("href")
            domain = "https://www.google.com.tw"
            whole_url = domain + next_page_url
            return(whole_url)
    if check_if_next_page_exist == 0:
        return(None)
  
        
      
