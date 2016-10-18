# -*- coding:utf-8 -*-  
from langconv import *
line = "門"
#转换繁体到简体
line = Converter('zh-hans').convert(line.decode('utf-8'))
line = line.encode('utf-8')
with open("qq.txt",'w') as f:
    f.write(line)

# 转换简体到繁体
# line = Converter('zh-hant').convert(line.decode('utf-8'))
# line = line.encode('utf-8')
