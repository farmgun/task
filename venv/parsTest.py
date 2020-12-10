from urllib.request import urlopen
from selenium import webdriver
from tqdm import tqdm_notebook as tqdmn
import folium
import urllib
import simplejson
from geopy.geocoders import Nominatim

import requests
import json
url = 'https://en.wikipedia.org/wiki/Main_Page'
page = urlopen(url)
print(page)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
session = requests.session()
response = session.get('https://en.wikipedia.org/wiki/Main_Page')
if response.status_code == 200:
    print("Success")
else:
    print("Bad result")
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(title)










