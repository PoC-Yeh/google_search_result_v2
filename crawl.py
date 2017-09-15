from bs4 import BeautifulSoup
import requests
import re
import progressbar
import time
import csv
import pickle
from get_serp import *
from crawl import *


crawl("https://www.google.com.tw/search?q=XXX", "filename")
