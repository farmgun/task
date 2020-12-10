from bs4 import BeautifulSoup
import lxml
from urllib.request import urlopen
import urllib
import requests
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
    root = soup.html
    root_childs = [e.name for e in root.children if e.name is not None]
    print(root_childs)
    root = soup.body
    root_childs = [e.name for e in root.children if e.name is not None]
    print(root_childs)
    print(soup.title)
    a=soup.title
    print(a.text)
    print(soup.findAll('li'))
    print(soup.find_all(string='Doc'))



