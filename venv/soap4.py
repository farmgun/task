from bs4 import BeautifulSoup
import lxml
from urllib.request import urlopen
import urllib
import requests
import re


url = 'https://www.multitran.com/'
page = urlopen(url)
print(page)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
file=open('file1.html', 'w')
file.write(html)
print(file)
file.close()
with open("file.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    strings = soup.find_all(string=re.compile('Doc'))
    for txt in strings:
        print(" ".join(txt.split()))