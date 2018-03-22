# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 19:17:00 2018

@author: mislu
"""

# 查找xml网页中所有的数字，并计算总和

import urllib
import xml.etree.ElementTree as ET

# 链接到xml页面
url = 'http://py4e-data.dr-chuck.net/comments_73285.xml'
xml_string = urllib.urlopen(url).read()

# 解析为树
tree = ET.fromstring(xml_string)

# 找到所有count标签
nums = tree.findall(".//count")
# 计算所有count下标签的数子的和
print sum([int(num.text) for num in nums])
