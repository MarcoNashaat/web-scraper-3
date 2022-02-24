#enabling https
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(),'html.parser')
two_attr_tags = bs.find_all(lambda tag : len(tag.attrs) == 2)
for tag in two_attr_tags:
    print(tag)