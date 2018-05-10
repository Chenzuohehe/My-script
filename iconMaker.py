# -*- coding: utf-8 -*-


# 根据提供的1024 像素的图生成对应的图还有名字

# imagePath = ""

#导入模块
from PIL import Image
#读取文件
im_path = r'/Users/chenzuo/Desktop/test.png'
im = Image.open(im_path)
width, height = im.size
# 宽高
print(im.size, width, height)
# 格式，以及格式的详细描述
print(im.format, im.format_description)

im.save(r'/Users/chenzuo/Desktop/test1.png')
im.show()

# https://blog.csdn.net/Richie_ll/article/details/69206210