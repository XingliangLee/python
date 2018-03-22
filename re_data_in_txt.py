# -*- coding: utf-8 -*-
"""
Created on Fri Feb 02 16:29:01 2018

@author: mislu
"""
#查找处于文件中的所有数字，并计算其总和
import re
#打开文件
fhand = open("regex_sum_73281.txt")
#总和
total_sum = 0
for line in fhand:
    sum = 0
    digist_in_line = re.findall("\d+", line)
    #re.findall返回的是字符串的list，需要先转换为数字的list
    new_num = map(int, digist_in_line)
    #数组不为空，计算其和
    if new_num:
         for element in new_num:
             sum = sum + element    
         total_sum = total_sum + sum
print total_sum