# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# 查找网页中<span>标签下的所有数字，并计算其总和
import urllib
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_73283.html'
html = urllib.urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
#计数总和初始0
sum = 0
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('class', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    sum += int(tag.contents[0])
    
print sum
