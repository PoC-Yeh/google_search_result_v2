from bs4 import BeautifulSoup
import requests
import re
import progressbar
import time
import csv
import pickle
from get_serp import *
from crawl import *


#google_crawl(url, filename)
google_crawl("https://www.google.com.tw/search?biw=1280&bih=398&q=stussy&oq=stussy&gs_l=psy-ab.3..0i131k1j0l3.1118041.1119145.0.1119350.6.6.0.0.0.0.80.355.6.6.0....0...1.1.64.psy-ab..0.6.354.6nRIogRrGKQ", "stussy")
