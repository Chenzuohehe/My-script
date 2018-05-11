# -*- coding: utf-8 -*-
#encoding=utf-8
# 目标：根据提供的1024 像素的图生成对应的图还有名字
# https://blog.csdn.net/Richie_ll/article/details/69206210


#导入模块
from PIL import Image
import os
#读取文件
im_path = r'/Users/chenzuo/Desktop/test.png' #原图地址

baseP = "/Users/chenzuo/Desktop" #保存地址

iconFile = "/Users/chenzuo/Desktop"
sizes = []
fileNames = []

im = Image.open(im_path)


def listdir():
    dirfile = os.listdir(iconFile)
    names = []
    for filename in dirfile:
        if not filename.startswith('.'):
            names.append(filename)
    fileNames = names

def resizeIcon():
    for i in len(sizes):
        size = sizes[i]
        filename = fileNames[i]
        re = im.resize((size, size))
        re.save(r'%s/%s' %(baseP, filename))

if __name__ == "__main__":
    listdir()
    resizeIcon()








