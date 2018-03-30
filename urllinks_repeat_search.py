# you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#寻找网页中特定位置的链接，并依次迭代寻找

import urllib
from bs4 import BeautifulSoup
import ssl

#位置与迭代次数
POSITION = 18
REPEAT = 7

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://py4e-data.dr-chuck.net/known_by_Meshach.html'
html = urllib.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')



# Retrieve all of the anchor tags
tags = soup('a')

# 迭代寻找链接 
for i in range(REPEAT):
    url = tags[POSITION - 1].get('href', None)
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print url
