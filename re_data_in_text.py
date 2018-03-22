# -*- coding: utf-8 -*-
"""
Created on Fri Feb 02 16:23:56 2018

@author: mislu
"""
# 查找文本中所有数字， 并计算其总和
import re
text = '''Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative 
7 and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that 
everyone needs to know how to program ... '''
#找到所有的数字
dig = re.findall("\d+", text)
#计算总和
sum = 0

for element in dig:
    sum = sum + int(element)
print sum