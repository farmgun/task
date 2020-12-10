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
    for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, ag.text))
    for tag in soup.find_all("li"):
        for tag in soup.find_all("a") :
            print(tag.get('href'))
    lst=[]
    for tag in soup.find_all("h1", "h2"):
        lst.append(tag.name)
    print(lst)










