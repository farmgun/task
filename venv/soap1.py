from bs4 import BeautifulSoup
import lxml
from urllib.request import urlopen
import urllib

with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    for tag in soup.find_all("p"):
        print("{0}: {1}".format(tag.name, tag.text))
    print(soup.p)
    tags = soup.find_all(['h2'])
    ln=0
    for tag in tags:
        ln=ln+len(tag.text)
    print(ln)
    root = soup.body
    counter=0
    for e in root.descendants:
        if e.name=='p':
            counter=counter+1
    print(counter)
    print(soup.a)
    c=0
    for tag in soup.find_all('a'):
        if c==0:
            hreff=tag.get('href')
            c+=1
        else:
            pass
    print(hreff)





