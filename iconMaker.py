# -*- coding: utf-8 -*-
#encoding=utf-8
# 目标：根据提供的图生成对应像素的图还有名字

from PIL import Image

im_path = r'/Users/chenzuo/Desktop/icon1024.png' #原图地址
baseP = "/Users/chenzuo/Desktop" #保存地址
sizes = [20,29,40,50,57,58,60,72,76,80,87,100,114,120,144,152,167,180,1024]

im = Image.open(im_path)

def makeIcons():
    for i in range(len(sizes)):
        resizedIm = im.resize((sizes[i], sizes[i]))
        name = "%s/_%s.png" % (baseP, sizes[i])
        # print (name)
        resizedIm.save(name)

if __name__ == "__main__":
    makeIcons()









